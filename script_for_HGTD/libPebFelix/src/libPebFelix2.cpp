#include <iomanip>
#include <iostream>
#include <unistd.h>

#include "FlxParser.h"
#include "FlxReceiver.h"
#include "FlxUpload.h"

using namespace std;

int g_dma_write = -1; // Autoselect FromHost DMA controller index
int g_dma_read = 0;
bool g_use_intrpt = false;
int g_cardnr = 1; // TODO make configurable if host has more than 1 card!
int g_timeout_us2 = 8000;

bool g_debug = false;

class SerialComm {

public:
  SerialComm(SerialComm& rhs) = delete;

  void operator=(const SerialComm& rhs) = delete;

  static SerialComm* getInstance(const std::string& output_filename = "", int cardnr = 0) {
    if (s_instance == nullptr) {
      s_instance = new SerialComm(output_filename, cardnr);
      s_instance->openFile(output_filename);
    }
    return s_instance;
  }

  long long getNTransactions() { return m_ntransactions; }

  long long getNBadTransactions() { return m_n_badtransactions; }

  void setNBadTransactions(long long n) { m_n_badtransactions = n; }

  std::string getOutputFilename() { return m_outfilename; }

  void deleteInstance() {
    cout << "[SerialComm] deleting instance after " << m_ntransactions
         << " transactions." << endl;
    fup.stop();
    frecvr.stop();
    delete s_instance;
    s_instance = nullptr;
  }

  ~SerialComm() = default;

protected:
  SerialComm(const std::string& output_filename, int cardnr);

  void openFile(const std::string& output_filename) {

    if (!output_filename.empty()) {
      m_outfile.open(output_filename.c_str(), std::ios_base::app);
      m_write_of = true;
      m_outfilename = output_filename;
    }
  }

  static SerialComm* s_instance;

public:
  int lpgbt_regs(int cardnr, int linknr, int i2c_addr, int reg_addr, bool read,
                 int nbytes, uint8_t* reg_vals, bool use_ec, bool debug,
                 bool display);

private:
  bool receiveIcReply(FlxReceiver* frecvr, int linknr, int reg_addr, int nbytes,
                      uint8_t* reg_vals, int timeout_us, bool use_ec,
                      bool lpgbt_v1, bool debug, bool display);

  bool writeIcRegs(FlxUpload* fup, FlxReceiver* frecvr, int linknr,
                   int i2c_addr, int reg_addr, int nbytes, uint8_t* reg_vals,
                   bool use_ec, bool lpgbt_v1, bool debug, bool display);

  bool readIcRegs(FlxUpload* fup, FlxReceiver* frecvr, int linknr, int i2c_addr,
                  int reg_addr, int nbytes, uint8_t* reg_vals, bool use_ec,
                  bool lpgbt_v1, bool debug, bool display);

  FlxParser fparser;
  FlxUpload fup;
  FlxReceiver frecvr;

  std::ofstream m_outfile;
  std::string m_outfilename;
  bool m_write_of;

  static long long m_ntransactions;
  static long long m_nreads;
  static long long m_nwrites;
  static long long m_n_badtransactions;
};

SerialComm::SerialComm(const std::string& output_filename, int cardnr)
    : fparser(),
      fup(cardnr, 0, g_dma_write),
      frecvr(cardnr, 64 * 1024 * 1024, g_dma_read, false),
      m_write_of(false) {
  if (fup.hasError()) {
    cout << "### " << fup.errorString() << endl;
    fup.stop();
    return;
  }
  if (m_ntransactions == 0)
    cout << "Opened FLX-device " << cardnr << ", firmw "
         << fup.firmwareVersion() << endl;

  if (fup.fanOutLocked())
    cout << "**NB**: FanOut-Select registers are locked!" << endl;
  fup.setFanOutForDaq();

  if (frecvr.hasError()) {
    cout << "### " << frecvr.errorString() << endl;
    cout << "###1 " << endl;
    fup.stop();
    frecvr.stop();
    return;
  }
  frecvr.setUseInterrupt(g_use_intrpt);

  fparser.setReceiver(&frecvr);
}

int SerialComm::lpgbt_regs(int cardnr, int linknr, int i2c_addr, int reg_addr,
                           bool read, int nbytes, uint8_t* reg_vals,
                           bool use_ec, bool debug, bool display) {

  bool tmp;
  if (read) {
    if (m_write_of) {
      m_outfile << "READ, ";
      if (use_ec) {
        m_outfile << "EC, ";
      } else {
        m_outfile << "IC, ";
      }
      m_outfile << "I2C adr: " << i2c_addr;
      m_outfile << ", reg adr: " << reg_addr;
      m_outfile << ", Nbytes: " << nbytes << "\n";
    }

    tmp = readIcRegs(&fup, &frecvr, linknr, i2c_addr, reg_addr, nbytes,
                     reg_vals, use_ec, true, debug, display);
    m_nreads++;
    m_ntransactions++;

  } else {
    if (m_write_of) {
      m_outfile << "WRITE, ";
      if (use_ec) {
        m_outfile << "EC, ";
      } else {
        m_outfile << "IC, ";
      }
      m_outfile << "I2C adr: " << i2c_addr;
      m_outfile << ", reg adr: " << reg_addr;
      m_outfile << ", Nbytes: " << nbytes << ", Values: ";
      for (int i = 0; i < nbytes; i++) {
        m_outfile << (uint32_t)reg_vals[i] << " ";
      }
      m_outfile << "\n";
    }

    tmp = writeIcRegs(&fup, &frecvr, linknr, i2c_addr, reg_addr, nbytes,
                      reg_vals, use_ec, true, debug, display);
    m_nwrites++;
    m_ntransactions++;
  }

  if (tmp) {
    if (g_debug) {
      cout << (read ? "SerialComm:: Successful read from "
                    : "SerialComm:: Successful writing to ")
           << reg_addr << endl;
      cout << "[lpgbt_regs] Sent " << m_ntransactions << " transactions."
           << endl;
    }

    return 0;
  } else {
    m_n_badtransactions++;
    // error
    if (fup.hasError()) {
      cout << "SerialComm:: ### FUP: " << fup.errorString() << endl;
    }

    if (fup.fanOutLocked())
      cout << "SerialComm:: **NB**: FanOut-Select registers are locked!"
           << endl;

    if (frecvr.hasError()) {
      cout << "SerialComm:: ### FRCVF: " << frecvr.errorString() << endl;
    }
    return 1;
  }
}

bool SerialComm::receiveIcReply(FlxReceiver* frecvr, int linknr, int reg_addr,
                                int nbytes, uint8_t* reg_vals, int timeout_us,
                                bool use_ec, bool lpgbt_v1, bool debug,
                                bool display) {
  // Function expects to read a single reply
  // with one or more register values returned

  // The IC (or EC) elink number from the original GBT firmware
  // (maintained within the software; will be mapped to the real number
  //  for Phase2 firmwares, internally)
  int egroup = 7;
  int epath = 6;
  if (use_ec)
    epath = 7;

  int elinknr = ((linknr << BLOCK_GBT_SHIFT) | (egroup << BLOCK_EGROUP_SHIFT) |
                 (epath << BLOCK_ELINK_SHIFT));

  uint8_t* chunkdata = 0;
  uint32_t size, chunknr = 1;
  uint32_t parity_start_index = (lpgbt_v1 ? 0 : 2);
  int offset = (lpgbt_v1 ? 0 : 1);
  bool reply_received = false;
  while (not reply_received and
         fparser.nextChunkRecvd(&chunkdata, &size, timeout_us, elinknr)) {
    if (size == 0) {
      if (debug) {
        cout << "Size is 0\n";
      }
      continue;
    }

    // Process chunk from the IC (or EC) channel
    uint32_t frame_len = size;
    uint8_t* frame = chunkdata;
    // Check reply frame CRC
    // (do not include I2C-address and zero-byte, in case of lpGBTv0)
    if (frame_len > 2) {
      if (debug)
        cout << "Chunk " << chunknr << ": ";
      uint8_t parity = 0;
      for (uint32_t i = parity_start_index; i < frame_len - 1; ++i)
        parity ^= frame[i];
      if (parity != frame[frame_len - 1]) {
        cout << hex << setfill('0') << "### Parity " << setw(2)
             << (uint32_t)frame[frame_len - 1] << ", expected " << setw(2)
             << (uint32_t)parity << dec << setfill(' ');
        if (!debug)
          cout << endl;
      } else {
        if (debug)
          cout << "parity OK";
      }

      if (debug) {
        if (frame[0] & 1)
          cout << ",  READ:";
        else
          cout << ", WRITE:";
      }
    }

    if (debug) {
      // Display IC frame bytes
      cout << hex << uppercase << setfill('0');
      for (uint32_t i = 0; i < frame_len; ++i)
        cout << " " << setw(2) << (uint32_t)frame[i];
      cout << endl << dec << nouppercase << setfill(' ');
    }

    // Display returned register values in IC frame
    // (I2C-address, zero-byte (lpGBTv0), command, #bytes, #address, parity:
    //  7 (v1) or 8 (v0) bytes in total) (###TBD: define v0 and v1 structs?)
    int data_len = frame_len - (offset + 1 + 1 + 2 + 2 + 1);
    if (data_len > 0 && nbytes > 0) {
      uint32_t len =
          ((uint32_t)frame[offset + 2] + ((uint32_t)frame[offset + 3] << 8));
      uint32_t addr =
          ((uint32_t)frame[offset + 4] + ((uint32_t)frame[offset + 5] << 8));

      cout << hex << uppercase << setfill('0');
      if (len == (uint32_t)nbytes && addr == (uint32_t)reg_addr) {
        if (display) {
          cout << "Address 0x" << setw(3) << addr << ":";
          for (int i = 0; i < nbytes; ++i) {
            if (i > 0 && (i & 0xF) == 0)
              cout << endl << "              ";
            cout << " 0x" << setw(2) << (uint32_t)frame[offset + 6 + i];
          }
          cout << endl;
        }
        reply_received = true;
      } else if (debug) {
        cout << "### Unexpected length or address: " << dec << len << hex
             << ", 0x" << setw(3) << addr << " (expected " << nbytes << ", 0x"
             << setw(3) << reg_addr << ")" << endl;
      }
      cout << dec << nouppercase << setfill(' ');

      // Extract the register values to return
      for (int i = 0; i < nbytes; ++i)
        reg_vals[i] = frame[offset + 6 + i];
    }
    ++chunknr;
  }

  return reply_received;
}

bool SerialComm::writeIcRegs(FlxUpload* fup, FlxReceiver* frecvr, int linknr,
                             int i2c_addr, int reg_addr, int nbytes,
                             uint8_t* reg_vals, bool use_ec, bool lpgbt_v1,
                             bool debug, bool display) {
  if (!fup->writeIcChannel(linknr, i2c_addr, reg_addr, nbytes, reg_vals, use_ec,
                           lpgbt_v1))
    cout << "### writeIcRegs(0x" << hex << reg_addr << dec
         << ",nbytes=" << nbytes << "): " << fup->errorString() << endl;
  ;
  // Receive the reply (containing nbytes bytes) and display
  bool reply_received =
      receiveIcReply(frecvr, linknr, reg_addr, nbytes, reg_vals, g_timeout_us2,
                     use_ec, lpgbt_v1, debug, display);
  if (!reply_received && display)
    cout << "### Reply not received (addr=0x" << hex << reg_addr << ")" << dec
         << endl;

  return reply_received;
}

bool SerialComm::readIcRegs(FlxUpload* fup, FlxReceiver* frecvr, int linknr,
                            int i2c_addr, int reg_addr, int nbytes,
                            uint8_t* reg_vals, bool use_ec, bool lpgbt_v1,
                            bool debug, bool display) {
  if (!fup->readIcChannel(linknr, i2c_addr, reg_addr, nbytes, use_ec, lpgbt_v1))
    cout << "### readIcRegs(0x" << hex << reg_addr << dec
         << ",nbytes=" << nbytes << "): ";
  // Receive the reply (containing nbytes bytes) and display
  bool reply_received =
      receiveIcReply(frecvr, linknr, reg_addr, nbytes, reg_vals, g_timeout_us2,
                     use_ec, lpgbt_v1, debug, display);
  if (!reply_received && display)
    cout << "### Reply not received (addr=0x" << hex << reg_addr << ")" << endl;

  if (debug)
    return true;
  return reply_received;
}

SerialComm* SerialComm::s_instance = nullptr;

long long SerialComm::m_ntransactions(0);
long long SerialComm::m_nreads(0);
long long SerialComm::m_nwrites(0);
long long SerialComm::m_n_badtransactions(0);

// Functions exposed to python interface
extern "C" {

SerialComm* init(char* out_filename, int cardnr) {
  return SerialComm::getInstance(std::string(out_filename), cardnr);
}

void deleteInstance(SerialComm* self) { self->deleteInstance(); }

int lpgbt_regs_serialcomm(SerialComm* self, int cardnr, int linknr,
                          int i2c_addr, int reg_addr, bool read, int nbytes,
                          uint8_t* reg_vals, bool use_ec, bool debug,
                          bool display) {
  if (self->getNBadTransactions() >= 5) {
    std::cout << "WARNING: too many bad transactions, resetting SerialComm\n";
    std::string filename = self->getOutputFilename();
    self->deleteInstance();
    SerialComm* newself = SerialComm::getInstance(filename);
    newself->setNBadTransactions(0);
    return newself->lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes,
                               reg_vals, use_ec, debug, display);
  }
  return self->lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes,
                          reg_vals, use_ec, debug, display);
}
}

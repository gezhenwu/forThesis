#include <iostream>
#include <iomanip>
using namespace std;
#include <unistd.h>
#include <cstring>

extern "C"{
int lpgbt_regs(int cardnr, int linknr, int i2c_addr, int reg_addr, 
  bool read, int nbytes, uint8_t *reg_vals,
  bool use_ec, bool debug, bool display);
}

// ----------------------------------------------------------------------------

int main( int argc, char *argv[] )
{
  int    cardnr      = 0;
  int    linknr      = 0;
  int    i2c_addr    = 0x70;
  int    reg_addr    = 0;
  bool   use_ec      = false;
  bool   display     = true;
  bool   debug       = true;

  int nbytes = 8;
  uint8_t regarray[512];
  regarray[0] = 0x55;
  regarray[1] = 2;
  regarray[2] = 3;
  regarray[3] = 4;
  regarray[4] = 5;
  regarray[5] = 6;
  regarray[6] = 7;
  regarray[7] = 8;

  uint8_t data[512];

  bool tmp;

  tmp = lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, 
    true, nbytes, data, 
    use_ec, debug, display);

  printf("return:%d\n", tmp);

  tmp = lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, 
    true, nbytes, data, 
    use_ec, debug, display);

  printf("return:%d\n", tmp);

  // tmp = lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, 
  //   false, nbytes, regarray, 
  //   use_ec, display);

  // printf("return:%d\n", tmp);

  return 0;
}



// ----------------------------------------------------------------------------

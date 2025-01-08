`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: NJU & IHEP
// Engineer: 
// 
// Create Date: 2022/12/01 20:30:11
// Design Name: 
// Module Name: timingSource
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module timingSource(
  input [1:0] type,
  input en_TDPU,
  input trigger,
  input reset,
  input clk40,
  input clk160,
  input clk_S,  
  input dataclk, 
  input [9:0] vth,
  input [231:0] vthc,
  input [28:0] pixelOn,
  output CharIsK,
  input [7:0] frameData,
  output [7:0] data_to_code
    );

  
  reg [9:0] BCID; 
  wire [4:0] error; 
  reg [5:0] L0L1;    
  wire parity;
  wire [23:0] header;
  reg pixelOn_r;
  wire [7:0] vthc_pix[28:0];
  reg [10:0] thres_sum; 
  reg [7:0] j;
  reg [9:0] thres_ref;
  reg enable;
  reg kischar_std;
  reg kischar_test;
  reg [7:0] cnt;
  wire [7:0] pixel_addr;  
  reg validDtae;    
  reg [23:0] sram;
  reg [5:0] tot_prbs;
  reg [4:0] toa_prbs;
  wire [7:0] tot;
  wire [6:0] toa;
  wire [7:0] crc8;
  reg [2:0] l;
  reg [23:0] testFrame;
  reg validFrame;
  reg [1:0] tick;
  wire empty;
  wire full;
  wire wr_en;
  wire rd_en;
  wire [24:0] din_fifo;
  wire [24:0] dout_fifo;    
  parameter IDLE =24'b10111100_11111100_11111100; //k28.5 k28.7,k28.7  bc fc fc
  //----------header----------
  //bunch crossing counter
  always @(posedge clk40 or posedge reset) begin
    if(reset) begin
      BCID<=10'b0;
    end
    else begin
      if(BCID==11'b11_1111_1111) begin
        BCID<=10'b0;
      end
      else begin
        BCID<=BCID+1;
      end
    end
  end
  //always set error=5'b0, no meaning
  assign error = 5'b0;
  //L0/L1 trigger counter
    reg trigger_r;
    reg trigger_rr;
    always @(posedge clk160) begin
        trigger_r <= trigger;
    end

    always @(posedge clk160) begin
        trigger_rr <= trigger_r;
    end

  always @(posedge clk160 or posedge reset) begin
    if(reset) begin
      L0L1<=6'b0;
    end
    else begin
      if(L0L1==6'b11_1111) begin
        L0L1<=6'b0;
      end
      else if(trigger_rr) begin
        L0L1<=L0L1+1;
      end
      else begin
        L0L1<=L0L1;
      end
    end
  end
  //parity
  assign parity = ^{BCID,error,L0L1};
  //header
  assign header = {type,error,BCID,L0L1,parity};

  //-----state for recycling pixels-----
    wire [7:0] j_temp;
    assign j_temp = (j==8'he5)? 8'h0 : j+1;
    always @(posedge clk_S or posedge reset ) begin
        if(reset) j <= 8'he5;
        else if(!en_TDPU) j <= 8'he5;
        else if(trigger_rr) j <= j_temp;
        else if(j != 8'he5) j <= j_temp;
        else  j <= 8'he5;        
    end

  //-----pixel enable/disable-----
  //considering the limited cells of FPGA, only the first 1 collums can be configured individually.
  //Other collums are determined by the first pixel of each row.
  always @(posedge clk_S) begin
    case(j)
      8'h0: begin
        pixelOn_r <= 1'b0;    
      end
      8'he2: begin
        pixelOn_r <= 1'b0;        
      end   
      8'he3: begin
        pixelOn_r <= 1'b0;        
      end   
      8'he4: begin
        pixelOn_r <= 1'b0;        
      end   
      8'he5: begin
        pixelOn_r <= 1'b0;         
      end      
      default: begin
        if(j>0&&j<=15) pixelOn_r <= pixelOn[28];
        if(j>15&&j<=30) pixelOn_r <= pixelOn[27];
        if(j>30&&j<=45) pixelOn_r <= pixelOn[26];
        if(j>45&&j<=60) pixelOn_r <= pixelOn[25];
        if(j>60&&j<=75) pixelOn_r <= pixelOn[24];
        if(j>75&&j<=90) pixelOn_r <= pixelOn[23];
        if(j>90&&j<=105) pixelOn_r <= pixelOn[22];
        if(j>105&&j<=120) pixelOn_r <= pixelOn[21];
        if(j>120&&j<=135) pixelOn_r <= pixelOn[20];
        if(j>135&&j<=150) pixelOn_r <= pixelOn[19];
        if(j>150&&j<=165) pixelOn_r <= pixelOn[18];
        if(j>165&&j<=180) pixelOn_r <= pixelOn[17];
        if(j>180&&j<=195) pixelOn_r <= pixelOn[16];
        if(j>195&&j<=210) pixelOn_r <= pixelOn[15];
        if(j>210&&j<=225) pixelOn_r <= pixelOn[225-j];   
      end      
    endcase    
  end

  //-----total threshold-----
  //considering the limited cells of FPGA, only the first 1 collums can be configured individually.
  //Other collums are determined by the first pixel of each row.
  always @(posedge clk_S) begin
    case(j)
      8'h0: begin
        thres_sum <= 11'h7ff;    
      end
      8'he2: begin
        thres_sum <= 11'h7ff;        
      end  
      8'he3: begin
        thres_sum <= 11'h7ff;        
      end   
      8'he4: begin
        thres_sum <= 11'h7ff;        
      end   
      8'he5: begin
        thres_sum <= 11'h7ff;         
      end      
      default: begin
        if(j>0&&j<=15) thres_sum <= vth+vthc_pix[28][7:0];
        if(j>15&&j<=30) thres_sum <= vth+vthc_pix[27][7:0];
        if(j>30&&j<=45) thres_sum <= vth+vthc_pix[26][7:0];
        if(j>45&&j<=60) thres_sum <= vth+vthc_pix[25][7:0];
        if(j>60&&j<=75) thres_sum <= vth+vthc_pix[24][7:0];
        if(j>75&&j<=90) thres_sum <= vth+vthc_pix[23][7:0];
        if(j>90&&j<=105) thres_sum <= vth+vthc_pix[22][7:0];
        if(j>105&&j<=120) thres_sum <= vth+vthc_pix[21][7:0];
        if(j>120&&j<=135) thres_sum <= vth+vthc_pix[20][7:0];
        if(j>135&&j<=150) thres_sum <= vth+vthc_pix[19][7:0];
        if(j>150&&j<=165) thres_sum <= vth+vthc_pix[18][7:0];
        if(j>165&&j<=180) thres_sum <= vth+vthc_pix[17][7:0];
        if(j>180&&j<=195) thres_sum <= vth+vthc_pix[16][7:0];
        if(j>195&&j<=210) thres_sum <= vth+vthc_pix[15][7:0];
        if(j>210&&j<=225) thres_sum <= vth+vthc_pix[225-j][7:0];   
      end      
    endcase    
  end
 
  //set the constant thresh for each pixel, make pixels responding differently to different vth+vthc
  //A S-curve can be obtained by scanning vth+vthc
  always @(posedge clk_S) begin
    case(j)
      8'h0: begin
        thres_ref <= 650;    
      end
      8'he2: begin
        thres_ref <= 650;  
      end   
      8'he3: begin
        thres_ref <= 650;  
      end   
      8'he4: begin
        thres_ref <= 650;  
      end   
      8'he5: begin
        thres_ref <= 650;   
      end      
      default: begin
        thres_ref <= thres_ref-2;       
      end
    endcase
  end

  //pixel address
  assign pixel_addr =  j>1&&j<=16?     240-j : 
                      (j>16&&j<=31?    239-j :
                      (j>31&&j<=46?    238-j :
                      (j>46&&j<=61?    237-j :
                      (j>61&&j<=76?    236-j :
                      (j>76&&j<=91?    235-j :
                      (j>91&&j<=106?   234-j :
                      (j>106&&j<=121?  233-j :
                      (j>121&&j<=136?  232-j :
                      (j>136&&j<=151?  231-j :
                      (j>151&&j<=166?  230-j :
                      (j>166&&j<=181?  229-j :
                      (j>181&&j<=196?  228-j :
                      (j>196&&j<=211?  227-j :
                      (j>211&&j<=226?  226-j : 8'hff))))))))))))));

  //generate tot and toa from prbs
  always @(posedge clk_S) begin
    if(reset) begin
      tot_prbs <= 6'b00_0001;
      toa_prbs <= 5'b0_0001;
    end
    else begin
      tot_prbs[5:1] <= tot_prbs[4:0];
      tot_prbs[0] <=  tot_prbs[5]^tot_prbs[0];
      toa_prbs[4:1] <= toa_prbs[3:0];
      toa_prbs[0] <=  toa_prbs[4]^toa_prbs[0];      
    end
  end
  assign tot = {2'b11,tot_prbs};
  assign toa = {2'b11,toa_prbs};

  //-----crc for trailer----
  crc8_24 crc_inst(
    .clk(clk_S),
    .rst(reset),
    .data_in(sram),
    .crc_en(1'b1),
    .crc_out(crc8)
  );

  //-----std frame-----
  //IDLE--header--std frame--trailler
  always @(posedge clk_S) begin
    case(j)
      8'h0: begin
        validDtae <= 1'b1;
        sram <= IDLE;
        enable <= 1'b1;
        kischar_std <= 1'b1;
      end
      8'h1: begin
        validDtae <= 1'b1;
        sram <= header; 
        enable <= 1'b1;
        kischar_std <= 1'b0;
      end
      8'he3: begin
        validDtae <= 1'b1;
        sram <= {8'hf0,cnt,crc8}; //trailer
        enable <= 1'b1;
        kischar_std <= 1'b0;
      end
      8'he4: begin
        validDtae <= 1'b1;
        sram <= IDLE;
        enable <= 1'b1;
        kischar_std <= 1'b1;
      end      
      8'he5: begin
        validDtae <= 1'b0;
        sram <= IDLE;
        enable <= 1'b0;
        kischar_std <= 1'b1;
      end 
      default: begin
        if(!pixelOn_r) begin
          validDtae <= 1'b0;
          sram <= {pixel_addr,1'b0,tot,toa};
          enable <= 1'b0;
          kischar_std <= 1'b0;      
        end
        else begin
          validDtae <= 1'b1;
          if(thres_sum<=thres_ref) begin
            sram <= {pixel_addr,1'b0,tot,toa};
            enable <= 1'b1;
            kischar_std <= 1'b0;
          end
          else begin
            sram <= {pixel_addr,1'b0,tot,toa}; 
            enable <= 1'b0;
            kischar_std <= 1'b0;
          end
        end         
      end
    endcase
  end

  //cnt: The number of hitting pixels 
  always @(posedge clk_S) begin
    case(j)
      8'h0: begin
        cnt <= 8'h0;     
      end
      8'h1: begin
        cnt <= 8'h0;     
      end
      8'he3: begin 
        cnt <= cnt;         
      end   
      8'he4: begin
        cnt <= cnt;         
      end   
      8'he5: begin
        cnt <= 8'h0;         
      end      
      default: begin
        if(enable) cnt <= cnt+1;        
      end
    endcase
  end

  //-----test frame-----
    wire [2:0] l_temp;
    assign l_temp = (l==3'b111)? 3'b0 : l+1;
    always @(posedge clk_S or posedge reset ) begin
        if(reset) l <= 3'b111;
        else if(!en_TDPU) l <= 3'b111;
        else if(trigger_rr) l <= l_temp;
        else if(l != 3'b111) l <= l_temp;
        else  l <= 3'b111;        
    end

  always @(posedge clk_S) begin
    case(l)
      2'b00: begin
        testFrame = IDLE;
        validFrame = 1'b1;
        kischar_test <=1'b1;
      end
      2'b01: begin
        testFrame = header;
        validFrame = 1'b1;
        kischar_test <=1'b0;
      end
      2'b10: begin
        testFrame = {3{frameData}};
        validFrame = 1'b1;
        kischar_test <=1'b0;
      end
      2'b11: begin
        testFrame = IDLE;
        validFrame = 1'b1;
        kischar_test <=1'b1;
      end
      default: begin
        testFrame = IDLE;
        validFrame = 1'b0;
        kischar_test <=1'b1;
      end
    endcase
  end

  //-----fifo-----
  always @(posedge dataclk or posedge reset) begin
    if(reset) begin
      tick <= 2'b00;
    end
    else begin
      if(tick==2'b10) tick <= 2'b00;
      else tick <= tick+1;
    end    
  end

  assign wr_en = (type==2'b00)? (!full && validDtae) : ((type==2'b10)? (!full && validFrame) : 1'b0);
  assign rd_en = (!empty) && (tick==2'b00);
  assign din_fifo = (type==2'b00)? (enable? {kischar_std,sram} : {1'b1,IDLE}) : ((type==2'b10)? {kischar_test,testFrame} : {1'b1,IDLE});

  xpm_fifo_async #(
    .CASCADE_HEIGHT(0),        // DECIMAL
    .CDC_SYNC_STAGES(2),       // DECIMAL
    .DOUT_RESET_VALUE("0"),    // String
    .ECC_MODE("no_ecc"),       // String
    .FIFO_MEMORY_TYPE("auto"), // String
    .FIFO_READ_LATENCY(1),     // DECIMAL default：1
    .FIFO_WRITE_DEPTH(2048),   // DECIMAL default: 2048
    .FULL_RESET_VALUE(0),      // DECIMAL
    .PROG_EMPTY_THRESH(10),    // DECIMAL
    .PROG_FULL_THRESH(2000),     // DECIMAL
    .RD_DATA_COUNT_WIDTH(1),   // DECIMAL
    .READ_DATA_WIDTH(25),      // DECIMAL
    .READ_MODE("std"),         // String default: "std""fwft"
    .RELATED_CLOCKS(0),        // DECIMAL
    .SIM_ASSERT_CHK(0),        // DECIMAL; 0=disable simulation messages, 1=enable simulation messages
    .USE_ADV_FEATURES("0000"), // String  Frans-"0000"  : 0707
    .WAKEUP_TIME(0),           // DECIMAL
    .WRITE_DATA_WIDTH(25),     // DECIMAL
    .WR_DATA_COUNT_WIDTH(1)    // DECIMAL
  )
  xpm_fifo_async_inst (
    .almost_empty(),   // 1-bit output: Almost Empty : When asserted, this signal indicates that
                                    // only one more read can be performed before the FIFO goes to empty.

    .almost_full(),     // 1-bit output: Almost Full: When asserted, this signal indicates that
                                    // only one more write can be performed before the FIFO is full.

    .data_valid(),       // 1-bit output: Read Data Valid: When asserted, this signal indicates
                                    // that valid data is available on the output bus (dout).

    .dbiterr(),             // 1-bit output: Double Bit Error: Indicates that the ECC decoder detected
                                    // a double-bit error and data in the FIFO core is corrupted.

    .dout(dout_fifo),                   // READ_DATA_WIDTH-bit output: Read Data: The output data bus is driven
                                    // when reading the FIFO.

    .empty(empty),                 // 1-bit output: Empty Flag: When asserted, this signal indicates that the
                                    // FIFO is empty. Read requests are ignored when the FIFO is empty,
                                    // initiating a read while empty is not destructive to the FIFO.

    .full(full),                   // 1-bit output: Full Flag: When asserted, this signal indicates that the
                                    // FIFO is full. Write requests are ignored when the FIFO is full,
                                    // initiating a write when the FIFO is full is not destructive to the
                                    // contents of the FIFO.

    .overflow(),           // 1-bit output: Overflow: This signal indicates that a write request
                                    // (wren) during the prior clock cycle was rejected, because the FIFO is
                                    // full. Overflowing the FIFO is not destructive to the contents of the
                                    // FIFO.

    .prog_empty(),       // 1-bit output: Programmable Empty: This signal is asserted when the
                                    // number of words in the FIFO is less than or equal to the programmable
                                    // empty threshold value. It is de-asserted when the number of words in
                                    // the FIFO exceeds the programmable empty threshold value.

    .prog_full(),         // 1-bit output: Programmable Full: This signal is asserted when the
                                    // number of words in the FIFO is greater than or equal to the
                                    // programmable full threshold value. It is de-asserted when the number of
                                    // words in the FIFO is less than the programmable full threshold value.

    .rd_data_count(), // RD_DATA_COUNT_WIDTH-bit output: Read Data Count: This bus indicates the
                                    // number of words read from the FIFO.

    .rd_rst_busy(),     // 1-bit output: Read Reset Busy: Active-High indicator that the FIFO read
                                    // domain is currently in a reset state.

    .sbiterr(),             // 1-bit output: Single Bit Error: Indicates that the ECC decoder detected
                                    // and fixed a single-bit error.

    .underflow(),         // 1-bit output: Underflow: Indicates that the read request (rd_en) during
                                    // the previous clock cycle was rejected because the FIFO is empty. Under
                                    // flowing the FIFO is not destructive to the FIFO.

    .wr_ack(),               // 1-bit output: Write Acknowledge: This signal indicates that a write
                                    // request (wr_en) during the prior clock cycle is succeeded.

    .wr_data_count(), // WR_DATA_COUNT_WIDTH-bit output: Write Data Count: This bus indicates
                                    // the number of words written into the FIFO.

    .wr_rst_busy(),     // 1-bit output: Write Reset Busy: Active-High indicator that the FIFO
                                    // write domain is currently in a reset state.

    .din(din_fifo),                     // WRITE_DATA_WIDTH-bit input: Write Data: The input data bus used when
                                    // writing the FIFO.

    .injectdbiterr(1'b0), // 1-bit input: Double Bit Error Injection: Injects a double bit error if
                                    // the ECC feature is used on block RAMs or UltraRAM macros.

    .injectsbiterr(1'b0), // 1-bit input: Single Bit Error Injection: Injects a single bit error if
                                    // the ECC feature is used on block RAMs or UltraRAM macros.

    .rd_clk(dataclk),               // 1-bit input: Read clock: Used for read operation. rd_clk must be a free
                                    // running clock.

    .rd_en(rd_en),                 // 1-bit input: Read Enable: If the FIFO is not empty, asserting this
                                    // signal causes data (on dout) to be read from the FIFO. Must be held
                                    // active-low when rd_rst_busy is active high.

    .rst(reset),                     // 1-bit input: Reset: Must be synchronous to wr_clk. The clock(s) can be
                                    // unstable at the time of applying reset, but reset must be released only
                                    // after the clock(s) is/are stable.

    .sleep(1'b0),                 // 1-bit input: Dynamic power saving: If sleep is High, the memory/fifo
                                    // block is in power saving mode.

    .wr_clk(clk_S),               // 1-bit input: Write clock: Used for write operation. wr_clk must be a
                                    // free running clock.

    .wr_en(wr_en)                  // 1-bit input: Write Enable: If the FIFO is not full, asserting this
                                    // signal causes data (on din) to be written to the FIFO. Must be held
                                    // active-low when rst or wr_rst_busy is active high.

  );

  assign data_to_code = (tick==2'b01)? dout_fifo[23:16] : ((tick==2'b10)? dout_fifo[15:8] : dout_fifo[7:0]);
  assign CharIsK = dout_fifo[24];

  //-----------------vthc for each pixel--------------
  assign vthc_pix[0][7:0] = vthc[7:0];
  assign vthc_pix[1][7:0] = vthc[15:8];
  assign vthc_pix[2][7:0] = vthc[23:16];
  assign vthc_pix[3][7:0] = vthc[31:24];
  assign vthc_pix[4][7:0] = vthc[39:32];
  assign vthc_pix[5][7:0] = vthc[47:40];
  assign vthc_pix[6][7:0] = vthc[55:48];
  assign vthc_pix[7][7:0] = vthc[63:56];
  assign vthc_pix[8][7:0] = vthc[71:64];
  assign vthc_pix[9][7:0] = vthc[79:72];
  assign vthc_pix[10][7:0] = vthc[87:80];
  assign vthc_pix[11][7:0] = vthc[95:88];
  assign vthc_pix[12][7:0] = vthc[103:96];
  assign vthc_pix[13][7:0] = vthc[111:104];
  assign vthc_pix[14][7:0] = vthc[119:112];
  assign vthc_pix[15][7:0] = vthc[127:120];
  assign vthc_pix[16][7:0] = vthc[135:128];
  assign vthc_pix[17][7:0] = vthc[143:136];
  assign vthc_pix[18][7:0] = vthc[151:144];
  assign vthc_pix[19][7:0] = vthc[159:152];
  assign vthc_pix[20][7:0] = vthc[167:160];
  assign vthc_pix[21][7:0] = vthc[175:168];
  assign vthc_pix[22][7:0] = vthc[183:176];
  assign vthc_pix[23][7:0] = vthc[191:184];
  assign vthc_pix[24][7:0] = vthc[199:192];
  assign vthc_pix[25][7:0] = vthc[207:200];
  assign vthc_pix[26][7:0] = vthc[215:208];
  assign vthc_pix[27][7:0] = vthc[223:216];
  assign vthc_pix[28][7:0] = vthc[231:224];
endmodule

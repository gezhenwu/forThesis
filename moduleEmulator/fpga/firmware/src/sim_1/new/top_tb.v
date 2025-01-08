`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2022/12/12 11:35:05
// Design Name: 
// Module Name: top_tb
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


module top_tb;
  reg  LPGBT_HARD_RSTB;  // From lpGBT GPIO
  reg  LPGBT_CLK40M_P;   // 40MHz from lpGBT ECLK
  wire  LPGBT_CLK40M_N;
  reg  FAST_CMD_P;       // From Timing lpGBT Elink
  wire  FAST_CMD_N;
  wire  [1:0]   TIMING_DOUT_P;    // To Timing lpGBT Elink
  wire  [1:0]   TIMING_DOUT_N;
  wire  [1:0]   LUMI_DOUT_P;      // To Lumi lpGBT Elink
  wire  [1:0]   LUMI_DOUT_N;
  // reg   [3:1]   I2C_ADDR;         // Config by PEB
  // reg  I2C_SCL;          // From Timing lpGBT I2C master
  // wire           I2C_SDA;
  // // Test
  // wire   [2:0]   DIPSW;            // Switch SW1
  // wire   [1:0]   TESTPIN;          // Connector J1
  // wire  [2:1]   TP;               
  reg  REFCLK_P;         // Local OSC; 200MHz
  wire  REFCLK_N;
  reg [1:0] state;

  parameter per_40 = 25.0;
  parameter per_200 = 5.0;
  parameter per_320 = 3.125;

  reg clk320;

  initial begin   
    LPGBT_CLK40M_P <= 1'b0;
    REFCLK_P <= 1'b0;
    clk320 <= 1'b0;
    LPGBT_HARD_RSTB <= 1'b1;
    #20 LPGBT_HARD_RSTB <= 1'b0;
    #20 LPGBT_HARD_RSTB <= 1'b1;
  end

    initial begin
        state = 2'b01;
        #30000 state = 2'b10;
        #30000 state = 2'b11;
        #30000 state = 2'b00;
        #30000 state = 2'b01;
    end


  always begin
    #(per_40/2) LPGBT_CLK40M_P = ~LPGBT_CLK40M_P;
  end
  assign LPGBT_CLK40M_N = ~LPGBT_CLK40M_P;

  always begin
    #(per_200/2) REFCLK_P = ~REFCLK_P;
  end
  assign REFCLK_N = ~REFCLK_P;

  always begin
    #(per_320/2) clk320 = ~clk320;
  end

  parameter IDEL = 8'b10101100;
  parameter L0L1 = 8'b10110010;
  parameter BCR  = 8'b10011001;
  reg [1023:0]  fast_cmd = {{126{IDEL}},L0L1,BCR};
  always @(posedge clk320 or negedge LPGBT_HARD_RSTB) begin
    if(!LPGBT_HARD_RSTB) begin
      FAST_CMD_P <= 1'b0;
    end
    else begin
      FAST_CMD_P <= fast_cmd[1023];
      fast_cmd[1023:1] <= fast_cmd[1022:0];
      fast_cmd[0] <= fast_cmd[1023];
    end
  end
  assign FAST_CMD_N = ~FAST_CMD_P;

  top top_inst(
    .LPGBT_HARD_RSTB(LPGBT_HARD_RSTB),  // From lpGBT GPIO
    .LPGBT_CLK40M_P(LPGBT_CLK40M_P),   // 40MHz from lpGBT ECLK
    .LPGBT_CLK40M_N(LPGBT_CLK40M_N),
    .FAST_CMD_P(FAST_CMD_P),       // From Timing lpGBT Elink
    .FAST_CMD_N(FAST_CMD_N),
    .TIMING_DOUT_P(TIMING_DOUT_P),    // To Timing lpGBT Elink
    .TIMING_DOUT_N(TIMING_DOUT_N),
    .LUMI_DOUT_P(LUMI_DOUT_P),      // To Lumi lpGBT Elink
    .LUMI_DOUT_N(LUMI_DOUT_N),
    .I2C_ADDR(),         // Config by PEB
    .I2C_SCL(),          // From Timing lpGBT I2C master
    .I2C_SDA(),
    // Test
    .DIPSW(),            // Switch SW1
    .TESTPIN(),          // Connector J1
    .TP(),               
    .REFCLK_P(REFCLK_P),         // Local OSC, 200MHz
    .REFCLK_N(REFCLK_N)
  );


endmodule

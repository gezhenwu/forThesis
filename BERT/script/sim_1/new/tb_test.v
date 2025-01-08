`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/01/08 11:11:43
// Design Name: 
// Module Name: tb_test
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


module tb_test;
  reg  LPGBT_HARD_RSTB;  // From lpGBT GPIO
  reg  LPGBT_CLK40M_P;   // 40MHz from lpGBT ECLK
  wire  LPGBT_CLK40M_N;
  wire  FAST_CMD_P;       // From Timing lpGBT Elink
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

  reg [7:0] DL_source;
  always @(posedge clk320) begin
    if(!LPGBT_HARD_RSTB) begin
      DL_source <= 8'h01;
    end    
    else begin
      DL_source <= {DL_source[6:0],DL_source[7]^DL_source[6]};
    end
  end
  
  assign FAST_CMD_P = DL_source[7];
  assign FAST_CMD_N = ~DL_source[7];

  top test_inst(
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


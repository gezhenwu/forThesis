`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/01/08 10:45:57
// Design Name: 
// Module Name: test
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


module test(
    input           LPGBT_HARD_RSTB,  // From lpGBT GPIO
    input           LPGBT_CLK40M_P,   // 40MHz from lpGBT ECLK
    input           LPGBT_CLK40M_N,
    input           FAST_CMD_P,       // From Timing lpGBT Elink
    input           FAST_CMD_N,
    output  [1:0]   TIMING_DOUT_P,    // To Timing lpGBT Elink
    output  [1:0]   TIMING_DOUT_N,
    output  [1:0]   LUMI_DOUT_P,      // To Lumi lpGBT Elink
    output  [1:0]   LUMI_DOUT_N,
    input   [3:1]   I2C_ADDR,         // Config by PEB
    input           I2C_SCL,          // From Timing lpGBT I2C master
    inout           I2C_SDA,
    // Test
    input   [2:0]   DIPSW,            // Switch SW1
    inout   [1:0]   TESTPIN,          // Connector J1
    output  [2:1]   TP,               
    input           REFCLK_P,         // Local OSC, 200MHz
    input           REFCLK_N
);

    wire clk40_buf, clk200_buf;
    wire clk40, clk80, clk160, clk200, clk320, clk640;    
    IBUFDS #(
        .DIFF_TERM("FALSE"),       // Differential Termination
        .IBUF_LOW_PWR("TRUE"),     // Low power="TRUE", Highest performance="FALSE" 
        .IOSTANDARD("DIFF_HSUL_12")     // Specify the input I/O standard
    ) IBUFDS_clk40 (
        .O(clk40_buf),  // Buffer output
        .I(LPGBT_CLK40M_P),  // Diff_p buffer input (connect directly to top-level port)
        .IB(LPGBT_CLK40M_N) // Diff_n buffer input (connect directly to top-level port)
    );    
    BUFG BUFG_clk40 (
        .O(clk40), // 1-bit output: Clock output
        .I(clk40_buf)  // 1-bit input: Clock input
    );

    IBUFDS #(
        .DIFF_TERM("FALSE"),       // Differential Termination
        .IBUF_LOW_PWR("TRUE"),     // Low power="TRUE", Highest performance="FALSE" 
        .IOSTANDARD("LVDS_25")     // Specify the input I/O standard
    ) IBUFDS_clk200 (
        .O(clk200_buf),  // Buffer output
        .I(REFCLK_P),  // Diff_p buffer input (connect directly to top-level port)
        .IB(REFCLK_N) // Diff_n buffer input (connect directly to top-level port)
    );    
    BUFG BUFG_clk200 (
        .O(clk200), // 1-bit output: Clock output
        .I(clk200_buf)  // 1-bit input: Clock input
    );

    wire locked, reset;
    clk_wiz_0 clk_gen
    (
    // Clock out ports
    .clk80(clk80),
    .clk160(clk160),
    .clk320(clk320),
    .clk640(clk640),
    // Status and control signals
    .reset(!LPGBT_HARD_RSTB),
    .locked(locked),
    // Clock in ports
    .clk40(clk40)
    );

    assign reset = !locked;

    wire FAST_CMD_BUF, FAST_CMD;
    IBUFDS #(
    .DIFF_TERM("FALSE"),       // Differential Termination
    .IBUF_LOW_PWR("TRUE"),     // Low power="TRUE", Highest performance="FALSE" 
    .IOSTANDARD("DIFF_HSUL_12")     // Specify the input I/O standard
    ) IBUFDS_fastcmd (
        .O(FAST_CMD_BUF),  // Buffer output
        .I(FAST_CMD_N),  // Diff_p buffer input (connect directly to top-level port)
        .IB(FAST_CMD_P) // Diff_n buffer input (connect directly to top-level port)
    );  

    reg CE_inc_dec, INC, LD;
    reg [4:0] CNTVALUEIN;
    wire [4:0] CNTVALUEOUT;
    always @(posedge clk160) begin
        if(reset) begin
            CE_inc_dec <= 1'b1;
            INC <= 1'b1;
            LD <= 1'b0;
            CNTVALUEIN <= 5'b0_0001;
        end
        else begin
            CE_inc_dec <= 1'b1;
            INC <= 1'b1;
            LD <= 1'b0;
            CNTVALUEIN <= 5'b0_0010;          
        end        
    end

    (* IODELAY_GROUP = "test" *) // Specifies group name for associated IDELAYs/ODELAYs and IDELAYCTRL

    IDELAYE2 #(
        .CINVCTRL_SEL("FALSE"),          // Enable dynamic clock inversion (FALSE, TRUE)
        .DELAY_SRC("IDATAIN"),           // Delay input (IDATAIN, DATAIN)
        .HIGH_PERFORMANCE_MODE("FALSE"), // Reduced jitter ("TRUE"), Reduced power ("FALSE")
        .IDELAY_TYPE("VAR_LOAD"),           // FIXED, VARIABLE, VAR_LOAD, VAR_LOAD_PIPE
        .IDELAY_VALUE(1),                // Input delay tap setting (0-31)
        .PIPE_SEL("FALSE"),              // Select pipelined mode, FALSE, TRUE
        .REFCLK_FREQUENCY(200.0),        // IDELAYCTRL clock input frequency in MHz (190.0-210.0, 290.0-310.0).
        .SIGNAL_PATTERN("DATA")          // DATA, CLOCK input signal
    )
    IDELAYE2_inst (
        .CNTVALUEOUT(CNTVALUEOUT), // 5-bit output: Counter value output
        .DATAOUT(FAST_CMD),         // 1-bit output: Delayed data output
        .C(clk160),                     // 1-bit input: Clock input
        .CE(CE_inc_dec),                   // 1-bit input: Active high enable increment/decrement input
        .CINVCTRL(1'b0),       // 1-bit input: Dynamic clock inversion input
        .CNTVALUEIN(CNTVALUEIN),   // 5-bit input: Counter value input
        .DATAIN(1'b0),           // 1-bit input: Internal delay data input
        .IDATAIN(FAST_CMD_BUF),         // 1-bit input: Data input from the I/O
        .INC(INC),                 // 1-bit input: Increment / Decrement tap delay input
        .LD(LD),                   // 1-bit input: Load IDELAY_VALUE input
        .LDPIPEEN(1'b0),       // 1-bit input: Enable PIPELINE register to load data input
        .REGRST(reset)            // 1-bit input: Active-high reset tap-delay input
    );

    wire ready;
    IDELAYCTRL IDELAYCTRL_inst (
        .RDY(ready),       // 1-bit output: Ready output
        .REFCLK(clk200), // 1-bit input: Reference clock input
        .RST(reset)        // 1-bit input: Active high reset input
    );

endmodule

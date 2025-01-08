`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/01/07 17:12:02
// Design Name: 
// Module Name: top
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
module top(
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

    // data pattern checker  
    wire [4:0] CNTVALUEOUT;

    (* IODELAY_GROUP = "test" *) // Specifies group name for associated IDELAYs/ODELAYs and IDELAYCTRL

    IDELAYE2 #(
        .CINVCTRL_SEL("FALSE"),          // Enable dynamic clock inversion (FALSE, TRUE)
        .DELAY_SRC("IDATAIN"),           // Delay input (IDATAIN, DATAIN)
        .HIGH_PERFORMANCE_MODE("TRUE"), // Reduced jitter ("TRUE"), Reduced power ("FALSE")
        .IDELAY_TYPE("FIXED"),           // FIXED, VARIABLE, VAR_LOAD, VAR_LOAD_PIPE
        .IDELAY_VALUE(0),                // Input delay tap setting (0-31)
        .PIPE_SEL("FALSE"),              // Select pipelined mode, FALSE, TRUE
        .REFCLK_FREQUENCY(200.0),        // IDELAYCTRL clock input frequency in MHz (190.0-210.0, 290.0-310.0).
        .SIGNAL_PATTERN("DATA")          // DATA, CLOCK input signal
    )
    IDELAYE2_inst (
        .CNTVALUEOUT(CNTVALUEOUT), // 5-bit output: Counter value output
        .DATAOUT(FAST_CMD),         // 1-bit output: Delayed data output
        .C(clk320),                     // 1-bit input: Clock input
        .CE(1'b0),                   // 1-bit input: Active high enable increment/decrement input
        .CINVCTRL(1'b0),       // 1-bit input: Dynamic clock inversion input
        .CNTVALUEIN(5'h00),   // 5-bit input: Counter value input
        .DATAIN(1'b0),           // 1-bit input: Internal delay data input
        .IDATAIN(FAST_CMD_BUF),         // 1-bit input: Data input from the I/O
        .INC(1'b0),                 // 1-bit input: Increment / Decrement tap delay input
        .LD(1'b0),                   // 1-bit input: Load IDELAY_VALUE input
        .LDPIPEEN(1'b0),       // 1-bit input: Enable PIPELINE register to load data input
        .REGRST(reset)            // 1-bit input: Active-high reset tap-delay input
    );

    wire ready;
    IDELAYCTRL IDELAYCTRL_inst (
        .RDY(ready),       // 1-bit output: Ready output
        .REFCLK(clk200), // 1-bit input: Reference clock input
        .RST(reset)        // 1-bit input: Active high reset input
    );

    reg [7:0] shiftreg;
    always @(posedge clk320) begin
        shiftreg <= {shiftreg[6:0],!FAST_CMD};
    end
    
    
    reg [7:0] cnt;
    always @(posedge clk320) begin
        if(reset) begin
            cnt <= 8'b0;
        end
        else begin
            if(cnt != 8'hff) begin
                cnt <= cnt+1;
            end                
            else begin
                cnt <= cnt;
            end                
        end
    end

    reg [32:0] bitErrorCnt;
    always @(posedge clk320) begin
        if(reset) begin
            bitErrorCnt <= 32'h0;  
        end
        else begin
            if(cnt == 8'hff) begin
                if((shiftreg[7]^shiftreg[6])^shiftreg[0]==1) begin
                    bitErrorCnt <= bitErrorCnt+1;              
                end
                else begin
                    bitErrorCnt <= bitErrorCnt;              
                end                
            end
            else begin
                bitErrorCnt <= 32'h0;
            end
        end
    end

    // //PRBS7 generator: X7+X6+1
    // wire clk_p, clk_s;  //clk_p = 160 && clk_s = 640: data rate = 1280Mbps; clk_p = 80 && clk_s = 320: data rate = 640Mbps; clk_p = 40 && clk_s = 160: data rate = 320Mbps;
    // assign clk_p = clk160;
    // assign clk_s = clk640;
    // reg [7:0] pseudo_data;
    // always @(posedge clk_p) begin
    //     if(reset) begin
    //         pseudo_data <= 8'h01;
    //     end
    //     else begin
    //         pseudo_data[7] <= pseudo_data[6]^pseudo_data[5];
    //         pseudo_data[6] <= pseudo_data[5]^pseudo_data[4];
    //         pseudo_data[5] <= pseudo_data[4]^pseudo_data[3];
    //         pseudo_data[4] <= pseudo_data[3]^pseudo_data[2];
    //         pseudo_data[3] <= pseudo_data[2]^pseudo_data[1];
    //         pseudo_data[2] <= pseudo_data[1]^pseudo_data[0];
    //         pseudo_data[1] <= pseudo_data[0]^(pseudo_data[6]^pseudo_data[5]);
    //         pseudo_data[0] <= (pseudo_data[6]^pseudo_data[5])^(pseudo_data[5]^pseudo_data[4]);              
    //     end        
    // end

    // reg [7:0] lumi_data;
    // always @(posedge clk640) begin
    //     if(reset) begin
    //         lumi_data <= 8'h01;
    //     end
    //     else begin
    //         lumi_data <= {lumi_data[6:0],lumi_data[7]^lumi_data[6]};           
    //     end        
    // end

    // oserdesData8b T0_inst(
    //     .din(pseudo_data),
    //     .reset(reset),
    //     .enable(1'b1),
    //     .clkPara(clk_p),
    //     .clkSeri(clk_s),
    //     .data_P(TIMING_DOUT_P[0]),
    //     .data_N(TIMING_DOUT_N[0])
    // );
    // oserdesData8b T1_inst(
    //     .din(pseudo_data),
    //     .reset(reset),
    //     .enable(1'b1),
    //     .clkPara(clk_p),
    //     .clkSeri(clk_s),
    //     .data_P(TIMING_DOUT_N[1]),
    //     .data_N(TIMING_DOUT_P[1])
    // );

    // oserdesData8b L0_inst(
    //     .din(lumi_data),
    //     .reset(reset),
    //     .enable(1'b1),
    //     .clkPara(clk80),
    //     .clkSeri(clk320),
    //     .data_P(LUMI_DOUT_N[0]),
    //     .data_N(LUMI_DOUT_P[0])
    // );
    // oserdesData8b L1_inst(
    //     .din(lumi_data),
    //     .reset(reset),
    //     .enable(1'b1),
    //     .clkPara(clk80),
    //     .clkSeri(clk320),
    //     .data_P(LUMI_DOUT_P[1]),
    //     .data_N(LUMI_DOUT_N[1])
    // );



    //PRBS7 generator: X7+X6+1
    wire clk_s; 
    assign clk_s = clk640;
    reg [6:0] pseudo_data;
    always @(posedge clk_s) begin
        if(reset) begin
            pseudo_data <= 7'h01;
        end
        else begin
            pseudo_data <= {pseudo_data[5:0],pseudo_data[6]^pseudo_data[5]};           
        end        
    end

    reg [6:0] lumi_data;
    always @(posedge clk640) begin
        if(reset) begin
            lumi_data <= 7'h01;
        end
        else begin
            lumi_data <= {lumi_data[5:0],lumi_data[6]^lumi_data[5]};           
        end        
    end

    //T0
    OBUFDS #(
            .IOSTANDARD("DIFF_HSUL_12"), 
            .SLEW("FAST") 
        ) T0_inst (
            .O(TIMING_DOUT_P[0]), 
            .OB(TIMING_DOUT_N[0]), 
            .I(pseudo_data[6])
        );    
    OBUFDS #(
            .IOSTANDARD("DIFF_HSUL_12"), 
            .SLEW("FAST") 
        ) T1_inst (
            .O(TIMING_DOUT_N[1]), 
            .OB(TIMING_DOUT_P[1]), 
            .I(pseudo_data[6])
        ); 
    OBUFDS #(
            .IOSTANDARD("DIFF_HSUL_12"), 
            .SLEW("FAST") 
        ) L0_inst (
            .O(LUMI_DOUT_N[0]), 
            .OB(LUMI_DOUT_P[0]), 
            .I(lumi_data[6])
        ); 
    OBUFDS #(
            .IOSTANDARD("DIFF_HSUL_12"), 
            .SLEW("FAST") 
        ) L1_inst (
            .O(LUMI_DOUT_P[1]), 
            .OB(LUMI_DOUT_N[1]), 
            .I(lumi_data[6])
        ); 



    ila_0 ILA_inst (
        .clk(clk320),
        .probe0(FAST_CMD),
        .probe1(shiftreg),
        .probe2(bitErrorCnt),
        .probe3(pseudo_data),
        .probe4(cnt)
    );

endmodule

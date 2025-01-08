`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/01/2023 03:16:05 PM
// Design Name: 
// Module Name: clkMUX
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


module clkMUX(
    input en_TDPU,
    input [1:0] txRate,
    input clk1,  //clk640  clk128
    input clk2,  //clk320  clk64
    input clk3,  //clk160  clk32
    output clk
    );


    wire s1,s2,s3;
    wire O1,O2;

    assign s1 = (en_TDPU==1'b1 && txRate==2'b11);
    assign s2 = (en_TDPU==1'b1 && txRate==2'b10);
    assign s3 = (en_TDPU==1'b1 && txRate==2'b01);    

    // assign O1 = s1? clk1 : 1'b0;
    BUFGMUX #(
    )
    BUFGMUX_inst0 (
        .O(O1),   // 1-bit output: Clock output
        .I0(1'b0), // 1-bit input: Clock input (S=0)
        .I1(clk1), // 1-bit input: Clock input (S=1)
        .S(s1)    // 1-bit input: Clock select
    );

    BUFGMUX #(
    )
    BUFGMUX_inst1 (
        .O(O2),   // 1-bit output: Clock output
        .I0(O1), // 1-bit input: Clock input (S=0)
        .I1(clk2), // 1-bit input: Clock input (S=1)
        .S(s2)    // 1-bit input: Clock select
    );

    BUFGMUX #(
    )
    BUFGMUX_inst2 (
        .O(clk),   // 1-bit output: Clock output
        .I0(O2), // 1-bit input: Clock input (S=0)
        .I1(clk3), // 1-bit input: Clock input (S=1)
        .S(s3)    // 1-bit input: Clock select
    );

endmodule

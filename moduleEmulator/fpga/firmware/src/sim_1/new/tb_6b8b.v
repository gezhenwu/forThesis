`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/03/24 19:23:39
// Design Name: 
// Module Name: tb_6b8b
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


module tb_6b8b;

    parameter period = 25;
    
    reg clk;
    reg rst;
    reg KisChar;
    reg [5:0] din;
    wire [7:0] dout;

    initial begin
        KisChar = 1;
        clk = 0;
        rst = 0;
        #50 rst = 1;
        #50 rst = 0;
        #50 din = 6'b000111;
        #50 din = 6'b111000;
        #50 din = 6'b010101;
        #50 din = 6'b101010;
    end

    always begin
        # (period/2) clk = ~clk;
    end

    // always @(posedge clk) begin
    //     if(rst) din = 6'b0;
    //     else din = din+1;
    // end

    enc_6b8b inst(
        .clk(clk),
        .rst(rst),
        .KisChar(KisChar),
        .din(din),
        .dout(dout)
        );


endmodule

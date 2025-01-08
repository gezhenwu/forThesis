`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: NJU & IHEP
// Engineer: 
// 
// Create Date: 2023/03/24 19:54:51
// Design Name: 
// Module Name: lumiSource
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


module lumiSource(
    input [2:0] W1H,
    input [2:0] W1L,
    input [2:0] W2H,
    input [2:0] W2L,
    input clk40,
    input clk80,
    input rst,
    input enable,
    input bcr,
    output [7:0] dout
    );

    reg [11:0] lumiData;
    always @(posedge clk40) begin
        if(rst || !enable) lumiData <= 12'b0;
        else lumiData <= {W1H,W1L,W2H,W2L};        
    end

    wire [15:0] lumi_to_ser;
    enc_6b8b highBits(
        .KisChar(1'b0),
        .din(lumiData[11:6]),
        .dout(lumi_to_ser[15:8])
    );
    enc_6b8b lowBits(
        .KisChar(1'b0),
        .din(lumiData[5:0]),
        .dout(lumi_to_ser[7:0])
    );

    reg bcr_r;
    reg bcr_rr;
    always @(posedge clk40 or posedge bcr) begin
        if(bcr) begin
            bcr_r <= 1'b1;
        end
        else begin
            bcr_r <= 1'b0;
        end
    end

    always @(posedge clk40) begin
        bcr_rr <= bcr_r;
    end

    reg [15:0] dout_temp;
    always @(posedge clk40 or posedge rst) begin
        if(rst) dout_temp <= 16'h47e8;
        else if(bcr_rr) dout_temp <= 16'h47e8;
        else dout_temp <= lumi_to_ser;
    end

    reg [15:0] dout_temp_r;
    always @(posedge clk40) begin
        dout_temp_r <= dout_temp;        
    end

    reg tick;
    always @(posedge clk80 or posedge rst) begin
        if(rst) tick <= 0;
        else tick <= tick+1;        
    end

    assign dout = tick? dout_temp_r[7:0] : dout_temp_r[15:8];

endmodule

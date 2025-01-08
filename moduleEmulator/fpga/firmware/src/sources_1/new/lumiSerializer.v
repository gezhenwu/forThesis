`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: NJU & IHEP 
// Engineer: 
// 
// Create Date: 2023/03/25 14:46:38
// Design Name: 
// Module Name: lumiSerializer
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
module lumiSerializer(
  // parallel data
  input           clk_par,
  input   [15:0]  parInrWord,
  // serial data
  input           clk_ser,
  input           reset_n,
  output          serOutData
);

// Cache
reg   [15:0]  parInrWord_r = 0;
always @(posedge clk_par) begin
    parInrWord_r <= parInrWord;
end

// Double Data Rate serializer
reg   [2 :0]  shift_count = 0;
always @(posedge clk_ser)
  if (~reset_n) shift_count <= 0;
  else begin
    shift_count <= shift_count+1;
  end

wire load = (shift_count == 0)? 1'b1: 1'b0;

reg   [7 :0]  srPos = 0;
always @(posedge clk_ser)
  if(load) begin
    srPos[7] <=  parInrWord_r[15];
    srPos[6] <=  parInrWord_r[13];
    srPos[5] <=  parInrWord_r[11];  
    srPos[4] <=  parInrWord_r[9];
    srPos[3] <=  parInrWord_r[7];
    srPos[2] <=  parInrWord_r[5];
    srPos[1] <=  parInrWord_r[3];
    srPos[0] <=  parInrWord_r[1];
  end
  else srPos[7:0] <= {srPos[6:0], 1'b0};

reg   [8 :0]  srNeg = 0;
always @(negedge clk_ser)
  if(load) begin
    srNeg[7] <=  parInrWord_r[14];
    srNeg[6] <=  parInrWord_r[12];
    srNeg[5] <=  parInrWord_r[10];  
    srNeg[4] <=  parInrWord_r[8];
    srNeg[3] <=  parInrWord_r[6];
    srNeg[2] <=  parInrWord_r[4];
    srNeg[1] <=  parInrWord_r[2];
    srNeg[0] <=  parInrWord_r[0];
  end
  else srNeg[7:0] <= {srNeg[6:0], 1'b0};

always @(negedge clk_ser) srNeg[8] <= srNeg[7];

assign serOutData = clk_ser ? srNeg[8] : srPos[7];

endmodule
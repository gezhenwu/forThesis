`timescale 1ns/1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: NJU & IHEP        
// Engineer:              
//
// Create Date:     
// Design Name:
// Module Name:     timingSerializer
// Project Name:
// Target Devices:
// Tool versions:
// Description: Convert data into streaming
//    For 1.28Gbps, convert word into streaming
//    For 640Mbps and 320Mbps, convert byte into streaming
// Dependencies:
//
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
//
//////////////////////////////////////////////////////////////////////////////////

module timingSerializer(
  // parallel data
  input           clk_par,
  input   [9:0]  parInrWord,
  // serial data
  input           clk_ser,
  input           reset_n,
  output          serOutData
);

// Cache
reg   [9:0]  parInrWord_r = 0;
always @(posedge clk_par) begin
    parInrWord_r <= parInrWord;
end

// Double Data Rate serializer
reg   [2 :0]  shift_count = 0;
always @(posedge clk_ser)
  if (~reset_n) shift_count <= 0;
  else begin
    if(shift_count==3'h4) shift_count <= 3'h0;
    else shift_count <= shift_count+1;
  end

wire load = (shift_count == 0)? 1'b1: 1'b0;

reg   [4 :0]  srPos = 0;
always @(posedge clk_ser)
  if(load) begin
    srPos[4] <=  parInrWord_r[9];
    srPos[3] <=  parInrWord_r[7];
    srPos[2] <=  parInrWord_r[5];
    srPos[1] <=  parInrWord_r[3];
    srPos[0] <=  parInrWord_r[1];
  end
  else srPos[4:0] <= {srPos[3:0], 1'b0};

reg   [5 :0]  srNeg = 0;
always @(negedge clk_ser)
  if(load) begin
    srNeg[4] <=  parInrWord_r[8];
    srNeg[3] <=  parInrWord_r[6];
    srNeg[2] <=  parInrWord_r[4];
    srNeg[1] <=  parInrWord_r[2];
    srNeg[0] <=  parInrWord_r[0];
  end
  else srNeg[4:0] <= {srNeg[3:0], 1'b0};

always @(negedge clk_ser) srNeg[5] <= srNeg[4];

assign serOutData = clk_ser ? srNeg[5] : srPos[4];

endmodule

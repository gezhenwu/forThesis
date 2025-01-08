`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: NJU & IHEP 
// Engineer: 
// 
// Create Date: 2023/03/24 16:48:00
// Design Name: 
// Module Name: enc_6b8b
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

module enc_6b8b(
    input KisChar,
    input [5:0] din,
    output [7:0] dout
    );

    wire ai,bi,ci,di,ei,fi;
    assign ai=din[0];
    assign bi=din[1];
    assign ci=din[2];
    assign di=din[3];
    assign ei=din[4];
    assign fi=din[5];

    wire [2:0] one;
    assign one = ai+bi+ci+di+ei+fi;
    wire signed [3:0] disParity;
    assign disParity = one+one-6;

    assign dout = KisChar? {2'b01,din} : (disParity==0? {2'b10,din} : (disParity==2 && din!=001111? {2'b00,din} : (disParity==-2 && din!=110000? {2'b11,din} : (disParity==6||disParity==-6? {2'b01,fi,!ei,!di,ci,bi,!ai} : (disParity==62||disParity==-2? {2'b01,fi,ei,di,!ci,bi,ai} : ((disParity==4||disParity==-4)&&(ai^bi==1)? {2'b01,!fi,!ei,di,ci,bi,ai} : ((disParity==4||disParity==-4)&&(ci^di==1)? {2'b01,!fi,ei,di,ci,bi,!ai} : {2'b01,fi,ei,di,ci,!bi,!ai})))))));

endmodule





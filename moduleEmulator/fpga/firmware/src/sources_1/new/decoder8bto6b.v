`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/04/02 20:41:53
// Design Name: 
// Module Name: decoder8bto6b
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


module decoder8bto6b(
    isK,
    encodedData,
    decodedData
    );
input isK;
input [7:0] encodedData;
output [5:0] decodedData;

reg [5:0] decodedDataS;
wire [5:0] decodedDataK;
always @(encodedData)
    case(encodedData)
        8'b01011001: decodedDataS = 6'b000000;// disparity -6 
        8'b01100110: decodedDataS = 6'b111111;// disparity +6
        8'b01001110: decodedDataS = 6'b111110;// disparity +4
        8'b01001101: decodedDataS = 6'b111101;
        8'b01011010: decodedDataS = 6'b111011;
        8'b01010110: decodedDataS = 6'b110111;
        8'b01101100: decodedDataS = 6'b101111;
        8'b01011100: decodedDataS = 6'b011111;
        8'b01110001: decodedDataS = 6'b000001;// disparity -4
        8'b01110010: decodedDataS = 6'b000010;
        8'b01100101: decodedDataS = 6'b000100;
        8'b01101001: decodedDataS = 6'b001000;
        8'b01010011: decodedDataS = 6'b010000;
        8'b01100011: decodedDataS = 6'b100000;
        8'b01001011: decodedDataS = 6'b001111;// disparity +2
        8'b01110100: decodedDataS = 6'b110000;// disparity +2
        default: decodedDataS = encodedData[5:0];// disparity +2, disparity -2, disparity 0       
    endcase
    
 //Control characters
 assign decodedDataK = ((encodedData == 8'b01000111) ? 6'b000111:
                    (encodedData == 8'b01010101) ? 6'b010101:
                    (encodedData == 8'b01111000) ? 6'b111000:
                    (encodedData == 8'b01101010) ? 6'b101010: 8'b0);
                    
assign decodedData = (isK ? decodedDataK : decodedDataS);
endmodule

`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/03/28 21:40:25
// Design Name: 
// Module Name: oserdesData8b
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


module oserdesData8b(
    input   [7:0]   din,
    input           reset,
    input           enable,
    input           clkPara,
    input           clkSeri,
    output          data_P,
    output          data_N
);
 
    wire serial_data;
    OSERDESE2 #(
    .DATA_RATE_OQ		("DDR")		,   		// DDR, SDR
    .DATA_RATE_TQ		("SDR")		,   		// DDR, BUF, SDR
    .DATA_WIDTH		    (8)			,   		// Parallel data width (2-8,10,14)
    .INIT_OQ			(1'b0)		,   		// Initial value of OQ output (1'b0,1'b1)
    .INIT_TQ			(1'b0)		,   		// Initial value of TQ output (1'b0,1'b1)
    .SERDES_MODE		("MASTER")	, 			// MASTER, SLAVE
    .SRVAL_OQ			(1'b0)		,			// OQ output value when SR is used (1'b0,1'b1)
    .SRVAL_TQ			(1'b0)		,			// TQ output value when SR is used (1'b0,1'b1)
    .TBYTE_CTL		    ("FALSE")	,			// Enable tristate byte operation (FALSE, TRUE)
    .TBYTE_SRC		    ("FALSE")	,			// Tristate byte source (FALSE, TRUE)
    .TRISTATE_WIDTH	(1)      				// 3-state converter width (1,4)
    )
    OSERDESE2_inst (
    .OFB				()					,	// 1-bit output: Feedback path for data
    .OQ				    (serial_data)		,	// 1-bit output: Data path output
    .SHIFTOUT1		    ()					,
    .SHIFTOUT2		    ()					,
    .TBYTEOUT			()					,   // 1-bit output: Byte group tristate
    .TFB				()					,	// 1-bit output: 3-state control
    .TQ				    ()					,	// 1-bit output: 3-state control
    .CLK				(clkSeri)			,	// 1-bit input: High speed clock
    .CLKDIV			    (clkPara)			,	// 1-bit input: Divided clock
    .D1				    (din[7])	   	,
    .D2				    (din[6])	   	,
    .D3				    (din[5])	   	,
    .D4				    (din[4])	   	,
    .D5				    (din[3])	   	,
    .D6				    (din[2])	   	,
    .D7				    (din[1])	    ,
    .D8				    (din[0])	    ,
    .OCE				(enable)			,	// 1-bit input: Output data clock enable
    .RST				(reset)			    ,	// 1-bit input: Reset
    .SHIFTIN1			()					,
    .SHIFTIN2			()					,
    .T1				    (1'b0)				,
    .T2				    (1'b0)				,
    .T3				    (1'b0)				,
    .T4				    (1'b0)				,
    .TBYTEIN			(1'b0)				,	// 1-bit input: Byte group tristate
    .TCE				(1'b0)              	// 1-bit input: 3-state clock enable
    );

  OBUFDS #(
          .IOSTANDARD("DIFF_HSUL_12"), 
          .SLEW("FAST") 
      ) OBUFDS_inst (
          .O(data_P), 
          .OB(data_N), 
          .I(serial_data)
      );    
endmodule
//////////////////////////////////////////////////////////////////////
////                                                              ////
//// Copyright (C) 2009 Authors and OPENCORES.ORG                 ////
////                                                              ////
//// This source file may be used and distributed without         ////
//// restriction provided that this copyright statement is not    ////
//// removed from the file and that any derivative work contains  ////
//// the original copyright notice and the associated disclaimer. ////
////                                                              ////
//// This source file is free software; you can redistribute it   ////
//// and/or modify it under the terms of the GNU Lesser General   ////
//// Public License as published by the Free Software Foundation; ////
//// either version 2.1 of the License, or (at your option) any   ////
//// later version.                                               ////
////                                                              ////
//// This source is distributed in the hope that it will be       ////
//// useful, but WITHOUT ANY WARRANTY; without even the implied   ////
//// warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR      ////
//// PURPOSE.  See the GNU Lesser General Public License for more ////
//// details.                                                     ////
////                                                              ////
//// You should have received a copy of the GNU Lesser General    ////
//// Public License along with this source; if not, download it   ////
//// from http://www.opencores.org/lgpl.shtml                     ////
////                                                              ////
//////////////////////////////////////////////////////////////////////
`timescale 1ns / 1ps

module glitch_filter #(
  parameter CLK_FREQ = 160 // System clock frequency in MHz (>=20)
)(
  input in,
  output reg out,
    
  output rise,
  output fall,
    
  input clk
);

// --------------------------------------------------------------------
//  in sync flop
reg in_reg;
always @(posedge clk)
  in_reg <= in;

// --------------------------------------------------------------------
// Glitch filter
// Debounce SCL and SDA over this many clock ticks.
// The rise time of SCL and SDA can be up to 300 ns (in Fast-mode, 400KHz)
// so it is essential to debounce the inputs.
// The spec requires 0.05V of hysteresis, but in practice simply debouncing
// the inputs is sufficient. I2C spec requires suppression of spikes of
// maximum duration 50 ns, so this debounce time should be greater than 50 ns.
// Also increases data hold time and decreases data setup time during an I2C read operation
localparam DEB_I2C_LEN = (CLK_FREQ*2)/20;

reg [(DEB_I2C_LEN-1):0] buffer;
always @(posedge clk)
  buffer <= { buffer[(DEB_I2C_LEN-2):0], in_reg };
    
wire all_hi = &buffer;
wire all_lo = ~|buffer;
wire out_en = all_hi|all_lo;
  
always @(posedge clk)
  if(out_en) out <= buffer[(DEB_I2C_LEN-1)];

// --------------------------------------------------------------------
//  outputs
assign fall = all_lo & out;
assign rise = all_hi & ~out;
  
endmodule


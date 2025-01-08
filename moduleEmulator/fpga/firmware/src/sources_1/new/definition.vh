`define TS              12
`define TRID            5
`define FIFODEPTH       106
`define FIFODATALENGHT  `TS + 16
`define FIFOMATCHDEPTH  32
`define FIFOMATCHLEN    16 + `TRID
`define L0A             8'b11010000
`define L1A             8'b11001000
`define BCRST           8'b11000100
`define GBRST           8'b11000010
`define NOCMD           8'b00000000
`define TX320MHz        2'b01
`define TX640MHz        2'b10
`define TX1280MHz       2'b11
`define TYPE_DATA       2'b00
`define TYPE_10bTOT     2'b01
`define TYPE_PATTERN    2'b10
`define TYPE_LINKID     2'b11
`define LUMADDR         10'd900
`define DATADDR         10'd908
`define ANATESTADDR     10'd910
`define CLOCKGENADDR    10'd912
`define PIXTDCADDR      10'd928
`define ANAPERI         10'd940
`define GLOBALCNTRL     10'd950
`define LATENCY0        3'h1
`define LATENCY1        8'h90
`define BUFFDEPTH       12'd1408
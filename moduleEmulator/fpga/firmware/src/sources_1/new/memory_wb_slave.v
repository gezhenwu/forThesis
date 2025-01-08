module memory_wb_slave 
    #(parameter date = 8'h00)
    (
    output wire [7:0] confpix0reg0,
    output wire [7:0] confpix0reg1,
    output wire [7:0] confpix0reg2,
    output wire [7:0] confpix0reg3,
    output wire [7:0] confpix1reg0,
    output wire [7:0] confpix1reg1,
    output wire [7:0] confpix1reg2,
    output wire [7:0] confpix1reg3,
    output wire [7:0] confpix2reg0,
    output wire [7:0] confpix2reg1,
    output wire [7:0] confpix2reg2,
    output wire [7:0] confpix2reg3,
    output wire [7:0] confpix3reg0,
    output wire [7:0] confpix3reg1,
    output wire [7:0] confpix3reg2,
    output wire [7:0] confpix3reg3,
    output wire [7:0] confpix4reg0,
    output wire [7:0] confpix4reg1,
    output wire [7:0] confpix4reg2,
    output wire [7:0] confpix4reg3,
    output wire [7:0] confpix5reg0,
    output wire [7:0] confpix5reg1,
    output wire [7:0] confpix5reg2,
    output wire [7:0] confpix5reg3,
    output wire [7:0] confpix6reg0,
    output wire [7:0] confpix6reg1,
    output wire [7:0] confpix6reg2,
    output wire [7:0] confpix6reg3,
    output wire [7:0] confpix7reg0,
    output wire [7:0] confpix7reg1,
    output wire [7:0] confpix7reg2,
    output wire [7:0] confpix7reg3,
    output wire [7:0] confpix8reg0,
    output wire [7:0] confpix8reg1,
    output wire [7:0] confpix8reg2,
    output wire [7:0] confpix8reg3,
    output wire [7:0] confpix9reg0,
    output wire [7:0] confpix9reg1,
    output wire [7:0] confpix9reg2,
    output wire [7:0] confpix9reg3,
    output wire [7:0] confpix10reg0,
    output wire [7:0] confpix10reg1,
    output wire [7:0] confpix10reg2,
    output wire [7:0] confpix10reg3,
    output wire [7:0] confpix11reg0,
    output wire [7:0] confpix11reg1,
    output wire [7:0] confpix11reg2,
    output wire [7:0] confpix11reg3,
    output wire [7:0] confpix12reg0,
    output wire [7:0] confpix12reg1,
    output wire [7:0] confpix12reg2,
    output wire [7:0] confpix12reg3,
    output wire [7:0] confpix13reg0,
    output wire [7:0] confpix13reg1,
    output wire [7:0] confpix13reg2,
    output wire [7:0] confpix13reg3,
    output wire [7:0] confpix14reg0,
    output wire [7:0] confpix14reg1,
    output wire [7:0] confpix14reg2,
    output wire [7:0] confpix14reg3,
    output wire [7:0] confpix15reg0,
    output wire [7:0] confpix15reg1,
    output wire [7:0] confpix15reg2,
    output wire [7:0] confpix15reg3,
    output wire [7:0] confpix30reg0,
    output wire [7:0] confpix30reg1,
    output wire [7:0] confpix30reg2,
    output wire [7:0] confpix30reg3,
    output wire [7:0] confpix45reg0,
    output wire [7:0] confpix45reg1,
    output wire [7:0] confpix45reg2,
    output wire [7:0] confpix45reg3,
    output wire [7:0] confpix60reg0,
    output wire [7:0] confpix60reg1,
    output wire [7:0] confpix60reg2,
    output wire [7:0] confpix60reg3,
    output wire [7:0] confpix75reg0,
    output wire [7:0] confpix75reg1,
    output wire [7:0] confpix75reg2,
    output wire [7:0] confpix75reg3,
    output wire [7:0] confpix90reg0,
    output wire [7:0] confpix90reg1,
    output wire [7:0] confpix90reg2,
    output wire [7:0] confpix90reg3,
    output wire [7:0] confpix105reg0,
    output wire [7:0] confpix105reg1,
    output wire [7:0] confpix105reg2,
    output wire [7:0] confpix105reg3,
    output wire [7:0] confpix120reg0,
    output wire [7:0] confpix120reg1,
    output wire [7:0] confpix120reg2,
    output wire [7:0] confpix120reg3,
    output wire [7:0] confpix135reg0,
    output wire [7:0] confpix135reg1,
    output wire [7:0] confpix135reg2,
    output wire [7:0] confpix135reg3,
    output wire [7:0] confpix150reg0,
    output wire [7:0] confpix150reg1,
    output wire [7:0] confpix150reg2,
    output wire [7:0] confpix150reg3,
    output wire [7:0] confpix165reg0,
    output wire [7:0] confpix165reg1,
    output wire [7:0] confpix165reg2,
    output wire [7:0] confpix165reg3,
    output wire [7:0] confpix180reg0,
    output wire [7:0] confpix180reg1,
    output wire [7:0] confpix180reg2,
    output wire [7:0] confpix180reg3,
    output wire [7:0] confpix195reg0,
    output wire [7:0] confpix195reg1,
    output wire [7:0] confpix195reg2,
    output wire [7:0] confpix195reg3,
    output wire [7:0] confpix210reg0,
    output wire [7:0] confpix210reg1,
    output wire [7:0] confpix210reg2,
    output wire [7:0] confpix210reg3,
    output wire [7:0] confldpuiniwin1l,
    output wire [7:0] confldpuiniwin1h,
    output wire [7:0] confldpuiniwin2l,
    output wire [7:0] confldpuiniwin2h,
    output wire [7:0] conf_ldpu_cntrl,
    output wire [7:0] conftdpulatencyl,
    output wire [7:0] conftdpulatencyh,
    output wire [7:0] conf_tdpu_cntrl,
    output wire [7:0] conf_tdpu_pattern,
    output wire [7:0] conf_tdpu_ocupref,
    output wire [7:0] dacrpgconf2,
    output wire [7:0] dacrpgconf1,
    output wire [7:0] bias_ch_sel_pulser,
    output wire [7:0] bias_ch_dac_pa,
    output wire [7:0] bias_ch_dac_dc_pa,
    output wire [7:0] dac10bconf1,
    output wire [7:0] dac10bconf2,
    output wire [7:0] pixeladdr,
    output wire [7:0] dll_120p_toa_cbit,
    output wire [7:0] dll_120p_toa_cp,
    output wire [7:0] dll_120p_toa_comp,
    output wire [7:0] dll_120p_tot_cbit,
    output wire [7:0] dll_120p_tot_cp,
    output wire [7:0] dll_120p_tot_comp,
    output wire [7:0] dll_140p_toa_cbit,
    output wire [7:0] dll_140p_toa_cp,
    output wire [7:0] dll_140p_toa_comp,
    output wire [7:0] dllcntrconf,
    output wire [7:0] selprobebiasconf,
    output wire [7:0] confglobalenprobe,
    output wire [7:0] confglobalsignaltdcs,
    output wire [7:0] confglobalsignalrincdcp,
    output wire [7:0] conf_global_cntr,
    output wire [7:0] conf_global_occupancy,
    output wire [7:0] enablecgeocl,
    output wire [7:0] enablecgeoch,
    output wire [7:0] conf_anaperi_selprobemon,
    output wire [7:0] bgconf,
    output wire [7:0] pllcpconf,
    output wire [7:0] pllbwconf,
    output wire [7:0] pllcntr1,
    output wire [7:0] pllcntr2,
    output wire [7:0] conf_anaperi_plllocksamples,
    output wire [7:0] conf_anaperi,
    output wire [7:0] psdelay1,
    output wire [7:0] psdelay2,
    output wire [7:0] psdelaylum,
    output wire [7:0] pscntr1,
    output wire [7:0] pscntr2,
    output wire [7:0] entestpadsconf1,
    output wire [7:0] entestpadsconf2,
    output wire [7:0] global_extclock,
    output wire [7:0] clktestpadsconf,
    output wire [7:0] probedigtestpadsconf,
    output wire [7:0] conf_fccu_trigid_l,
    output wire [7:0] conf_fccu_trigid_h,
    output wire [7:0] fccucntrconf,
    output wire [7:0] cmdcalgenconf1,
    output wire [7:0] cmdcalgenconf2,
    output wire [7:0] cmdcalgenconf3,

    output wire [7:0] logRegister,

    input wire clk_wb,
    input wire wb_rst,
    input wire wb_stb_i,
    output wire wb_ack_o,
    input wire wb_wen_i,
    input wire [7:0] wb_dat_i,
    output wire [7:0] wb_dat_o,
    input wire [9:0] wb_adr_i
);
    // tmrg default triplicate

    wire [7:0] dat_iVoted = wb_dat_i;
    wire wb_stb_iVoted = wb_stb_i;
    wire wb_wen_iVoted = wb_wen_i;
    wire wb_we = wb_stb_iVoted && wb_wen_iVoted;

    // Register: confPix0Reg0 address:0
    wire reg0_select = wb_adr_i == 10'h0;
    reg [7:0] reg0_q;
    wire [7:0] reg0_qVoted = reg0_q;
    wire [7:0] reg0_d = wb_we && reg0_select ? dat_iVoted : reg0_qVoted;
    assign confpix0reg0 = reg0_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg0_q <= 8'h00;
        else
            reg0_q <= reg0_d;

`ifdef SIM
    initial
        reg0_q = $urandom;
`endif



    // Register: confPix0Reg1 address:1
    wire reg1_select = wb_adr_i == 10'h1;
    reg [7:0] reg1_q;
    wire [7:0] reg1_qVoted = reg1_q;
    wire [7:0] reg1_d = wb_we && reg1_select ? dat_iVoted : reg1_qVoted;
    assign confpix0reg1 = reg1_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1_q <= 8'hf0;
        else
            reg1_q <= reg1_d;

`ifdef SIM
    initial
        reg1_q = $urandom;
`endif



    // Register: confPix0Reg2 address:2
    wire reg2_select = wb_adr_i == 10'h2;
    reg [7:0] reg2_q;
    wire [7:0] reg2_qVoted = reg2_q;
    wire [7:0] reg2_d = wb_we && reg2_select ? dat_iVoted : reg2_qVoted;
    assign confpix0reg2 = reg2_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg2_q <= 8'h1c;
        else
            reg2_q <= reg2_d;

`ifdef SIM
    initial
        reg2_q = $urandom;
`endif



    // Register: confPix0Reg3 address:3
    wire reg3_select = wb_adr_i == 10'h3;
    reg [7:0] reg3_q;
    wire [7:0] reg3_qVoted = reg3_q;
    wire [7:0] reg3_d = wb_we && reg3_select ? dat_iVoted : reg3_qVoted;
    assign confpix0reg3 = reg3_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg3_q <= 8'h40;
        else
            reg3_q <= reg3_d;

`ifdef SIM
    initial
        reg3_q = $urandom;
`endif



    // Register: confPix1Reg0 address:4
    wire reg4_select = wb_adr_i == 10'h4;
    reg [7:0] reg4_q;
    wire [7:0] reg4_qVoted = reg4_q;
    wire [7:0] reg4_d = wb_we && reg4_select ? dat_iVoted : reg4_qVoted;
    assign confpix1reg0 = reg4_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg4_q <= 8'h00;
        else
            reg4_q <= reg4_d;

`ifdef SIM
    initial
        reg4_q = $urandom;
`endif



    // Register: confPix1Reg1 address:5
    wire reg5_select = wb_adr_i == 10'h5;
    reg [7:0] reg5_q;
    wire [7:0] reg5_qVoted = reg5_q;
    wire [7:0] reg5_d = wb_we && reg5_select ? dat_iVoted : reg5_qVoted;
    assign confpix1reg1 = reg5_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg5_q <= 8'hf0;
        else
            reg5_q <= reg5_d;

`ifdef SIM
    initial
        reg5_q = $urandom;
`endif



    // Register: confPix1Reg2 address:6
    wire reg6_select = wb_adr_i == 10'h6;
    reg [7:0] reg6_q;
    wire [7:0] reg6_qVoted = reg6_q;
    wire [7:0] reg6_d = wb_we && reg6_select ? dat_iVoted : reg6_qVoted;
    assign confpix1reg2 = reg6_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg6_q <= 8'h1c;
        else
            reg6_q <= reg6_d;

`ifdef SIM
    initial
        reg6_q = $urandom;
`endif



    // Register: confPix1Reg3 address:7
    wire reg7_select = wb_adr_i == 10'h7;
    reg [7:0] reg7_q;
    wire [7:0] reg7_qVoted = reg7_q;
    wire [7:0] reg7_d = wb_we && reg7_select ? dat_iVoted : reg7_qVoted;
    assign confpix1reg3 = reg7_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg7_q <= 8'h40;
        else
            reg7_q <= reg7_d;

`ifdef SIM
    initial
        reg7_q = $urandom;
`endif



    // Register: confPix2Reg0 address:8
    wire reg8_select = wb_adr_i == 10'h8;
    reg [7:0] reg8_q;
    wire [7:0] reg8_qVoted = reg8_q;
    wire [7:0] reg8_d = wb_we && reg8_select ? dat_iVoted : reg8_qVoted;
    assign confpix2reg0 = reg8_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg8_q <= 8'h00;
        else
            reg8_q <= reg8_d;

`ifdef SIM
    initial
        reg8_q = $urandom;
`endif



    // Register: confPix2Reg1 address:9
    wire reg9_select = wb_adr_i == 10'h9;
    reg [7:0] reg9_q;
    wire [7:0] reg9_qVoted = reg9_q;
    wire [7:0] reg9_d = wb_we && reg9_select ? dat_iVoted : reg9_qVoted;
    assign confpix2reg1 = reg9_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg9_q <= 8'hf0;
        else
            reg9_q <= reg9_d;

`ifdef SIM
    initial
        reg9_q = $urandom;
`endif



    // Register: confPix2Reg2 address:10
    wire reg10_select = wb_adr_i == 10'ha;
    reg [7:0] reg10_q;
    wire [7:0] reg10_qVoted = reg10_q;
    wire [7:0] reg10_d = wb_we && reg10_select ? dat_iVoted : reg10_qVoted;
    assign confpix2reg2 = reg10_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg10_q <= 8'h1c;
        else
            reg10_q <= reg10_d;

`ifdef SIM
    initial
        reg10_q = $urandom;
`endif



    // Register: confPix2Reg3 address:11
    wire reg11_select = wb_adr_i == 10'hb;
    reg [7:0] reg11_q;
    wire [7:0] reg11_qVoted = reg11_q;
    wire [7:0] reg11_d = wb_we && reg11_select ? dat_iVoted : reg11_qVoted;
    assign confpix2reg3 = reg11_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg11_q <= 8'h40;
        else
            reg11_q <= reg11_d;

`ifdef SIM
    initial
        reg11_q = $urandom;
`endif



    // Register: confPix3Reg0 address:12
    wire reg12_select = wb_adr_i == 10'hc;
    reg [7:0] reg12_q;
    wire [7:0] reg12_qVoted = reg12_q;
    wire [7:0] reg12_d = wb_we && reg12_select ? dat_iVoted : reg12_qVoted;
    assign confpix3reg0 = reg12_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg12_q <= 8'h00;
        else
            reg12_q <= reg12_d;

`ifdef SIM
    initial
        reg12_q = $urandom;
`endif



    // Register: confPix3Reg1 address:13
    wire reg13_select = wb_adr_i == 10'hd;
    reg [7:0] reg13_q;
    wire [7:0] reg13_qVoted = reg13_q;
    wire [7:0] reg13_d = wb_we && reg13_select ? dat_iVoted : reg13_qVoted;
    assign confpix3reg1 = reg13_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg13_q <= 8'hf0;
        else
            reg13_q <= reg13_d;

`ifdef SIM
    initial
        reg13_q = $urandom;
`endif



    // Register: confPix3Reg2 address:14
    wire reg14_select = wb_adr_i == 10'he;
    reg [7:0] reg14_q;
    wire [7:0] reg14_qVoted = reg14_q;
    wire [7:0] reg14_d = wb_we && reg14_select ? dat_iVoted : reg14_qVoted;
    assign confpix3reg2 = reg14_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg14_q <= 8'h1c;
        else
            reg14_q <= reg14_d;

`ifdef SIM
    initial
        reg14_q = $urandom;
`endif



    // Register: confPix3Reg3 address:15
    wire reg15_select = wb_adr_i == 10'hf;
    reg [7:0] reg15_q;
    wire [7:0] reg15_qVoted = reg15_q;
    wire [7:0] reg15_d = wb_we && reg15_select ? dat_iVoted : reg15_qVoted;
    assign confpix3reg3 = reg15_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg15_q <= 8'h40;
        else
            reg15_q <= reg15_d;

`ifdef SIM
    initial
        reg15_q = $urandom;
`endif



    // Register: confPix4Reg0 address:16
    wire reg16_select = wb_adr_i == 10'h10;
    reg [7:0] reg16_q;
    wire [7:0] reg16_qVoted = reg16_q;
    wire [7:0] reg16_d = wb_we && reg16_select ? dat_iVoted : reg16_qVoted;
    assign confpix4reg0 = reg16_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg16_q <= 8'h00;
        else
            reg16_q <= reg16_d;

`ifdef SIM
    initial
        reg16_q = $urandom;
`endif



    // Register: confPix4Reg1 address:17
    wire reg17_select = wb_adr_i == 10'h11;
    reg [7:0] reg17_q;
    wire [7:0] reg17_qVoted = reg17_q;
    wire [7:0] reg17_d = wb_we && reg17_select ? dat_iVoted : reg17_qVoted;
    assign confpix4reg1 = reg17_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg17_q <= 8'hf0;
        else
            reg17_q <= reg17_d;

`ifdef SIM
    initial
        reg17_q = $urandom;
`endif



    // Register: confPix4Reg2 address:18
    wire reg18_select = wb_adr_i == 10'h12;
    reg [7:0] reg18_q;
    wire [7:0] reg18_qVoted = reg18_q;
    wire [7:0] reg18_d = wb_we && reg18_select ? dat_iVoted : reg18_qVoted;
    assign confpix4reg2 = reg18_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg18_q <= 8'h1c;
        else
            reg18_q <= reg18_d;

`ifdef SIM
    initial
        reg18_q = $urandom;
`endif



    // Register: confPix4Reg3 address:19
    wire reg19_select = wb_adr_i == 10'h13;
    reg [7:0] reg19_q;
    wire [7:0] reg19_qVoted = reg19_q;
    wire [7:0] reg19_d = wb_we && reg19_select ? dat_iVoted : reg19_qVoted;
    assign confpix4reg3 = reg19_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg19_q <= 8'h40;
        else
            reg19_q <= reg19_d;

`ifdef SIM
    initial
        reg19_q = $urandom;
`endif



    // Register: confPix5Reg0 address:20
    wire reg20_select = wb_adr_i == 10'h14;
    reg [7:0] reg20_q;
    wire [7:0] reg20_qVoted = reg20_q;
    wire [7:0] reg20_d = wb_we && reg20_select ? dat_iVoted : reg20_qVoted;
    assign confpix5reg0 = reg20_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg20_q <= 8'h00;
        else
            reg20_q <= reg20_d;

`ifdef SIM
    initial
        reg20_q = $urandom;
`endif



    // Register: confPix5Reg1 address:21
    wire reg21_select = wb_adr_i == 10'h15;
    reg [7:0] reg21_q;
    wire [7:0] reg21_qVoted = reg21_q;
    wire [7:0] reg21_d = wb_we && reg21_select ? dat_iVoted : reg21_qVoted;
    assign confpix5reg1 = reg21_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg21_q <= 8'hf0;
        else
            reg21_q <= reg21_d;

`ifdef SIM
    initial
        reg21_q = $urandom;
`endif



    // Register: confPix5Reg2 address:22
    wire reg22_select = wb_adr_i == 10'h16;
    reg [7:0] reg22_q;
    wire [7:0] reg22_qVoted = reg22_q;
    wire [7:0] reg22_d = wb_we && reg22_select ? dat_iVoted : reg22_qVoted;
    assign confpix5reg2 = reg22_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg22_q <= 8'h1c;
        else
            reg22_q <= reg22_d;

`ifdef SIM
    initial
        reg22_q = $urandom;
`endif



    // Register: confPix5Reg3 address:23
    wire reg23_select = wb_adr_i == 10'h17;
    reg [7:0] reg23_q;
    wire [7:0] reg23_qVoted = reg23_q;
    wire [7:0] reg23_d = wb_we && reg23_select ? dat_iVoted : reg23_qVoted;
    assign confpix5reg3 = reg23_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg23_q <= 8'h40;
        else
            reg23_q <= reg23_d;

`ifdef SIM
    initial
        reg23_q = $urandom;
`endif



    // Register: confPix6Reg0 address:24
    wire reg24_select = wb_adr_i == 10'h18;
    reg [7:0] reg24_q;
    wire [7:0] reg24_qVoted = reg24_q;
    wire [7:0] reg24_d = wb_we && reg24_select ? dat_iVoted : reg24_qVoted;
    assign confpix6reg0 = reg24_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg24_q <= 8'h00;
        else
            reg24_q <= reg24_d;

`ifdef SIM
    initial
        reg24_q = $urandom;
`endif



    // Register: confPix6Reg1 address:25
    wire reg25_select = wb_adr_i == 10'h19;
    reg [7:0] reg25_q;
    wire [7:0] reg25_qVoted = reg25_q;
    wire [7:0] reg25_d = wb_we && reg25_select ? dat_iVoted : reg25_qVoted;
    assign confpix6reg1 = reg25_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg25_q <= 8'hf0;
        else
            reg25_q <= reg25_d;

`ifdef SIM
    initial
        reg25_q = $urandom;
`endif



    // Register: confPix6Reg2 address:26
    wire reg26_select = wb_adr_i == 10'h1a;
    reg [7:0] reg26_q;
    wire [7:0] reg26_qVoted = reg26_q;
    wire [7:0] reg26_d = wb_we && reg26_select ? dat_iVoted : reg26_qVoted;
    assign confpix6reg2 = reg26_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg26_q <= 8'h1c;
        else
            reg26_q <= reg26_d;

`ifdef SIM
    initial
        reg26_q = $urandom;
`endif



    // Register: confPix6Reg3 address:27
    wire reg27_select = wb_adr_i == 10'h1b;
    reg [7:0] reg27_q;
    wire [7:0] reg27_qVoted = reg27_q;
    wire [7:0] reg27_d = wb_we && reg27_select ? dat_iVoted : reg27_qVoted;
    assign confpix6reg3 = reg27_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg27_q <= 8'h40;
        else
            reg27_q <= reg27_d;

`ifdef SIM
    initial
        reg27_q = $urandom;
`endif



    // Register: confPix7Reg0 address:28
    wire reg28_select = wb_adr_i == 10'h1c;
    reg [7:0] reg28_q;
    wire [7:0] reg28_qVoted = reg28_q;
    wire [7:0] reg28_d = wb_we && reg28_select ? dat_iVoted : reg28_qVoted;
    assign confpix7reg0 = reg28_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg28_q <= 8'h00;
        else
            reg28_q <= reg28_d;

`ifdef SIM
    initial
        reg28_q = $urandom;
`endif



    // Register: confPix7Reg1 address:29
    wire reg29_select = wb_adr_i == 10'h1d;
    reg [7:0] reg29_q;
    wire [7:0] reg29_qVoted = reg29_q;
    wire [7:0] reg29_d = wb_we && reg29_select ? dat_iVoted : reg29_qVoted;
    assign confpix7reg1 = reg29_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg29_q <= 8'hf0;
        else
            reg29_q <= reg29_d;

`ifdef SIM
    initial
        reg29_q = $urandom;
`endif



    // Register: confPix7Reg2 address:30
    wire reg30_select = wb_adr_i == 10'h1e;
    reg [7:0] reg30_q;
    wire [7:0] reg30_qVoted = reg30_q;
    wire [7:0] reg30_d = wb_we && reg30_select ? dat_iVoted : reg30_qVoted;
    assign confpix7reg2 = reg30_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg30_q <= 8'h1c;
        else
            reg30_q <= reg30_d;

`ifdef SIM
    initial
        reg30_q = $urandom;
`endif



    // Register: confPix7Reg3 address:31
    wire reg31_select = wb_adr_i == 10'h1f;
    reg [7:0] reg31_q;
    wire [7:0] reg31_qVoted = reg31_q;
    wire [7:0] reg31_d = wb_we && reg31_select ? dat_iVoted : reg31_qVoted;
    assign confpix7reg3 = reg31_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg31_q <= 8'h40;
        else
            reg31_q <= reg31_d;

`ifdef SIM
    initial
        reg31_q = $urandom;
`endif



    // Register: confPix8Reg0 address:32
    wire reg32_select = wb_adr_i == 10'h20;
    reg [7:0] reg32_q;
    wire [7:0] reg32_qVoted = reg32_q;
    wire [7:0] reg32_d = wb_we && reg32_select ? dat_iVoted : reg32_qVoted;
    assign confpix8reg0 = reg32_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg32_q <= 8'h00;
        else
            reg32_q <= reg32_d;

`ifdef SIM
    initial
        reg32_q = $urandom;
`endif



    // Register: confPix8Reg1 address:33
    wire reg33_select = wb_adr_i == 10'h21;
    reg [7:0] reg33_q;
    wire [7:0] reg33_qVoted = reg33_q;
    wire [7:0] reg33_d = wb_we && reg33_select ? dat_iVoted : reg33_qVoted;
    assign confpix8reg1 = reg33_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg33_q <= 8'hf0;
        else
            reg33_q <= reg33_d;

`ifdef SIM
    initial
        reg33_q = $urandom;
`endif



    // Register: confPix8Reg2 address:34
    wire reg34_select = wb_adr_i == 10'h22;
    reg [7:0] reg34_q;
    wire [7:0] reg34_qVoted = reg34_q;
    wire [7:0] reg34_d = wb_we && reg34_select ? dat_iVoted : reg34_qVoted;
    assign confpix8reg2 = reg34_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg34_q <= 8'h1c;
        else
            reg34_q <= reg34_d;

`ifdef SIM
    initial
        reg34_q = $urandom;
`endif



    // Register: confPix8Reg3 address:35
    wire reg35_select = wb_adr_i == 10'h23;
    reg [7:0] reg35_q;
    wire [7:0] reg35_qVoted = reg35_q;
    wire [7:0] reg35_d = wb_we && reg35_select ? dat_iVoted : reg35_qVoted;
    assign confpix8reg3 = reg35_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg35_q <= 8'h40;
        else
            reg35_q <= reg35_d;

`ifdef SIM
    initial
        reg35_q = $urandom;
`endif



    // Register: confPix9Reg0 address:36
    wire reg36_select = wb_adr_i == 10'h24;
    reg [7:0] reg36_q;
    wire [7:0] reg36_qVoted = reg36_q;
    wire [7:0] reg36_d = wb_we && reg36_select ? dat_iVoted : reg36_qVoted;
    assign confpix9reg0 = reg36_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg36_q <= 8'h00;
        else
            reg36_q <= reg36_d;

`ifdef SIM
    initial
        reg36_q = $urandom;
`endif



    // Register: confPix9Reg1 address:37
    wire reg37_select = wb_adr_i == 10'h25;
    reg [7:0] reg37_q;
    wire [7:0] reg37_qVoted = reg37_q;
    wire [7:0] reg37_d = wb_we && reg37_select ? dat_iVoted : reg37_qVoted;
    assign confpix9reg1 = reg37_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg37_q <= 8'hf0;
        else
            reg37_q <= reg37_d;

`ifdef SIM
    initial
        reg37_q = $urandom;
`endif



    // Register: confPix9Reg2 address:38
    wire reg38_select = wb_adr_i == 10'h26;
    reg [7:0] reg38_q;
    wire [7:0] reg38_qVoted = reg38_q;
    wire [7:0] reg38_d = wb_we && reg38_select ? dat_iVoted : reg38_qVoted;
    assign confpix9reg2 = reg38_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg38_q <= 8'h1c;
        else
            reg38_q <= reg38_d;

`ifdef SIM
    initial
        reg38_q = $urandom;
`endif



    // Register: confPix9Reg3 address:39
    wire reg39_select = wb_adr_i == 10'h27;
    reg [7:0] reg39_q;
    wire [7:0] reg39_qVoted = reg39_q;
    wire [7:0] reg39_d = wb_we && reg39_select ? dat_iVoted : reg39_qVoted;
    assign confpix9reg3 = reg39_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg39_q <= 8'h40;
        else
            reg39_q <= reg39_d;

`ifdef SIM
    initial
        reg39_q = $urandom;
`endif



    // Register: confPix10Reg0 address:40
    wire reg40_select = wb_adr_i == 10'h28;
    reg [7:0] reg40_q;
    wire [7:0] reg40_qVoted = reg40_q;
    wire [7:0] reg40_d = wb_we && reg40_select ? dat_iVoted : reg40_qVoted;
    assign confpix10reg0 = reg40_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg40_q <= 8'h00;
        else
            reg40_q <= reg40_d;

`ifdef SIM
    initial
        reg40_q = $urandom;
`endif



    // Register: confPix10Reg1 address:41
    wire reg41_select = wb_adr_i == 10'h29;
    reg [7:0] reg41_q;
    wire [7:0] reg41_qVoted = reg41_q;
    wire [7:0] reg41_d = wb_we && reg41_select ? dat_iVoted : reg41_qVoted;
    assign confpix10reg1 = reg41_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg41_q <= 8'hf0;
        else
            reg41_q <= reg41_d;

`ifdef SIM
    initial
        reg41_q = $urandom;
`endif



    // Register: confPix10Reg2 address:42
    wire reg42_select = wb_adr_i == 10'h2a;
    reg [7:0] reg42_q;
    wire [7:0] reg42_qVoted = reg42_q;
    wire [7:0] reg42_d = wb_we && reg42_select ? dat_iVoted : reg42_qVoted;
    assign confpix10reg2 = reg42_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg42_q <= 8'h1c;
        else
            reg42_q <= reg42_d;

`ifdef SIM
    initial
        reg42_q = $urandom;
`endif



    // Register: confPix10Reg3 address:43
    wire reg43_select = wb_adr_i == 10'h2b;
    reg [7:0] reg43_q;
    wire [7:0] reg43_qVoted = reg43_q;
    wire [7:0] reg43_d = wb_we && reg43_select ? dat_iVoted : reg43_qVoted;
    assign confpix10reg3 = reg43_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg43_q <= 8'h40;
        else
            reg43_q <= reg43_d;

`ifdef SIM
    initial
        reg43_q = $urandom;
`endif



    // Register: confPix11Reg0 address:44
    wire reg44_select = wb_adr_i == 10'h2c;
    reg [7:0] reg44_q;
    wire [7:0] reg44_qVoted = reg44_q;
    wire [7:0] reg44_d = wb_we && reg44_select ? dat_iVoted : reg44_qVoted;
    assign confpix11reg0 = reg44_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg44_q <= 8'h00;
        else
            reg44_q <= reg44_d;

`ifdef SIM
    initial
        reg44_q = $urandom;
`endif



    // Register: confPix11Reg1 address:45
    wire reg45_select = wb_adr_i == 10'h2d;
    reg [7:0] reg45_q;
    wire [7:0] reg45_qVoted = reg45_q;
    wire [7:0] reg45_d = wb_we && reg45_select ? dat_iVoted : reg45_qVoted;
    assign confpix11reg1 = reg45_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg45_q <= 8'hf0;
        else
            reg45_q <= reg45_d;

`ifdef SIM
    initial
        reg45_q = $urandom;
`endif



    // Register: confPix11Reg2 address:46
    wire reg46_select = wb_adr_i == 10'h2e;
    reg [7:0] reg46_q;
    wire [7:0] reg46_qVoted = reg46_q;
    wire [7:0] reg46_d = wb_we && reg46_select ? dat_iVoted : reg46_qVoted;
    assign confpix11reg2 = reg46_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg46_q <= 8'h1c;
        else
            reg46_q <= reg46_d;

`ifdef SIM
    initial
        reg46_q = $urandom;
`endif



    // Register: confPix11Reg3 address:47
    wire reg47_select = wb_adr_i == 10'h2f;
    reg [7:0] reg47_q;
    wire [7:0] reg47_qVoted = reg47_q;
    wire [7:0] reg47_d = wb_we && reg47_select ? dat_iVoted : reg47_qVoted;
    assign confpix11reg3 = reg47_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg47_q <= 8'h40;
        else
            reg47_q <= reg47_d;

`ifdef SIM
    initial
        reg47_q = $urandom;
`endif



    // Register: confPix12Reg0 address:48
    wire reg48_select = wb_adr_i == 10'h30;
    reg [7:0] reg48_q;
    wire [7:0] reg48_qVoted = reg48_q;
    wire [7:0] reg48_d = wb_we && reg48_select ? dat_iVoted : reg48_qVoted;
    assign confpix12reg0 = reg48_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg48_q <= 8'h00;
        else
            reg48_q <= reg48_d;

`ifdef SIM
    initial
        reg48_q = $urandom;
`endif



    // Register: confPix12Reg1 address:49
    wire reg49_select = wb_adr_i == 10'h31;
    reg [7:0] reg49_q;
    wire [7:0] reg49_qVoted = reg49_q;
    wire [7:0] reg49_d = wb_we && reg49_select ? dat_iVoted : reg49_qVoted;
    assign confpix12reg1 = reg49_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg49_q <= 8'hf0;
        else
            reg49_q <= reg49_d;

`ifdef SIM
    initial
        reg49_q = $urandom;
`endif



    // Register: confPix12Reg2 address:50
    wire reg50_select = wb_adr_i == 10'h32;
    reg [7:0] reg50_q;
    wire [7:0] reg50_qVoted = reg50_q;
    wire [7:0] reg50_d = wb_we && reg50_select ? dat_iVoted : reg50_qVoted;
    assign confpix12reg2 = reg50_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg50_q <= 8'h1c;
        else
            reg50_q <= reg50_d;

`ifdef SIM
    initial
        reg50_q = $urandom;
`endif



    // Register: confPix12Reg3 address:51
    wire reg51_select = wb_adr_i == 10'h33;
    reg [7:0] reg51_q;
    wire [7:0] reg51_qVoted = reg51_q;
    wire [7:0] reg51_d = wb_we && reg51_select ? dat_iVoted : reg51_qVoted;
    assign confpix12reg3 = reg51_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg51_q <= 8'h40;
        else
            reg51_q <= reg51_d;

`ifdef SIM
    initial
        reg51_q = $urandom;
`endif



    // Register: confPix13Reg0 address:52
    wire reg52_select = wb_adr_i == 10'h34;
    reg [7:0] reg52_q;
    wire [7:0] reg52_qVoted = reg52_q;
    wire [7:0] reg52_d = wb_we && reg52_select ? dat_iVoted : reg52_qVoted;
    assign confpix13reg0 = reg52_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg52_q <= 8'h00;
        else
            reg52_q <= reg52_d;

`ifdef SIM
    initial
        reg52_q = $urandom;
`endif



    // Register: confPix13Reg1 address:53
    wire reg53_select = wb_adr_i == 10'h35;
    reg [7:0] reg53_q;
    wire [7:0] reg53_qVoted = reg53_q;
    wire [7:0] reg53_d = wb_we && reg53_select ? dat_iVoted : reg53_qVoted;
    assign confpix13reg1 = reg53_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg53_q <= 8'hf0;
        else
            reg53_q <= reg53_d;

`ifdef SIM
    initial
        reg53_q = $urandom;
`endif



    // Register: confPix13Reg2 address:54
    wire reg54_select = wb_adr_i == 10'h36;
    reg [7:0] reg54_q;
    wire [7:0] reg54_qVoted = reg54_q;
    wire [7:0] reg54_d = wb_we && reg54_select ? dat_iVoted : reg54_qVoted;
    assign confpix13reg2 = reg54_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg54_q <= 8'h1c;
        else
            reg54_q <= reg54_d;

`ifdef SIM
    initial
        reg54_q = $urandom;
`endif



    // Register: confPix13Reg3 address:55
    wire reg55_select = wb_adr_i == 10'h37;
    reg [7:0] reg55_q;
    wire [7:0] reg55_qVoted = reg55_q;
    wire [7:0] reg55_d = wb_we && reg55_select ? dat_iVoted : reg55_qVoted;
    assign confpix13reg3 = reg55_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg55_q <= 8'h40;
        else
            reg55_q <= reg55_d;

`ifdef SIM
    initial
        reg55_q = $urandom;
`endif



    // Register: confPix14Reg0 address:56
    wire reg56_select = wb_adr_i == 10'h38;
    reg [7:0] reg56_q;
    wire [7:0] reg56_qVoted = reg56_q;
    wire [7:0] reg56_d = wb_we && reg56_select ? dat_iVoted : reg56_qVoted;
    assign confpix14reg0 = reg56_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg56_q <= 8'h00;
        else
            reg56_q <= reg56_d;

`ifdef SIM
    initial
        reg56_q = $urandom;
`endif



    // Register: confPix14Reg1 address:57
    wire reg57_select = wb_adr_i == 10'h39;
    reg [7:0] reg57_q;
    wire [7:0] reg57_qVoted = reg57_q;
    wire [7:0] reg57_d = wb_we && reg57_select ? dat_iVoted : reg57_qVoted;
    assign confpix14reg1 = reg57_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg57_q <= 8'hf0;
        else
            reg57_q <= reg57_d;

`ifdef SIM
    initial
        reg57_q = $urandom;
`endif



    // Register: confPix14Reg2 address:58
    wire reg58_select = wb_adr_i == 10'h3a;
    reg [7:0] reg58_q;
    wire [7:0] reg58_qVoted = reg58_q;
    wire [7:0] reg58_d = wb_we && reg58_select ? dat_iVoted : reg58_qVoted;
    assign confpix14reg2 = reg58_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg58_q <= 8'h1c;
        else
            reg58_q <= reg58_d;

`ifdef SIM
    initial
        reg58_q = $urandom;
`endif



    // Register: confPix14Reg3 address:59
    wire reg59_select = wb_adr_i == 10'h3b;
    reg [7:0] reg59_q;
    wire [7:0] reg59_qVoted = reg59_q;
    wire [7:0] reg59_d = wb_we && reg59_select ? dat_iVoted : reg59_qVoted;
    assign confpix14reg3 = reg59_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg59_q <= 8'h40;
        else
            reg59_q <= reg59_d;

`ifdef SIM
    initial
        reg59_q = $urandom;
`endif



    // Register: confPix15Reg0 address:60
    wire reg60_select = wb_adr_i == 10'h3c;
    reg [7:0] reg60_q;
    wire [7:0] reg60_qVoted = reg60_q;
    wire [7:0] reg60_d = wb_we && reg60_select ? dat_iVoted : reg60_qVoted;
    assign confpix15reg0 = reg60_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg60_q <= 8'h00;
        else
            reg60_q <= reg60_d;

`ifdef SIM
    initial
        reg60_q = $urandom;
`endif



    // Register: confPix15Reg1 address:61
    wire reg61_select = wb_adr_i == 10'h3d;
    reg [7:0] reg61_q;
    wire [7:0] reg61_qVoted = reg61_q;
    wire [7:0] reg61_d = wb_we && reg61_select ? dat_iVoted : reg61_qVoted;
    assign confpix15reg1 = reg61_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg61_q <= 8'hf0;
        else
            reg61_q <= reg61_d;

`ifdef SIM
    initial
        reg61_q = $urandom;
`endif



    // Register: confPix15Reg2 address:62
    wire reg62_select = wb_adr_i == 10'h3e;
    reg [7:0] reg62_q;
    wire [7:0] reg62_qVoted = reg62_q;
    wire [7:0] reg62_d = wb_we && reg62_select ? dat_iVoted : reg62_qVoted;
    assign confpix15reg2 = reg62_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg62_q <= 8'h1c;
        else
            reg62_q <= reg62_d;

`ifdef SIM
    initial
        reg62_q = $urandom;
`endif



    // Register: confPix15Reg3 address:63
    wire reg63_select = wb_adr_i == 10'h3f;
    reg [7:0] reg63_q;
    wire [7:0] reg63_qVoted = reg63_q;
    wire [7:0] reg63_d = wb_we && reg63_select ? dat_iVoted : reg63_qVoted;
    assign confpix15reg3 = reg63_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg63_q <= 8'h40;
        else
            reg63_q <= reg63_d;

`ifdef SIM
    initial
        reg63_q = $urandom;
`endif



    // Register: confPix30Reg0 address:120
    wire reg120_select = wb_adr_i == 10'h78;
    reg [7:0] reg120_q;
    wire [7:0] reg120_qVoted = reg120_q;
    wire [7:0] reg120_d = wb_we && reg120_select ? dat_iVoted : reg120_qVoted;
    assign confpix30reg0 = reg120_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg120_q <= 8'h00;
        else
            reg120_q <= reg120_d;

`ifdef SIM
    initial
        reg120_q = $urandom;
`endif



    // Register: confPix30Reg1 address:121
    wire reg121_select = wb_adr_i == 10'h79;
    reg [7:0] reg121_q;
    wire [7:0] reg121_qVoted = reg121_q;
    wire [7:0] reg121_d = wb_we && reg121_select ? dat_iVoted : reg121_qVoted;
    assign confpix30reg1 = reg121_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg121_q <= 8'hf0;
        else
            reg121_q <= reg121_d;

`ifdef SIM
    initial
        reg121_q = $urandom;
`endif



    // Register: confPix30Reg2 address:122
    wire reg122_select = wb_adr_i == 10'h7a;
    reg [7:0] reg122_q;
    wire [7:0] reg122_qVoted = reg122_q;
    wire [7:0] reg122_d = wb_we && reg122_select ? dat_iVoted : reg122_qVoted;
    assign confpix30reg2 = reg122_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg122_q <= 8'h1c;
        else
            reg122_q <= reg122_d;

`ifdef SIM
    initial
        reg122_q = $urandom;
`endif



    // Register: confPix30Reg3 address:123
    wire reg123_select = wb_adr_i == 10'h7b;
    reg [7:0] reg123_q;
    wire [7:0] reg123_qVoted = reg123_q;
    wire [7:0] reg123_d = wb_we && reg123_select ? dat_iVoted : reg123_qVoted;
    assign confpix30reg3 = reg123_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg123_q <= 8'h40;
        else
            reg123_q <= reg123_d;

`ifdef SIM
    initial
        reg123_q = $urandom;
`endif



    // Register: confPix45Reg0 address:180
    wire reg180_select = wb_adr_i == 10'hb4;
    reg [7:0] reg180_q;
    wire [7:0] reg180_qVoted = reg180_q;
    wire [7:0] reg180_d = wb_we && reg180_select ? dat_iVoted : reg180_qVoted;
    assign confpix45reg0 = reg180_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg180_q <= 8'h00;
        else
            reg180_q <= reg180_d;

`ifdef SIM
    initial
        reg180_q = $urandom;
`endif



    // Register: confPix45Reg1 address:181
    wire reg181_select = wb_adr_i == 10'hb5;
    reg [7:0] reg181_q;
    wire [7:0] reg181_qVoted = reg181_q;
    wire [7:0] reg181_d = wb_we && reg181_select ? dat_iVoted : reg181_qVoted;
    assign confpix45reg1 = reg181_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg181_q <= 8'hf0;
        else
            reg181_q <= reg181_d;

`ifdef SIM
    initial
        reg181_q = $urandom;
`endif



    // Register: confPix45Reg2 address:182
    wire reg182_select = wb_adr_i == 10'hb6;
    reg [7:0] reg182_q;
    wire [7:0] reg182_qVoted = reg182_q;
    wire [7:0] reg182_d = wb_we && reg182_select ? dat_iVoted : reg182_qVoted;
    assign confpix45reg2 = reg182_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg182_q <= 8'h1c;
        else
            reg182_q <= reg182_d;

`ifdef SIM
    initial
        reg182_q = $urandom;
`endif



    // Register: confPix45Reg3 address:183
    wire reg183_select = wb_adr_i == 10'hb7;
    reg [7:0] reg183_q;
    wire [7:0] reg183_qVoted = reg183_q;
    wire [7:0] reg183_d = wb_we && reg183_select ? dat_iVoted : reg183_qVoted;
    assign confpix45reg3 = reg183_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg183_q <= 8'h40;
        else
            reg183_q <= reg183_d;

`ifdef SIM
    initial
        reg183_q = $urandom;
`endif



    // Register: confPix60Reg0 address:240
    wire reg240_select = wb_adr_i == 10'hf0;
    reg [7:0] reg240_q;
    wire [7:0] reg240_qVoted = reg240_q;
    wire [7:0] reg240_d = wb_we && reg240_select ? dat_iVoted : reg240_qVoted;
    assign confpix60reg0 = reg240_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg240_q <= 8'h00;
        else
            reg240_q <= reg240_d;

`ifdef SIM
    initial
        reg240_q = $urandom;
`endif



    // Register: confPix60Reg1 address:241
    wire reg241_select = wb_adr_i == 10'hf1;
    reg [7:0] reg241_q;
    wire [7:0] reg241_qVoted = reg241_q;
    wire [7:0] reg241_d = wb_we && reg241_select ? dat_iVoted : reg241_qVoted;
    assign confpix60reg1 = reg241_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg241_q <= 8'hf0;
        else
            reg241_q <= reg241_d;

`ifdef SIM
    initial
        reg241_q = $urandom;
`endif



    // Register: confPix60Reg2 address:242
    wire reg242_select = wb_adr_i == 10'hf2;
    reg [7:0] reg242_q;
    wire [7:0] reg242_qVoted = reg242_q;
    wire [7:0] reg242_d = wb_we && reg242_select ? dat_iVoted : reg242_qVoted;
    assign confpix60reg2 = reg242_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg242_q <= 8'h1c;
        else
            reg242_q <= reg242_d;

`ifdef SIM
    initial
        reg242_q = $urandom;
`endif



    // Register: confPix60Reg3 address:243
    wire reg243_select = wb_adr_i == 10'hf3;
    reg [7:0] reg243_q;
    wire [7:0] reg243_qVoted = reg243_q;
    wire [7:0] reg243_d = wb_we && reg243_select ? dat_iVoted : reg243_qVoted;
    assign confpix60reg3 = reg243_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg243_q <= 8'h40;
        else
            reg243_q <= reg243_d;

`ifdef SIM
    initial
        reg243_q = $urandom;
`endif



    // Register: confPix75Reg0 address:300
    wire reg300_select = wb_adr_i == 10'h12c;
    reg [7:0] reg300_q;
    wire [7:0] reg300_qVoted = reg300_q;
    wire [7:0] reg300_d = wb_we && reg300_select ? dat_iVoted : reg300_qVoted;
    assign confpix75reg0 = reg300_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg300_q <= 8'h00;
        else
            reg300_q <= reg300_d;

`ifdef SIM
    initial
        reg300_q = $urandom;
`endif



    // Register: confPix75Reg1 address:301
    wire reg301_select = wb_adr_i == 10'h12d;
    reg [7:0] reg301_q;
    wire [7:0] reg301_qVoted = reg301_q;
    wire [7:0] reg301_d = wb_we && reg301_select ? dat_iVoted : reg301_qVoted;
    assign confpix75reg1 = reg301_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg301_q <= 8'hf0;
        else
            reg301_q <= reg301_d;

`ifdef SIM
    initial
        reg301_q = $urandom;
`endif



    // Register: confPix75Reg2 address:302
    wire reg302_select = wb_adr_i == 10'h12e;
    reg [7:0] reg302_q;
    wire [7:0] reg302_qVoted = reg302_q;
    wire [7:0] reg302_d = wb_we && reg302_select ? dat_iVoted : reg302_qVoted;
    assign confpix75reg2 = reg302_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg302_q <= 8'h1c;
        else
            reg302_q <= reg302_d;

`ifdef SIM
    initial
        reg302_q = $urandom;
`endif



    // Register: confPix75Reg3 address:303
    wire reg303_select = wb_adr_i == 10'h12f;
    reg [7:0] reg303_q;
    wire [7:0] reg303_qVoted = reg303_q;
    wire [7:0] reg303_d = wb_we && reg303_select ? dat_iVoted : reg303_qVoted;
    assign confpix75reg3 = reg303_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg303_q <= 8'h40;
        else
            reg303_q <= reg303_d;

`ifdef SIM
    initial
        reg303_q = $urandom;
`endif



    // Register: confPix90Reg0 address:360
    wire reg360_select = wb_adr_i == 10'h168;
    reg [7:0] reg360_q;
    wire [7:0] reg360_qVoted = reg360_q;
    wire [7:0] reg360_d = wb_we && reg360_select ? dat_iVoted : reg360_qVoted;
    assign confpix90reg0 = reg360_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg360_q <= 8'h00;
        else
            reg360_q <= reg360_d;

`ifdef SIM
    initial
        reg360_q = $urandom;
`endif



    // Register: confPix90Reg1 address:361
    wire reg361_select = wb_adr_i == 10'h169;
    reg [7:0] reg361_q;
    wire [7:0] reg361_qVoted = reg361_q;
    wire [7:0] reg361_d = wb_we && reg361_select ? dat_iVoted : reg361_qVoted;
    assign confpix90reg1 = reg361_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg361_q <= 8'hf0;
        else
            reg361_q <= reg361_d;

`ifdef SIM
    initial
        reg361_q = $urandom;
`endif



    // Register: confPix90Reg2 address:362
    wire reg362_select = wb_adr_i == 10'h16a;
    reg [7:0] reg362_q;
    wire [7:0] reg362_qVoted = reg362_q;
    wire [7:0] reg362_d = wb_we && reg362_select ? dat_iVoted : reg362_qVoted;
    assign confpix90reg2 = reg362_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg362_q <= 8'h1c;
        else
            reg362_q <= reg362_d;

`ifdef SIM
    initial
        reg362_q = $urandom;
`endif



    // Register: confPix90Reg3 address:363
    wire reg363_select = wb_adr_i == 10'h16b;
    reg [7:0] reg363_q;
    wire [7:0] reg363_qVoted = reg363_q;
    wire [7:0] reg363_d = wb_we && reg363_select ? dat_iVoted : reg363_qVoted;
    assign confpix90reg3 = reg363_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg363_q <= 8'h40;
        else
            reg363_q <= reg363_d;

`ifdef SIM
    initial
        reg363_q = $urandom;
`endif



    // Register: confPix105Reg0 address:420
    wire reg420_select = wb_adr_i == 10'h1a4;
    reg [7:0] reg420_q;
    wire [7:0] reg420_qVoted = reg420_q;
    wire [7:0] reg420_d = wb_we && reg420_select ? dat_iVoted : reg420_qVoted;
    assign confpix105reg0 = reg420_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg420_q <= 8'h00;
        else
            reg420_q <= reg420_d;

`ifdef SIM
    initial
        reg420_q = $urandom;
`endif



    // Register: confPix105Reg1 address:421
    wire reg421_select = wb_adr_i == 10'h1a5;
    reg [7:0] reg421_q;
    wire [7:0] reg421_qVoted = reg421_q;
    wire [7:0] reg421_d = wb_we && reg421_select ? dat_iVoted : reg421_qVoted;
    assign confpix105reg1 = reg421_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg421_q <= 8'hf0;
        else
            reg421_q <= reg421_d;

`ifdef SIM
    initial
        reg421_q = $urandom;
`endif



    // Register: confPix105Reg2 address:422
    wire reg422_select = wb_adr_i == 10'h1a6;
    reg [7:0] reg422_q;
    wire [7:0] reg422_qVoted = reg422_q;
    wire [7:0] reg422_d = wb_we && reg422_select ? dat_iVoted : reg422_qVoted;
    assign confpix105reg2 = reg422_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg422_q <= 8'h1c;
        else
            reg422_q <= reg422_d;

`ifdef SIM
    initial
        reg422_q = $urandom;
`endif



    // Register: confPix105Reg3 address:423
    wire reg423_select = wb_adr_i == 10'h1a7;
    reg [7:0] reg423_q;
    wire [7:0] reg423_qVoted = reg423_q;
    wire [7:0] reg423_d = wb_we && reg423_select ? dat_iVoted : reg423_qVoted;
    assign confpix105reg3 = reg423_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg423_q <= 8'h40;
        else
            reg423_q <= reg423_d;

`ifdef SIM
    initial
        reg423_q = $urandom;
`endif



    // Register: confPix120Reg0 address:480
    wire reg480_select = wb_adr_i == 10'h1e0;
    reg [7:0] reg480_q;
    wire [7:0] reg480_qVoted = reg480_q;
    wire [7:0] reg480_d = wb_we && reg480_select ? dat_iVoted : reg480_qVoted;
    assign confpix120reg0 = reg480_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg480_q <= 8'h00;
        else
            reg480_q <= reg480_d;

`ifdef SIM
    initial
        reg480_q = $urandom;
`endif



    // Register: confPix120Reg1 address:481
    wire reg481_select = wb_adr_i == 10'h1e1;
    reg [7:0] reg481_q;
    wire [7:0] reg481_qVoted = reg481_q;
    wire [7:0] reg481_d = wb_we && reg481_select ? dat_iVoted : reg481_qVoted;
    assign confpix120reg1 = reg481_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg481_q <= 8'hf0;
        else
            reg481_q <= reg481_d;

`ifdef SIM
    initial
        reg481_q = $urandom;
`endif



    // Register: confPix120Reg2 address:482
    wire reg482_select = wb_adr_i == 10'h1e2;
    reg [7:0] reg482_q;
    wire [7:0] reg482_qVoted = reg482_q;
    wire [7:0] reg482_d = wb_we && reg482_select ? dat_iVoted : reg482_qVoted;
    assign confpix120reg2 = reg482_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg482_q <= 8'h1c;
        else
            reg482_q <= reg482_d;

`ifdef SIM
    initial
        reg482_q = $urandom;
`endif



    // Register: confPix120Reg3 address:483
    wire reg483_select = wb_adr_i == 10'h1e3;
    reg [7:0] reg483_q;
    wire [7:0] reg483_qVoted = reg483_q;
    wire [7:0] reg483_d = wb_we && reg483_select ? dat_iVoted : reg483_qVoted;
    assign confpix120reg3 = reg483_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg483_q <= 8'h40;
        else
            reg483_q <= reg483_d;

`ifdef SIM
    initial
        reg483_q = $urandom;
`endif



    // Register: confPix135Reg0 address:540
    wire reg540_select = wb_adr_i == 10'h21c;
    reg [7:0] reg540_q;
    wire [7:0] reg540_qVoted = reg540_q;
    wire [7:0] reg540_d = wb_we && reg540_select ? dat_iVoted : reg540_qVoted;
    assign confpix135reg0 = reg540_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg540_q <= 8'h00;
        else
            reg540_q <= reg540_d;

`ifdef SIM
    initial
        reg540_q = $urandom;
`endif



    // Register: confPix135Reg1 address:541
    wire reg541_select = wb_adr_i == 10'h21d;
    reg [7:0] reg541_q;
    wire [7:0] reg541_qVoted = reg541_q;
    wire [7:0] reg541_d = wb_we && reg541_select ? dat_iVoted : reg541_qVoted;
    assign confpix135reg1 = reg541_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg541_q <= 8'hf0;
        else
            reg541_q <= reg541_d;

`ifdef SIM
    initial
        reg541_q = $urandom;
`endif



    // Register: confPix135Reg2 address:542
    wire reg542_select = wb_adr_i == 10'h21e;
    reg [7:0] reg542_q;
    wire [7:0] reg542_qVoted = reg542_q;
    wire [7:0] reg542_d = wb_we && reg542_select ? dat_iVoted : reg542_qVoted;
    assign confpix135reg2 = reg542_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg542_q <= 8'h1c;
        else
            reg542_q <= reg542_d;

`ifdef SIM
    initial
        reg542_q = $urandom;
`endif



    // Register: confPix135Reg3 address:543
    wire reg543_select = wb_adr_i == 10'h21f;
    reg [7:0] reg543_q;
    wire [7:0] reg543_qVoted = reg543_q;
    wire [7:0] reg543_d = wb_we && reg543_select ? dat_iVoted : reg543_qVoted;
    assign confpix135reg3 = reg543_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg543_q <= 8'h40;
        else
            reg543_q <= reg543_d;

`ifdef SIM
    initial
        reg543_q = $urandom;
`endif



    // Register: confPix150Reg0 address:600
    wire reg600_select = wb_adr_i == 10'h258;
    reg [7:0] reg600_q;
    wire [7:0] reg600_qVoted = reg600_q;
    wire [7:0] reg600_d = wb_we && reg600_select ? dat_iVoted : reg600_qVoted;
    assign confpix150reg0 = reg600_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg600_q <= 8'h00;
        else
            reg600_q <= reg600_d;

`ifdef SIM
    initial
        reg600_q = $urandom;
`endif



    // Register: confPix150Reg1 address:601
    wire reg601_select = wb_adr_i == 10'h259;
    reg [7:0] reg601_q;
    wire [7:0] reg601_qVoted = reg601_q;
    wire [7:0] reg601_d = wb_we && reg601_select ? dat_iVoted : reg601_qVoted;
    assign confpix150reg1 = reg601_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg601_q <= 8'hf0;
        else
            reg601_q <= reg601_d;

`ifdef SIM
    initial
        reg601_q = $urandom;
`endif



    // Register: confPix150Reg2 address:602
    wire reg602_select = wb_adr_i == 10'h25a;
    reg [7:0] reg602_q;
    wire [7:0] reg602_qVoted = reg602_q;
    wire [7:0] reg602_d = wb_we && reg602_select ? dat_iVoted : reg602_qVoted;
    assign confpix150reg2 = reg602_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg602_q <= 8'h1c;
        else
            reg602_q <= reg602_d;

`ifdef SIM
    initial
        reg602_q = $urandom;
`endif



    // Register: confPix150Reg3 address:603
    wire reg603_select = wb_adr_i == 10'h25b;
    reg [7:0] reg603_q;
    wire [7:0] reg603_qVoted = reg603_q;
    wire [7:0] reg603_d = wb_we && reg603_select ? dat_iVoted : reg603_qVoted;
    assign confpix150reg3 = reg603_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg603_q <= 8'h40;
        else
            reg603_q <= reg603_d;

`ifdef SIM
    initial
        reg603_q = $urandom;
`endif



    // Register: confPix165Reg0 address:660
    wire reg660_select = wb_adr_i == 10'h294;
    reg [7:0] reg660_q;
    wire [7:0] reg660_qVoted = reg660_q;
    wire [7:0] reg660_d = wb_we && reg660_select ? dat_iVoted : reg660_qVoted;
    assign confpix165reg0 = reg660_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg660_q <= 8'h00;
        else
            reg660_q <= reg660_d;

`ifdef SIM
    initial
        reg660_q = $urandom;
`endif



    // Register: confPix165Reg1 address:661
    wire reg661_select = wb_adr_i == 10'h295;
    reg [7:0] reg661_q;
    wire [7:0] reg661_qVoted = reg661_q;
    wire [7:0] reg661_d = wb_we && reg661_select ? dat_iVoted : reg661_qVoted;
    assign confpix165reg1 = reg661_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg661_q <= 8'hf0;
        else
            reg661_q <= reg661_d;

`ifdef SIM
    initial
        reg661_q = $urandom;
`endif



    // Register: confPix165Reg2 address:662
    wire reg662_select = wb_adr_i == 10'h296;
    reg [7:0] reg662_q;
    wire [7:0] reg662_qVoted = reg662_q;
    wire [7:0] reg662_d = wb_we && reg662_select ? dat_iVoted : reg662_qVoted;
    assign confpix165reg2 = reg662_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg662_q <= 8'h1c;
        else
            reg662_q <= reg662_d;

`ifdef SIM
    initial
        reg662_q = $urandom;
`endif



    // Register: confPix165Reg3 address:663
    wire reg663_select = wb_adr_i == 10'h297;
    reg [7:0] reg663_q;
    wire [7:0] reg663_qVoted = reg663_q;
    wire [7:0] reg663_d = wb_we && reg663_select ? dat_iVoted : reg663_qVoted;
    assign confpix165reg3 = reg663_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg663_q <= 8'h40;
        else
            reg663_q <= reg663_d;

`ifdef SIM
    initial
        reg663_q = $urandom;
`endif



    // Register: confPix180Reg0 address:720
    wire reg720_select = wb_adr_i == 10'h2d0;
    reg [7:0] reg720_q;
    wire [7:0] reg720_qVoted = reg720_q;
    wire [7:0] reg720_d = wb_we && reg720_select ? dat_iVoted : reg720_qVoted;
    assign confpix180reg0 = reg720_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg720_q <= 8'h00;
        else
            reg720_q <= reg720_d;

`ifdef SIM
    initial
        reg720_q = $urandom;
`endif



    // Register: confPix180Reg1 address:721
    wire reg721_select = wb_adr_i == 10'h2d1;
    reg [7:0] reg721_q;
    wire [7:0] reg721_qVoted = reg721_q;
    wire [7:0] reg721_d = wb_we && reg721_select ? dat_iVoted : reg721_qVoted;
    assign confpix180reg1 = reg721_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg721_q <= 8'hf0;
        else
            reg721_q <= reg721_d;

`ifdef SIM
    initial
        reg721_q = $urandom;
`endif



    // Register: confPix180Reg2 address:722
    wire reg722_select = wb_adr_i == 10'h2d2;
    reg [7:0] reg722_q;
    wire [7:0] reg722_qVoted = reg722_q;
    wire [7:0] reg722_d = wb_we && reg722_select ? dat_iVoted : reg722_qVoted;
    assign confpix180reg2 = reg722_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg722_q <= 8'h1c;
        else
            reg722_q <= reg722_d;

`ifdef SIM
    initial
        reg722_q = $urandom;
`endif



    // Register: confPix180Reg3 address:723
    wire reg723_select = wb_adr_i == 10'h2d3;
    reg [7:0] reg723_q;
    wire [7:0] reg723_qVoted = reg723_q;
    wire [7:0] reg723_d = wb_we && reg723_select ? dat_iVoted : reg723_qVoted;
    assign confpix180reg3 = reg723_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg723_q <= 8'h40;
        else
            reg723_q <= reg723_d;

`ifdef SIM
    initial
        reg723_q = $urandom;
`endif



    // Register: confPix195Reg0 address:780
    wire reg780_select = wb_adr_i == 10'h30c;
    reg [7:0] reg780_q;
    wire [7:0] reg780_qVoted = reg780_q;
    wire [7:0] reg780_d = wb_we && reg780_select ? dat_iVoted : reg780_qVoted;
    assign confpix195reg0 = reg780_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg780_q <= 8'h00;
        else
            reg780_q <= reg780_d;

`ifdef SIM
    initial
        reg780_q = $urandom;
`endif



    // Register: confPix195Reg1 address:781
    wire reg781_select = wb_adr_i == 10'h30d;
    reg [7:0] reg781_q;
    wire [7:0] reg781_qVoted = reg781_q;
    wire [7:0] reg781_d = wb_we && reg781_select ? dat_iVoted : reg781_qVoted;
    assign confpix195reg1 = reg781_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg781_q <= 8'hf0;
        else
            reg781_q <= reg781_d;

`ifdef SIM
    initial
        reg781_q = $urandom;
`endif



    // Register: confPix195Reg2 address:782
    wire reg782_select = wb_adr_i == 10'h30e;
    reg [7:0] reg782_q;
    wire [7:0] reg782_qVoted = reg782_q;
    wire [7:0] reg782_d = wb_we && reg782_select ? dat_iVoted : reg782_qVoted;
    assign confpix195reg2 = reg782_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg782_q <= 8'h1c;
        else
            reg782_q <= reg782_d;

`ifdef SIM
    initial
        reg782_q = $urandom;
`endif



    // Register: confPix195Reg3 address:783
    wire reg783_select = wb_adr_i == 10'h30f;
    reg [7:0] reg783_q;
    wire [7:0] reg783_qVoted = reg783_q;
    wire [7:0] reg783_d = wb_we && reg783_select ? dat_iVoted : reg783_qVoted;
    assign confpix195reg3 = reg783_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg783_q <= 8'h40;
        else
            reg783_q <= reg783_d;

`ifdef SIM
    initial
        reg783_q = $urandom;
`endif



    // Register: confPix210Reg0 address:840
    wire reg840_select = wb_adr_i == 10'h348;
    reg [7:0] reg840_q;
    wire [7:0] reg840_qVoted = reg840_q;
    wire [7:0] reg840_d = wb_we && reg840_select ? dat_iVoted : reg840_qVoted;
    assign confpix210reg0 = reg840_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg840_q <= 8'h00;
        else
            reg840_q <= reg840_d;

`ifdef SIM
    initial
        reg840_q = $urandom;
`endif



    // Register: confPix210Reg1 address:841
    wire reg841_select = wb_adr_i == 10'h349;
    reg [7:0] reg841_q;
    wire [7:0] reg841_qVoted = reg841_q;
    wire [7:0] reg841_d = wb_we && reg841_select ? dat_iVoted : reg841_qVoted;
    assign confpix210reg1 = reg841_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg841_q <= 8'hf0;
        else
            reg841_q <= reg841_d;

`ifdef SIM
    initial
        reg841_q = $urandom;
`endif



    // Register: confPix210Reg2 address:842
    wire reg842_select = wb_adr_i == 10'h34a;
    reg [7:0] reg842_q;
    wire [7:0] reg842_qVoted = reg842_q;
    wire [7:0] reg842_d = wb_we && reg842_select ? dat_iVoted : reg842_qVoted;
    assign confpix210reg2 = reg842_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg842_q <= 8'h1c;
        else
            reg842_q <= reg842_d;

`ifdef SIM
    initial
        reg842_q = $urandom;
`endif



    // Register: confPix210Reg3 address:843
    wire reg843_select = wb_adr_i == 10'h34b;
    reg [7:0] reg843_q;
    wire [7:0] reg843_qVoted = reg843_q;
    wire [7:0] reg843_d = wb_we && reg843_select ? dat_iVoted : reg843_qVoted;
    assign confpix210reg3 = reg843_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg843_q <= 8'h40;
        else
            reg843_q <= reg843_d;

`ifdef SIM
    initial
        reg843_q = $urandom;
`endif



    // Register: confLdpuIniWin1L address:904
    wire reg904_select = wb_adr_i == 10'h388;
    reg [7:0] reg904_q;
    wire [7:0] reg904_qVoted = reg904_q;
    wire [7:0] reg904_d = wb_we && reg904_select ? dat_iVoted : reg904_qVoted;
    assign confldpuiniwin1l = reg904_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg904_q <= 8'h00;//reg904_q <= 8'h00;
        else
            reg904_q <= reg904_d;

`ifdef SIM
    initial
        reg904_q = $urandom;
`endif



    // Register: confLdpuIniWin1H address:905
    wire reg905_select = wb_adr_i == 10'h389;
    reg [7:0] reg905_q;
    wire [7:0] reg905_qVoted = reg905_q;
    wire [7:0] reg905_d = wb_we && reg905_select ? dat_iVoted : reg905_qVoted;
    assign confldpuiniwin1h = reg905_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg905_q <= 8'h18;//reg905_q <= 8'h18;
        else
            reg905_q <= reg905_d;

`ifdef SIM
    initial
        reg905_q = $urandom;
`endif



    // Register: confLdpuIniWin2L address:906
    wire reg906_select = wb_adr_i == 10'h38a;
    reg [7:0] reg906_q;
    wire [7:0] reg906_qVoted = reg906_q;
    wire [7:0] reg906_d = wb_we && reg906_select ? dat_iVoted : reg906_qVoted;
    assign confldpuiniwin2l = reg906_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg906_q <= 8'h00;//reg906_q <= 8'h00;
        else
            reg906_q <= reg906_d;

`ifdef SIM
    initial
        reg906_q = $urandom;
`endif



    // Register: confLdpuIniWin2H address:907
    wire reg907_select = wb_adr_i == 10'h38b;
    reg [7:0] reg907_q;
    wire [7:0] reg907_qVoted = reg907_q;
    wire [7:0] reg907_d = wb_we && reg907_select ? dat_iVoted : reg907_qVoted;
    assign confldpuiniwin2h = reg907_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg907_q <= 8'hff;//reg907_q <= 8'hff;
        else
            reg907_q <= reg907_d;

`ifdef SIM
    initial
        reg907_q = $urandom;
`endif



    // Register: CONF_LDPU_CNTRL address:908
    wire reg908_select = wb_adr_i == 10'h38c;
    reg [7:0] reg908_q;
    wire [7:0] reg908_qVoted = reg908_q;
    wire [7:0] reg908_d = wb_we && reg908_select ? dat_iVoted : reg908_qVoted;
    assign conf_ldpu_cntrl = reg908_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg908_q <= 8'h08;//reg908_q <= 8'h08;
        else
            reg908_q <= reg908_d;

`ifdef SIM
    initial
        reg908_q = $urandom;
`endif


    // Register: confTdpuLatencyL address:912
    wire reg912_select = wb_adr_i == 10'h390;
    reg [7:0] reg912_q;
    wire [7:0] reg912_qVoted = reg912_q;
    wire [7:0] reg912_d = wb_we && reg912_select ? dat_iVoted : reg912_qVoted;
    assign conftdpulatencyl = reg912_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg912_q <= 8'h79;
        else
            reg912_q <= reg912_d;

`ifdef SIM
    initial
        reg912_q = $urandom;
`endif



    // Register: confTdpuLatencyH address:913
    wire reg913_select = wb_adr_i == 10'h391;
    reg [7:0] reg913_q;
    wire [7:0] reg913_qVoted = reg913_q;
    wire [7:0] reg913_d = wb_we && reg913_select ? dat_iVoted : reg913_qVoted;
    assign conftdpulatencyh = reg913_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg913_q <= 8'h05;
        else
            reg913_q <= reg913_d;

`ifdef SIM
    initial
        reg913_q = $urandom;
`endif



    // Register: CONF_TDPU_CNTRL address:914
    wire reg914_select = wb_adr_i == 10'h392;
    reg [7:0] reg914_q;
    wire [7:0] reg914_qVoted = reg914_q;
    wire [7:0] reg914_d = wb_we && reg914_select ? dat_iVoted : reg914_qVoted;
    assign conf_tdpu_cntrl = reg914_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg914_q <= 8'h19; //default 8'h19
        else
            reg914_q <= reg914_d;

`ifdef SIM
    initial
        reg914_q = $urandom;
`endif



    // Register: CONF_TDPU_PATTERN address:915
    wire reg915_select = wb_adr_i == 10'h393;
    reg [7:0] reg915_q;
    wire [7:0] reg915_qVoted = reg915_q;
    wire [7:0] reg915_d = wb_we && reg915_select ? dat_iVoted : reg915_qVoted;
    assign conf_tdpu_pattern = reg915_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg915_q <= 8'haa;
        else
            reg915_q <= reg915_d;

`ifdef SIM
    initial
        reg915_q = $urandom;
`endif



    // Register: CONF_TDPU_OCUPREF address:916
    wire reg916_select = wb_adr_i == 10'h394;
    reg [7:0] reg916_q;
    wire [7:0] reg916_qVoted = reg916_q;
    wire [7:0] reg916_d = wb_we && reg916_select ? dat_iVoted : reg916_qVoted;
    assign conf_tdpu_ocupref = reg916_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg916_q <= 8'h1f;
        else
            reg916_q <= reg916_d;

`ifdef SIM
    initial
        reg916_q = $urandom;
`endif



    // Register: dacRPGConf2 address:960
    wire reg960_select = wb_adr_i == 10'h3c0;
    reg [7:0] reg960_q;
    wire [7:0] reg960_qVoted = reg960_q;
    wire [7:0] reg960_d = wb_we && reg960_select ? dat_iVoted : reg960_qVoted;
    assign dacrpgconf2 = reg960_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg960_q <= 8'h00;
        else
            reg960_q <= reg960_d;

`ifdef SIM
    initial
        reg960_q = $urandom;
`endif



    // Register: dacRPGConf1 address:961
    wire reg961_select = wb_adr_i == 10'h3c1;
    reg [7:0] reg961_q;
    wire [7:0] reg961_qVoted = reg961_q;
    wire [7:0] reg961_d = wb_we && reg961_select ? dat_iVoted : reg961_qVoted;
    assign dacrpgconf1 = reg961_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg961_q <= 8'h00;
        else
            reg961_q <= reg961_d;

`ifdef SIM
    initial
        reg961_q = $urandom;
`endif



    // Register: bias_ch_sel_pulser address:962
    wire reg962_select = wb_adr_i == 10'h3c2;
    reg [7:0] reg962_q;
    wire [7:0] reg962_qVoted = reg962_q;
    wire [7:0] reg962_d = wb_we && reg962_select ? dat_iVoted : reg962_qVoted;
    assign bias_ch_sel_pulser = reg962_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg962_q <= 8'h20;
        else
            reg962_q <= reg962_d;

`ifdef SIM
    initial
        reg962_q = $urandom;
`endif



    // Register: bias_ch_dac_pa address:963
    wire reg963_select = wb_adr_i == 10'h3c3;
    reg [7:0] reg963_q;
    wire [7:0] reg963_qVoted = reg963_q;
    wire [7:0] reg963_d = wb_we && reg963_select ? dat_iVoted : reg963_qVoted;
    assign bias_ch_dac_pa = reg963_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg963_q <= 8'h20;
        else
            reg963_q <= reg963_d;

`ifdef SIM
    initial
        reg963_q = $urandom;
`endif



    // Register: bias_ch_dac_dc_pa address:964
    wire reg964_select = wb_adr_i == 10'h3c4;
    reg [7:0] reg964_q;
    wire [7:0] reg964_qVoted = reg964_q;
    wire [7:0] reg964_d = wb_we && reg964_select ? dat_iVoted : reg964_qVoted;
    assign bias_ch_dac_dc_pa = reg964_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg964_q <= 8'h00;
        else
            reg964_q <= reg964_d;

`ifdef SIM
    initial
        reg964_q = $urandom;
`endif



    // Register: dac10bConf1 address:965
    wire reg965_select = wb_adr_i == 10'h3c5;
    reg [7:0] reg965_q;
    wire [7:0] reg965_qVoted = reg965_q;
    wire [7:0] reg965_d = wb_we && reg965_select ? dat_iVoted : reg965_qVoted;
    assign dac10bconf1 = reg965_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg965_q <= 8'h00;
        else
            reg965_q <= reg965_d;

`ifdef SIM
    initial
        reg965_q = $urandom;
`endif



    // Register: dac10bConf2 address:966
    wire reg966_select = wb_adr_i == 10'h3c6;
    reg [7:0] reg966_q;
    wire [7:0] reg966_qVoted = reg966_q;
    wire [7:0] reg966_d = wb_we && reg966_select ? dat_iVoted : reg966_qVoted;
    assign dac10bconf2 = reg966_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg966_q <= 8'h04;
        else
            reg966_q <= reg966_d;

`ifdef SIM
    initial
        reg966_q = $urandom;
`endif



    // Register: pixelAddr address:967
    wire reg967_select = wb_adr_i == 10'h3c7;
    reg [7:0] reg967_q;
    wire [7:0] reg967_qVoted = reg967_q;
    wire [7:0] reg967_d = wb_we && reg967_select ? dat_iVoted : reg967_qVoted;
    assign pixeladdr = reg967_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg967_q <= 8'h00;
        else
            reg967_q <= reg967_d;

`ifdef SIM
    initial
        reg967_q = $urandom;
`endif



    // Register: dll_120p_toa_cBit address:968
    wire reg968_select = wb_adr_i == 10'h3c8;
    reg [7:0] reg968_q;
    wire [7:0] reg968_qVoted = reg968_q;
    wire [7:0] reg968_d = wb_we && reg968_select ? dat_iVoted : reg968_qVoted;
    assign dll_120p_toa_cbit = reg968_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg968_q <= 8'h00;
        else
            reg968_q <= reg968_d;

`ifdef SIM
    initial
        reg968_q = $urandom;
`endif



    // Register: dll_120p_toa_cp address:969
    wire reg969_select = wb_adr_i == 10'h3c9;
    reg [7:0] reg969_q;
    wire [7:0] reg969_qVoted = reg969_q;
    wire [7:0] reg969_d = wb_we && reg969_select ? dat_iVoted : reg969_qVoted;
    assign dll_120p_toa_cp = reg969_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg969_q <= 8'h00;
        else
            reg969_q <= reg969_d;

`ifdef SIM
    initial
        reg969_q = $urandom;
`endif



    // Register: dll_120p_toa_comp address:970
    wire reg970_select = wb_adr_i == 10'h3ca;
    reg [7:0] reg970_q;
    wire [7:0] reg970_qVoted = reg970_q;
    wire [7:0] reg970_d = wb_we && reg970_select ? dat_iVoted : reg970_qVoted;
    assign dll_120p_toa_comp = reg970_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg970_q <= 8'h00;
        else
            reg970_q <= reg970_d;

`ifdef SIM
    initial
        reg970_q = $urandom;
`endif



    // Register: dll_120p_tot_cBit address:971
    wire reg971_select = wb_adr_i == 10'h3cb;
    reg [7:0] reg971_q;
    wire [7:0] reg971_qVoted = reg971_q;
    wire [7:0] reg971_d = wb_we && reg971_select ? dat_iVoted : reg971_qVoted;
    assign dll_120p_tot_cbit = reg971_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg971_q <= 8'h00;
        else
            reg971_q <= reg971_d;

`ifdef SIM
    initial
        reg971_q = $urandom;
`endif



    // Register: dll_120p_tot_cp address:972
    wire reg972_select = wb_adr_i == 10'h3cc;
    reg [7:0] reg972_q;
    wire [7:0] reg972_qVoted = reg972_q;
    wire [7:0] reg972_d = wb_we && reg972_select ? dat_iVoted : reg972_qVoted;
    assign dll_120p_tot_cp = reg972_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg972_q <= 8'h00;
        else
            reg972_q <= reg972_d;

`ifdef SIM
    initial
        reg972_q = $urandom;
`endif



    // Register: dll_120p_tot_comp address:973
    wire reg973_select = wb_adr_i == 10'h3cd;
    reg [7:0] reg973_q;
    wire [7:0] reg973_qVoted = reg973_q;
    wire [7:0] reg973_d = wb_we && reg973_select ? dat_iVoted : reg973_qVoted;
    assign dll_120p_tot_comp = reg973_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg973_q <= 8'h00;
        else
            reg973_q <= reg973_d;

`ifdef SIM
    initial
        reg973_q = $urandom;
`endif



    // Register: dll_140p_toa_cBit address:974
    wire reg974_select = wb_adr_i == 10'h3ce;
    reg [7:0] reg974_q;
    wire [7:0] reg974_qVoted = reg974_q;
    wire [7:0] reg974_d = wb_we && reg974_select ? dat_iVoted : reg974_qVoted;
    assign dll_140p_toa_cbit = reg974_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg974_q <= 8'h00;
        else
            reg974_q <= reg974_d;

`ifdef SIM
    initial
        reg974_q = $urandom;
`endif



    // Register: dll_140p_toa_cp address:975
    wire reg975_select = wb_adr_i == 10'h3cf;
    reg [7:0] reg975_q;
    wire [7:0] reg975_qVoted = reg975_q;
    wire [7:0] reg975_d = wb_we && reg975_select ? dat_iVoted : reg975_qVoted;
    assign dll_140p_toa_cp = reg975_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg975_q <= 8'h00;
        else
            reg975_q <= reg975_d;

`ifdef SIM
    initial
        reg975_q = $urandom;
`endif



    // Register: dll_140p_toa_comp address:976
    wire reg976_select = wb_adr_i == 10'h3d0;
    reg [7:0] reg976_q;
    wire [7:0] reg976_qVoted = reg976_q;
    wire [7:0] reg976_d = wb_we && reg976_select ? dat_iVoted : reg976_qVoted;
    assign dll_140p_toa_comp = reg976_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg976_q <= 8'h00;
        else
            reg976_q <= reg976_d;

`ifdef SIM
    initial
        reg976_q = $urandom;
`endif



    // Register: dllCntrConf address:977
    wire reg977_select = wb_adr_i == 10'h3d1;
    reg [7:0] reg977_q;
    wire [7:0] reg977_qVoted = reg977_q;
    wire [7:0] reg977_d = wb_we && reg977_select ? dat_iVoted : reg977_qVoted;
    assign dllcntrconf = reg977_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg977_q <= 8'h30;
        else
            reg977_q <= reg977_d;

`ifdef SIM
    initial
        reg977_q = $urandom;
`endif



    // Register: selProbeBiasConf address:978
    wire reg978_select = wb_adr_i == 10'h3d2;
    reg [7:0] reg978_q;
    wire [7:0] reg978_qVoted = reg978_q;
    wire [7:0] reg978_d = wb_we && reg978_select ? dat_iVoted : reg978_qVoted;
    assign selprobebiasconf = reg978_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg978_q <= 8'h00;
        else
            reg978_q <= reg978_d;

`ifdef SIM
    initial
        reg978_q = $urandom;
`endif



    // Register: confGlobalEnProbe address:979
    wire reg979_select = wb_adr_i == 10'h3d3;
    reg [7:0] reg979_q;
    wire [7:0] reg979_qVoted = reg979_q;
    wire [7:0] reg979_d = wb_we && reg979_select ? dat_iVoted : reg979_qVoted;
    assign confglobalenprobe = reg979_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg979_q <= 8'h00;
        else
            reg979_q <= reg979_d;

`ifdef SIM
    initial
        reg979_q = $urandom;
`endif



    // Register: confGlobalSignalTDCs address:980
    wire reg980_select = wb_adr_i == 10'h3d4;
    reg [7:0] reg980_q;
    wire [7:0] reg980_qVoted = reg980_q;
    wire [7:0] reg980_d = wb_we && reg980_select ? dat_iVoted : reg980_qVoted;
    assign confglobalsignaltdcs = reg980_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg980_q <= 8'h07;
        else
            reg980_q <= reg980_d;

`ifdef SIM
    initial
        reg980_q = $urandom;
`endif



    // Register: confGlobalSignalRinCdCp address:981
    wire reg981_select = wb_adr_i == 10'h3d5;
    reg [7:0] reg981_q;
    wire [7:0] reg981_qVoted = reg981_q;
    wire [7:0] reg981_d = wb_we && reg981_select ? dat_iVoted : reg981_qVoted;
    assign confglobalsignalrincdcp = reg981_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg981_q <= 8'h00;
        else
            reg981_q <= reg981_d;

`ifdef SIM
    initial
        reg981_q = $urandom;
`endif



    // Register: CONF_GLOBAL_CNTR address:982
    wire reg982_select = wb_adr_i == 10'h3d6;
    reg [7:0] reg982_q;
    wire [7:0] reg982_qVoted = reg982_q;
    wire [7:0] reg982_d = wb_we && reg982_select ? dat_iVoted : reg982_qVoted;
    assign conf_global_cntr = reg982_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg982_q <= 8'h00;
        else
            reg982_q <= reg982_d;

`ifdef SIM
    initial
        reg982_q = $urandom;
`endif



    // Register: CONF_GLOBAL_OCCUPANCY address:983
    wire reg983_select = wb_adr_i == 10'h3d7;
    reg [7:0] reg983_q;
    wire [7:0] reg983_qVoted = reg983_q;
    wire [7:0] reg983_d = wb_we && reg983_select ? dat_iVoted : reg983_qVoted;
    assign conf_global_occupancy = reg983_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg983_q <= 8'h0f;
        else
            reg983_q <= reg983_d;

`ifdef SIM
    initial
        reg983_q = $urandom;
`endif



    // Register: enableCGEOCL address:984
    wire reg984_select = wb_adr_i == 10'h3d8;
    reg [7:0] reg984_q;
    wire [7:0] reg984_qVoted = reg984_q;
    wire [7:0] reg984_d = wb_we && reg984_select ? dat_iVoted : reg984_qVoted;
    assign enablecgeocl = reg984_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg984_q <= 8'hff;
        else
            reg984_q <= reg984_d;

`ifdef SIM
    initial
        reg984_q = $urandom;
`endif



    // Register: enableCGEOCH address:985
    wire reg985_select = wb_adr_i == 10'h3d9;
    reg [7:0] reg985_q;
    wire [7:0] reg985_qVoted = reg985_q;
    wire [7:0] reg985_d = wb_we && reg985_select ? dat_iVoted : reg985_qVoted;
    assign enablecgeoch = reg985_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg985_q <= 8'h7f;
        else
            reg985_q <= reg985_d;

`ifdef SIM
    initial
        reg985_q = $urandom;
`endif



    // Register: CONF_ANAPERI_SELPROBEMON address:986
    wire reg986_select = wb_adr_i == 10'h3da;
    reg [7:0] reg986_q;
    wire [7:0] reg986_qVoted = reg986_q;
    wire [7:0] reg986_d = wb_we && reg986_select ? dat_iVoted : reg986_qVoted;
    assign conf_anaperi_selprobemon = reg986_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg986_q <= 8'h00;
        else
            reg986_q <= reg986_d;

`ifdef SIM
    initial
        reg986_q = $urandom;
`endif



    // Register: bgConf address:992
    wire reg992_select = wb_adr_i == 10'h3e0;
    reg [7:0] reg992_q;
    wire [7:0] reg992_qVoted = reg992_q;
    wire [7:0] reg992_d = wb_we && reg992_select ? dat_iVoted : reg992_qVoted;
    assign bgconf = reg992_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg992_q <= 8'h0d;
        else
            reg992_q <= reg992_d;

`ifdef SIM
    initial
        reg992_q = $urandom;
`endif



    // Register: pllCpConf address:993
    wire reg993_select = wb_adr_i == 10'h3e1;
    reg [7:0] reg993_q;
    wire [7:0] reg993_qVoted = reg993_q;
    wire [7:0] reg993_d = wb_we && reg993_select ? dat_iVoted : reg993_qVoted;
    assign pllcpconf = reg993_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg993_q <= 8'h20;
        else
            reg993_q <= reg993_d;

`ifdef SIM
    initial
        reg993_q = $urandom;
`endif



    // Register: pllBwConf address:994
    wire reg994_select = wb_adr_i == 10'h3e2;
    reg [7:0] reg994_q;
    wire [7:0] reg994_qVoted = reg994_q;
    wire [7:0] reg994_d = wb_we && reg994_select ? dat_iVoted : reg994_qVoted;
    assign pllbwconf = reg994_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg994_q <= 8'h08;
        else
            reg994_q <= reg994_d;

`ifdef SIM
    initial
        reg994_q = $urandom;
`endif



    // Register: pllCntr1 address:995
    wire reg995_select = wb_adr_i == 10'h3e3;
    reg [7:0] reg995_q;
    wire [7:0] reg995_qVoted = reg995_q;
    wire [7:0] reg995_d = wb_we && reg995_select ? dat_iVoted : reg995_qVoted;
    assign pllcntr1 = reg995_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg995_q <= 8'h11;
        else
            reg995_q <= reg995_d;

`ifdef SIM
    initial
        reg995_q = $urandom;
`endif



    // Register: pllCntr2 address:996
    wire reg996_select = wb_adr_i == 10'h3e4;
    reg [7:0] reg996_q;
    wire [7:0] reg996_qVoted = reg996_q;
    wire [7:0] reg996_d = wb_we && reg996_select ? dat_iVoted : reg996_qVoted;
    assign pllcntr2 = reg996_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg996_q <= 8'h29;
        else
            reg996_q <= reg996_d;

`ifdef SIM
    initial
        reg996_q = $urandom;
`endif



    // Register: CONF_ANAPERI_PLLLOCKSAMPLES address:997
    wire reg997_select = wb_adr_i == 10'h3e5;
    reg [7:0] reg997_q;
    wire [7:0] reg997_qVoted = reg997_q;
    wire [7:0] reg997_d = wb_we && reg997_select ? dat_iVoted : reg997_qVoted;
    assign conf_anaperi_plllocksamples = reg997_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg997_q <= 8'h32;
        else
            reg997_q <= reg997_d;

`ifdef SIM
    initial
        reg997_q = $urandom;
`endif



    // Register: CONF_ANAPERI address:998
    wire reg998_select = wb_adr_i == 10'h3e6;
    reg [7:0] reg998_q;
    wire [7:0] reg998_qVoted = reg998_q;
    wire [7:0] reg998_d = wb_we && reg998_select ? dat_iVoted : reg998_qVoted;
    assign conf_anaperi = reg998_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg998_q <= 8'h02;
        else
            reg998_q <= reg998_d;

`ifdef SIM
    initial
        reg998_q = $urandom;
`endif



    // Register: psDelay1 address:999
    wire reg999_select = wb_adr_i == 10'h3e7;
    reg [7:0] reg999_q;
    wire [7:0] reg999_qVoted = reg999_q;
    wire [7:0] reg999_d = wb_we && reg999_select ? dat_iVoted : reg999_qVoted;
    assign psdelay1 = reg999_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg999_q <= 8'h00;
        else
            reg999_q <= reg999_d;

`ifdef SIM
    initial
        reg999_q = $urandom;
`endif



    // Register: psDelay2 address:1000
    wire reg1000_select = wb_adr_i == 10'h3e8;
    reg [7:0] reg1000_q;
    wire [7:0] reg1000_qVoted = reg1000_q;
    wire [7:0] reg1000_d = wb_we && reg1000_select ? dat_iVoted : reg1000_qVoted;
    assign psdelay2 = reg1000_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1000_q <= 8'h00;
        else
            reg1000_q <= reg1000_d;

`ifdef SIM
    initial
        reg1000_q = $urandom;
`endif



    // Register: psDelayLum address:1001
    wire reg1001_select = wb_adr_i == 10'h3e9;
    reg [7:0] reg1001_q;
    wire [7:0] reg1001_qVoted = reg1001_q;
    wire [7:0] reg1001_d = wb_we && reg1001_select ? dat_iVoted : reg1001_qVoted;
    assign psdelaylum = reg1001_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1001_q <= 8'h00;
        else
            reg1001_q <= reg1001_d;

`ifdef SIM
    initial
        reg1001_q = $urandom;
`endif



    // Register: psCntr1 address:1002
    wire reg1002_select = wb_adr_i == 10'h3ea;
    reg [7:0] reg1002_q;
    wire [7:0] reg1002_qVoted = reg1002_q;
    wire [7:0] reg1002_d = wb_we && reg1002_select ? dat_iVoted : reg1002_qVoted;
    assign pscntr1 = reg1002_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1002_q <= 8'hfc;
        else
            reg1002_q <= reg1002_d;

`ifdef SIM
    initial
        reg1002_q = $urandom;
`endif



    // Register: psCntr2 address:1003
    wire reg1003_select = wb_adr_i == 10'h3eb;
    reg [7:0] reg1003_q;
    wire [7:0] reg1003_qVoted = reg1003_q;
    wire [7:0] reg1003_d = wb_we && reg1003_select ? dat_iVoted : reg1003_qVoted;
    assign pscntr2 = reg1003_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1003_q <= 8'h4f;
        else
            reg1003_q <= reg1003_d;

`ifdef SIM
    initial
        reg1003_q = $urandom;
`endif



    // Register: enTestPadsConf1 address:1004
    wire reg1004_select = wb_adr_i == 10'h3ec;
    reg [7:0] reg1004_q;
    wire [7:0] reg1004_qVoted = reg1004_q;
    wire [7:0] reg1004_d = wb_we && reg1004_select ? dat_iVoted : reg1004_qVoted;
    assign entestpadsconf1 = reg1004_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1004_q <= 8'h0c;
        else
            reg1004_q <= reg1004_d;

`ifdef SIM
    initial
        reg1004_q = $urandom;
`endif



    // Register: enTestPadsConf2 address:1005
    wire reg1005_select = wb_adr_i == 10'h3ed;
    reg [7:0] reg1005_q;
    wire [7:0] reg1005_qVoted = reg1005_q;
    wire [7:0] reg1005_d = wb_we && reg1005_select ? dat_iVoted : reg1005_qVoted;
    assign entestpadsconf2 = reg1005_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1005_q <= 8'h00;
        else
            reg1005_q <= reg1005_d;

`ifdef SIM
    initial
        reg1005_q = $urandom;
`endif



    // Register: GLOBAL_EXTCLOCK address:1006
    wire reg1006_select = wb_adr_i == 10'h3ee;
    reg [7:0] reg1006_q;
    wire [7:0] reg1006_qVoted = reg1006_q;
    wire [7:0] reg1006_d = wb_we && reg1006_select ? dat_iVoted : reg1006_qVoted;
    assign global_extclock = reg1006_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1006_q <= 8'h00;
        else
            reg1006_q <= reg1006_d;

`ifdef SIM
    initial
        reg1006_q = $urandom;
`endif



    // Register: clkTestPadsConf address:1007
    wire reg1007_select = wb_adr_i == 10'h3ef;
    reg [7:0] reg1007_q;
    wire [7:0] reg1007_qVoted = reg1007_q;
    wire [7:0] reg1007_d = wb_we && reg1007_select ? dat_iVoted : reg1007_qVoted;
    assign clktestpadsconf = reg1007_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1007_q <= 8'h00;
        else
            reg1007_q <= reg1007_d;

`ifdef SIM
    initial
        reg1007_q = $urandom;
`endif



    // Register: probeDigTestPadsConf address:1008
    wire reg1008_select = wb_adr_i == 10'h3f0;
    reg [7:0] reg1008_q;
    wire [7:0] reg1008_qVoted = reg1008_q;
    wire [7:0] reg1008_d = wb_we && reg1008_select ? dat_iVoted : reg1008_qVoted;
    assign probedigtestpadsconf = reg1008_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1008_q <= 8'h00;
        else
            reg1008_q <= reg1008_d;

`ifdef SIM
    initial
        reg1008_q = $urandom;
`endif



    // Register: CONF_FCCU_TRIGID_L address:1009
    wire reg1009_select = wb_adr_i == 10'h3f1;
    reg [7:0] reg1009_q;
    wire [7:0] reg1009_qVoted = reg1009_q;
    wire [7:0] reg1009_d = wb_we && reg1009_select ? dat_iVoted : reg1009_qVoted;
    assign conf_fccu_trigid_l = reg1009_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1009_q <= 8'h00;
        else
            reg1009_q <= reg1009_d;

`ifdef SIM
    initial
        reg1009_q = $urandom;
`endif



    // Register: CONF_FCCU_TRIGID_H address:1010
    wire reg1010_select = wb_adr_i == 10'h3f2;
    reg [7:0] reg1010_q;
    wire [7:0] reg1010_qVoted = reg1010_q;
    wire [7:0] reg1010_d = wb_we && reg1010_select ? dat_iVoted : reg1010_qVoted;
    assign conf_fccu_trigid_h = reg1010_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1010_q <= 8'h00;
        else
            reg1010_q <= reg1010_d;

`ifdef SIM
    initial
        reg1010_q = $urandom;
`endif



    // Register: fccuCntrConf address:1011
    wire reg1011_select = wb_adr_i == 10'h3f3;
    reg [7:0] reg1011_q;
    wire [7:0] reg1011_qVoted = reg1011_q;
    wire [7:0] reg1011_d = wb_we && reg1011_select ? dat_iVoted : reg1011_qVoted;
    assign fccucntrconf = reg1011_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1011_q <= 8'h18;
        else
            reg1011_q <= reg1011_d;

`ifdef SIM
    initial
        reg1011_q = $urandom;
`endif



    // Register: cmdCalGenConf1 address:1012
    wire reg1012_select = wb_adr_i == 10'h3f4;
    reg [7:0] reg1012_q;
    wire [7:0] reg1012_qVoted = reg1012_q;
    wire [7:0] reg1012_d = wb_we && reg1012_select ? dat_iVoted : reg1012_qVoted;
    assign cmdcalgenconf1 = reg1012_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1012_q <= 8'h00;
        else
            reg1012_q <= reg1012_d;

`ifdef SIM
    initial
        reg1012_q = $urandom;
`endif



    // Register: cmdCalGenConf2 address:1013
    wire reg1013_select = wb_adr_i == 10'h3f5;
    reg [7:0] reg1013_q;
    wire [7:0] reg1013_qVoted = reg1013_q;
    wire [7:0] reg1013_d = wb_we && reg1013_select ? dat_iVoted : reg1013_qVoted;
    assign cmdcalgenconf2 = reg1013_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1013_q <= 8'h00;
        else
            reg1013_q <= reg1013_d;

`ifdef SIM
    initial
        reg1013_q = $urandom;
`endif



    // Register: cmdCalGenConf3 address:1014
    wire reg1014_select = wb_adr_i == 10'h3f6;
    reg [7:0] reg1014_q;
    wire [7:0] reg1014_qVoted = reg1014_q;
    wire [7:0] reg1014_d = wb_we && reg1014_select ? dat_iVoted : reg1014_qVoted;
    assign cmdcalgenconf3 = reg1014_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1014_q <= 8'h08;
        else
            reg1014_q <= reg1014_d;

`ifdef SIM
    initial
        reg1014_q = $urandom;
`endif



    // Register: for log
    wire reg1023_select = wb_adr_i == 10'h3ff;
    reg [7:0] reg1023_q;
    wire [7:0] reg1023_qVoted = reg1023_q;
    wire [7:0] reg1023_d = wb_we && reg1023_select ? dat_iVoted : reg1023_qVoted;
    assign logRegister = reg1023_qVoted[7:0];
    always @(posedge clk_wb or posedge wb_rst)
        if (wb_rst)
            reg1023_q <= date;
        else
            reg1023_q <= reg1023_d;

`ifdef SIM
    initial
        reg1023_q = $urandom;
`endif



    reg wb_ack_q;
    wire wb_ack_qVoted = wb_ack_q;
    always @(posedge clk_wb or posedge wb_rst) begin
        if(wb_rst)
            wb_ack_q <= 1'b0;
        else if(wb_stb_iVoted)
            wb_ack_q <= 1'b1;
        else
            wb_ack_q <= 1'b0;
    end
    assign wb_ack_o = wb_ack_qVoted;

    // Readout multiplexer
    reg [7:0] data_read_mux;
    always @(*)
        case(wb_adr_i)
            0: data_read_mux = reg0_qVoted;
            1: data_read_mux = reg1_qVoted;
            2: data_read_mux = reg2_qVoted;
            3: data_read_mux = reg3_qVoted;
            4: data_read_mux = reg4_qVoted;
            5: data_read_mux = reg5_qVoted;
            6: data_read_mux = reg6_qVoted;
            7: data_read_mux = reg7_qVoted;
            8: data_read_mux = reg8_qVoted;
            9: data_read_mux = reg9_qVoted;
            10: data_read_mux = reg10_qVoted;
            11: data_read_mux = reg11_qVoted;
            12: data_read_mux = reg12_qVoted;
            13: data_read_mux = reg13_qVoted;
            14: data_read_mux = reg14_qVoted;
            15: data_read_mux = reg15_qVoted;
            16: data_read_mux = reg16_qVoted;
            17: data_read_mux = reg17_qVoted;
            18: data_read_mux = reg18_qVoted;
            19: data_read_mux = reg19_qVoted;
            20: data_read_mux = reg20_qVoted;
            21: data_read_mux = reg21_qVoted;
            22: data_read_mux = reg22_qVoted;
            23: data_read_mux = reg23_qVoted;
            24: data_read_mux = reg24_qVoted;
            25: data_read_mux = reg25_qVoted;
            26: data_read_mux = reg26_qVoted;
            27: data_read_mux = reg27_qVoted;
            28: data_read_mux = reg28_qVoted;
            29: data_read_mux = reg29_qVoted;
            30: data_read_mux = reg30_qVoted;
            31: data_read_mux = reg31_qVoted;
            32: data_read_mux = reg32_qVoted;
            33: data_read_mux = reg33_qVoted;
            34: data_read_mux = reg34_qVoted;
            35: data_read_mux = reg35_qVoted;
            36: data_read_mux = reg36_qVoted;
            37: data_read_mux = reg37_qVoted;
            38: data_read_mux = reg38_qVoted;
            39: data_read_mux = reg39_qVoted;
            40: data_read_mux = reg40_qVoted;
            41: data_read_mux = reg41_qVoted;
            42: data_read_mux = reg42_qVoted;
            43: data_read_mux = reg43_qVoted;
            44: data_read_mux = reg44_qVoted;
            45: data_read_mux = reg45_qVoted;
            46: data_read_mux = reg46_qVoted;
            47: data_read_mux = reg47_qVoted;
            48: data_read_mux = reg48_qVoted;
            49: data_read_mux = reg49_qVoted;
            50: data_read_mux = reg50_qVoted;
            51: data_read_mux = reg51_qVoted;
            52: data_read_mux = reg52_qVoted;
            53: data_read_mux = reg53_qVoted;
            54: data_read_mux = reg54_qVoted;
            55: data_read_mux = reg55_qVoted;
            56: data_read_mux = reg56_qVoted;
            57: data_read_mux = reg57_qVoted;
            58: data_read_mux = reg58_qVoted;
            59: data_read_mux = reg59_qVoted;
            60: data_read_mux = reg60_qVoted;
            61: data_read_mux = reg61_qVoted;
            62: data_read_mux = reg62_qVoted;
            63: data_read_mux = reg63_qVoted;
            120: data_read_mux = reg120_qVoted;
            121: data_read_mux = reg121_qVoted;
            122: data_read_mux = reg122_qVoted;
            123: data_read_mux = reg123_qVoted;
            180: data_read_mux = reg180_qVoted;
            181: data_read_mux = reg181_qVoted;
            182: data_read_mux = reg182_qVoted;
            183: data_read_mux = reg183_qVoted;
            240: data_read_mux = reg240_qVoted;
            241: data_read_mux = reg241_qVoted;
            242: data_read_mux = reg242_qVoted;
            243: data_read_mux = reg243_qVoted;
            300: data_read_mux = reg300_qVoted;
            301: data_read_mux = reg301_qVoted;
            302: data_read_mux = reg302_qVoted;
            303: data_read_mux = reg303_qVoted;
            360: data_read_mux = reg360_qVoted;
            361: data_read_mux = reg361_qVoted;
            362: data_read_mux = reg362_qVoted;
            363: data_read_mux = reg363_qVoted;
            420: data_read_mux = reg420_qVoted;
            421: data_read_mux = reg421_qVoted;
            422: data_read_mux = reg422_qVoted;
            423: data_read_mux = reg423_qVoted;
            480: data_read_mux = reg480_qVoted;
            481: data_read_mux = reg481_qVoted;
            482: data_read_mux = reg482_qVoted;
            483: data_read_mux = reg483_qVoted;
            540: data_read_mux = reg540_qVoted;
            541: data_read_mux = reg541_qVoted;
            542: data_read_mux = reg542_qVoted;
            543: data_read_mux = reg543_qVoted;
            600: data_read_mux = reg600_qVoted;
            601: data_read_mux = reg601_qVoted;
            602: data_read_mux = reg602_qVoted;
            603: data_read_mux = reg603_qVoted;
            660: data_read_mux = reg660_qVoted;
            661: data_read_mux = reg661_qVoted;
            662: data_read_mux = reg662_qVoted;
            663: data_read_mux = reg663_qVoted;
            720: data_read_mux = reg720_qVoted;
            721: data_read_mux = reg721_qVoted;
            722: data_read_mux = reg722_qVoted;
            723: data_read_mux = reg723_qVoted;
            780: data_read_mux = reg780_qVoted;
            781: data_read_mux = reg781_qVoted;
            782: data_read_mux = reg782_qVoted;
            783: data_read_mux = reg783_qVoted;
            840: data_read_mux = reg840_qVoted;
            841: data_read_mux = reg841_qVoted;
            842: data_read_mux = reg842_qVoted;
            843: data_read_mux = reg843_qVoted;
            904: data_read_mux = reg904_qVoted;
            905: data_read_mux = reg905_qVoted;
            906: data_read_mux = reg906_qVoted;
            907: data_read_mux = reg907_qVoted;
            908: data_read_mux = reg908_qVoted;
            912: data_read_mux = reg912_qVoted;
            913: data_read_mux = reg913_qVoted;
            914: data_read_mux = reg914_qVoted;
            915: data_read_mux = reg915_qVoted;
            916: data_read_mux = reg916_qVoted;
            960: data_read_mux = reg960_qVoted;
            961: data_read_mux = reg961_qVoted;
            962: data_read_mux = reg962_qVoted;
            963: data_read_mux = reg963_qVoted;
            964: data_read_mux = reg964_qVoted;
            965: data_read_mux = reg965_qVoted;
            966: data_read_mux = reg966_qVoted;
            967: data_read_mux = reg967_qVoted;
            968: data_read_mux = reg968_qVoted;
            969: data_read_mux = reg969_qVoted;
            970: data_read_mux = reg970_qVoted;
            971: data_read_mux = reg971_qVoted;
            972: data_read_mux = reg972_qVoted;
            973: data_read_mux = reg973_qVoted;
            974: data_read_mux = reg974_qVoted;
            975: data_read_mux = reg975_qVoted;
            976: data_read_mux = reg976_qVoted;
            977: data_read_mux = reg977_qVoted;
            978: data_read_mux = reg978_qVoted;
            979: data_read_mux = reg979_qVoted;
            980: data_read_mux = reg980_qVoted;
            981: data_read_mux = reg981_qVoted;
            982: data_read_mux = reg982_qVoted;
            983: data_read_mux = reg983_qVoted;
            984: data_read_mux = reg984_qVoted;
            985: data_read_mux = reg985_qVoted;
            986: data_read_mux = reg986_qVoted;
            992: data_read_mux = reg992_qVoted;
            993: data_read_mux = reg993_qVoted;
            994: data_read_mux = reg994_qVoted;
            995: data_read_mux = reg995_qVoted;
            996: data_read_mux = reg996_qVoted;
            997: data_read_mux = reg997_qVoted;
            998: data_read_mux = reg998_qVoted;
            999: data_read_mux = reg999_qVoted;
            1000: data_read_mux = reg1000_qVoted;
            1001: data_read_mux = reg1001_qVoted;
            1002: data_read_mux = reg1002_qVoted;
            1003: data_read_mux = reg1003_qVoted;
            1004: data_read_mux = reg1004_qVoted;
            1005: data_read_mux = reg1005_qVoted;
            1006: data_read_mux = reg1006_qVoted;
            1007: data_read_mux = reg1007_qVoted;
            1008: data_read_mux = reg1008_qVoted;
            1009: data_read_mux = reg1009_qVoted;
            1010: data_read_mux = reg1010_qVoted;
            1011: data_read_mux = reg1011_qVoted;
            1012: data_read_mux = reg1012_qVoted;
            1013: data_read_mux = reg1013_qVoted;
            1014: data_read_mux = reg1014_qVoted;
            1023: data_read_mux = reg1023_qVoted;
            default: data_read_mux = 8'h0;
        endcase
    assign wb_dat_o = data_read_mux;
endmodule
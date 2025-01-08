`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company:  NJU && IHEP
// Engineer: 
// 
// Create Date: 2022/12/01 10:28:14
// Design Name: altiroc_emulator
// Module Name: top
// Project Name: altiroc_emulator
// Target Devices: Spartan-7s15-196-2
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

module top #(
    parameter       CLK_FREQ = 40,
    parameter       DATE = 8'h00
)(
    input           LPGBT_HARD_RSTB,  // From lpGBT GPIO
    input           LPGBT_CLK40M_P,   // 40MHz from lpGBT ECLK
    input           LPGBT_CLK40M_N,
    input           FAST_CMD_P,       // From Timing lpGBT Elink
    input           FAST_CMD_N,
    output  [1:0]   TIMING_DOUT_P,    // To Timing lpGBT Elink
    output  [1:0]   TIMING_DOUT_N,
    output  [1:0]   LUMI_DOUT_P,      // To Lumi lpGBT Elink
    output  [1:0]   LUMI_DOUT_N,
    input   [3:1]   I2C_ADDR,         // Config by PEB
    input           I2C_SCL,          // From Timing lpGBT I2C master
    inout           I2C_SDA,
    // Test
    input   [2:0]   DIPSW,            // Switch SW1
    inout   [1:0]   TESTPIN,          // Connector J1
    output  [2:1]   TP,               
    input           REFCLK_P,         // Local OSC, 200MHz
    input           REFCLK_N
);

//-------------------slow control for chi0-------------------
    wire [7:0] confpix0reg0_0;
    wire [7:0] confpix0reg1_0;
    wire [7:0] confpix0reg2_0;
    wire [7:0] confpix0reg3_0;
    wire [7:0] confpix1reg0_0;
    wire [7:0] confpix1reg1_0;
    wire [7:0] confpix1reg2_0;
    wire [7:0] confpix1reg3_0;
    wire [7:0] confpix2reg0_0;
    wire [7:0] confpix2reg1_0;
    wire [7:0] confpix2reg2_0;
    wire [7:0] confpix2reg3_0;
    wire [7:0] confpix3reg0_0;
    wire [7:0] confpix3reg1_0;
    wire [7:0] confpix3reg2_0;
    wire [7:0] confpix3reg3_0;
    wire [7:0] confpix4reg0_0;
    wire [7:0] confpix4reg1_0;
    wire [7:0] confpix4reg2_0;
    wire [7:0] confpix4reg3_0;
    wire [7:0] confpix5reg0_0;
    wire [7:0] confpix5reg1_0;
    wire [7:0] confpix5reg2_0;
    wire [7:0] confpix5reg3_0;
    wire [7:0] confpix6reg0_0;
    wire [7:0] confpix6reg1_0;
    wire [7:0] confpix6reg2_0;
    wire [7:0] confpix6reg3_0;
    wire [7:0] confpix7reg0_0;
    wire [7:0] confpix7reg1_0;
    wire [7:0] confpix7reg2_0;
    wire [7:0] confpix7reg3_0;
    wire [7:0] confpix8reg0_0;
    wire [7:0] confpix8reg1_0;
    wire [7:0] confpix8reg2_0;
    wire [7:0] confpix8reg3_0;
    wire [7:0] confpix9reg0_0;
    wire [7:0] confpix9reg1_0;
    wire [7:0] confpix9reg2_0;
    wire [7:0] confpix9reg3_0;
    wire [7:0] confpix10reg0_0;
    wire [7:0] confpix10reg1_0;
    wire [7:0] confpix10reg2_0;
    wire [7:0] confpix10reg3_0;
    wire [7:0] confpix11reg0_0;
    wire [7:0] confpix11reg1_0;
    wire [7:0] confpix11reg2_0;
    wire [7:0] confpix11reg3_0;
    wire [7:0] confpix12reg0_0;
    wire [7:0] confpix12reg1_0;
    wire [7:0] confpix12reg2_0;
    wire [7:0] confpix12reg3_0;
    wire [7:0] confpix13reg0_0;
    wire [7:0] confpix13reg1_0;
    wire [7:0] confpix13reg2_0;
    wire [7:0] confpix13reg3_0;
    wire [7:0] confpix14reg0_0;
    wire [7:0] confpix14reg1_0;
    wire [7:0] confpix14reg2_0;
    wire [7:0] confpix14reg3_0;
    wire [7:0] confpix15reg0_0;
    wire [7:0] confpix15reg1_0;
    wire [7:0] confpix15reg2_0;
    wire [7:0] confpix15reg3_0;
    wire [7:0] confpix30reg0_0;
    wire [7:0] confpix30reg1_0;
    wire [7:0] confpix30reg2_0;
    wire [7:0] confpix30reg3_0;
    wire [7:0] confpix45reg0_0;
    wire [7:0] confpix45reg1_0;
    wire [7:0] confpix45reg2_0;
    wire [7:0] confpix45reg3_0;
    wire [7:0] confpix60reg0_0;
    wire [7:0] confpix60reg1_0;
    wire [7:0] confpix60reg2_0;
    wire [7:0] confpix60reg3_0;
    wire [7:0] confpix75reg0_0;
    wire [7:0] confpix75reg1_0;
    wire [7:0] confpix75reg2_0;
    wire [7:0] confpix75reg3_0;
    wire [7:0] confpix90reg0_0;
    wire [7:0] confpix90reg1_0;
    wire [7:0] confpix90reg2_0;
    wire [7:0] confpix90reg3_0;
    wire [7:0] confpix105reg0_0;
    wire [7:0] confpix105reg1_0;
    wire [7:0] confpix105reg2_0;
    wire [7:0] confpix105reg3_0;
    wire [7:0] confpix120reg0_0;
    wire [7:0] confpix120reg1_0;
    wire [7:0] confpix120reg2_0;
    wire [7:0] confpix120reg3_0;
    wire [7:0] confpix135reg0_0;
    wire [7:0] confpix135reg1_0;
    wire [7:0] confpix135reg2_0;
    wire [7:0] confpix135reg3_0;
    wire [7:0] confpix150reg0_0;
    wire [7:0] confpix150reg1_0;
    wire [7:0] confpix150reg2_0;
    wire [7:0] confpix150reg3_0;
    wire [7:0] confpix165reg0_0;
    wire [7:0] confpix165reg1_0;
    wire [7:0] confpix165reg2_0;
    wire [7:0] confpix165reg3_0;
    wire [7:0] confpix180reg0_0;
    wire [7:0] confpix180reg1_0;
    wire [7:0] confpix180reg2_0;
    wire [7:0] confpix180reg3_0;
    wire [7:0] confpix195reg0_0;
    wire [7:0] confpix195reg1_0;
    wire [7:0] confpix195reg2_0;
    wire [7:0] confpix195reg3_0;
    wire [7:0] confpix210reg0_0;
    wire [7:0] confpix210reg1_0;
    wire [7:0] confpix210reg2_0;
    wire [7:0] confpix210reg3_0;
    wire [7:0] confldpuiniwin1l_0;
    wire [7:0] confldpuiniwin1h_0;
    wire [7:0] confldpuiniwin2l_0;
    wire [7:0] confldpuiniwin2h_0;
    wire [7:0] conf_ldpu_cntrl_0;
    wire [7:0] conftdpulatencyl_0;
    wire [7:0] conftdpulatencyh_0;
    wire [7:0] conf_tdpu_cntrl_0;
    wire [7:0] conf_tdpu_pattern_0;
    wire [7:0] conf_tdpu_ocupref_0;
    wire [7:0] dacrpgconf2_0;
    wire [7:0] dacrpgconf1_0;
    wire [7:0] bias_ch_sel_pulser_0;
    wire [7:0] bias_ch_dac_pa_0;
    wire [7:0] bias_ch_dac_dc_pa_0;
    wire [7:0] dac10bconf1_0;
    wire [7:0] dac10bconf2_0;
    wire [7:0] pixeladdr_0;
    wire [7:0] dll_120p_toa_cbit_0;
    wire [7:0] dll_120p_toa_cp_0;
    wire [7:0] dll_120p_toa_comp_0;
    wire [7:0] dll_120p_tot_cbit_0;
    wire [7:0] dll_120p_tot_cp_0;
    wire [7:0] dll_120p_tot_comp_0;
    wire [7:0] dll_140p_toa_cbit_0;
    wire [7:0] dll_140p_toa_cp_0;
    wire [7:0] dll_140p_toa_comp_0;
    wire [7:0] dllcntrconf_0;
    wire [7:0] selprobebiasconf_0;
    wire [7:0] confglobalenprobe_0;
    wire [7:0] confglobalsignaltdcs_0;
    wire [7:0] confglobalsignalrincdcp_0;
    wire [7:0] conf_global_cntr_0;
    wire [7:0] conf_global_occupancy_0;
    wire [7:0] enablecgeocl_0;
    wire [7:0] enablecgeoch_0;
    wire [7:0] conf_anaperi_selprobemon_0;
    wire [7:0] bgconf_0;
    wire [7:0] pllcpconf_0;
    wire [7:0] pllbwconf_0;
    wire [7:0] pllcntr1_0;
    wire [7:0] pllcntr2_0;
    wire [7:0] conf_anaperi_plllocksamples_0;
    wire [7:0] conf_anaperi_0;
    wire [7:0] psdelay1_0;
    wire [7:0] psdelay2_0;
    wire [7:0] psdelaylum_0;
    wire [7:0] pscntr1_0;
    wire [7:0] pscntr2_0;
    wire [7:0] entestpadsconf1_0;
    wire [7:0] entestpadsconf2_0;
    wire [7:0] global_extclock_0;
    wire [7:0] clktestpadsconf_0;
    wire [7:0] probedigtestpadsconf_0;
    wire [7:0] conf_fccu_trigid_l_0;
    wire [7:0] conf_fccu_trigid_h_0;
    wire [7:0] fccucntrconf_0;
    wire [7:0] cmdcalgenconf1_0;
    wire [7:0] cmdcalgenconf2_0;
    wire [7:0] cmdcalgenconf3_0;
    wire [7:0] logRegister_0; 

    wire [1:0] type;
    wire [9:0] vth;
    wire [231:0] vthc;
    wire [28:0] pixelOn;  
    wire [1:0] txRate;
    wire en_TDPU;
    wire [7:0] frameData;
    wire en8b10b;

//-------------------slow control for chi1-------------------
    wire [7:0] confpix0reg0_1;
    wire [7:0] confpix0reg1_1;
    wire [7:0] confpix0reg2_1;
    wire [7:0] confpix0reg3_1;
    wire [7:0] confpix1reg0_1;
    wire [7:0] confpix1reg1_1;
    wire [7:0] confpix1reg2_1;
    wire [7:0] confpix1reg3_1;
    wire [7:0] confpix2reg0_1;
    wire [7:0] confpix2reg1_1;
    wire [7:0] confpix2reg2_1;
    wire [7:0] confpix2reg3_1;
    wire [7:0] confpix3reg0_1;
    wire [7:0] confpix3reg1_1;
    wire [7:0] confpix3reg2_1;
    wire [7:0] confpix3reg3_1;
    wire [7:0] confpix4reg0_1;
    wire [7:0] confpix4reg1_1;
    wire [7:0] confpix4reg2_1;
    wire [7:0] confpix4reg3_1;
    wire [7:0] confpix5reg0_1;
    wire [7:0] confpix5reg1_1;
    wire [7:0] confpix5reg2_1;
    wire [7:0] confpix5reg3_1;
    wire [7:0] confpix6reg0_1;
    wire [7:0] confpix6reg1_1;
    wire [7:0] confpix6reg2_1;
    wire [7:0] confpix6reg3_1;
    wire [7:0] confpix7reg0_1;
    wire [7:0] confpix7reg1_1;
    wire [7:0] confpix7reg2_1;
    wire [7:0] confpix7reg3_1;
    wire [7:0] confpix8reg0_1;
    wire [7:0] confpix8reg1_1;
    wire [7:0] confpix8reg2_1;
    wire [7:0] confpix8reg3_1;
    wire [7:0] confpix9reg0_1;
    wire [7:0] confpix9reg1_1;
    wire [7:0] confpix9reg2_1;
    wire [7:0] confpix9reg3_1;
    wire [7:0] confpix10reg0_1;
    wire [7:0] confpix10reg1_1;
    wire [7:0] confpix10reg2_1;
    wire [7:0] confpix10reg3_1;
    wire [7:0] confpix11reg0_1;
    wire [7:0] confpix11reg1_1;
    wire [7:0] confpix11reg2_1;
    wire [7:0] confpix11reg3_1;
    wire [7:0] confpix12reg0_1;
    wire [7:0] confpix12reg1_1;
    wire [7:0] confpix12reg2_1;
    wire [7:0] confpix12reg3_1;
    wire [7:0] confpix13reg0_1;
    wire [7:0] confpix13reg1_1;
    wire [7:0] confpix13reg2_1;
    wire [7:0] confpix13reg3_1;
    wire [7:0] confpix14reg0_1;
    wire [7:0] confpix14reg1_1;
    wire [7:0] confpix14reg2_1;
    wire [7:0] confpix14reg3_1;
    wire [7:0] confpix15reg0_1;
    wire [7:0] confpix15reg1_1;
    wire [7:0] confpix15reg2_1;
    wire [7:0] confpix15reg3_1;
    wire [7:0] confpix30reg0_1;
    wire [7:0] confpix30reg1_1;
    wire [7:0] confpix30reg2_1;
    wire [7:0] confpix30reg3_1;
    wire [7:0] confpix45reg0_1;
    wire [7:0] confpix45reg1_1;
    wire [7:0] confpix45reg2_1;
    wire [7:0] confpix45reg3_1;
    wire [7:0] confpix60reg0_1;
    wire [7:0] confpix60reg1_1;
    wire [7:0] confpix60reg2_1;
    wire [7:0] confpix60reg3_1;
    wire [7:0] confpix75reg0_1;
    wire [7:0] confpix75reg1_1;
    wire [7:0] confpix75reg2_1;
    wire [7:0] confpix75reg3_1;
    wire [7:0] confpix90reg0_1;
    wire [7:0] confpix90reg1_1;
    wire [7:0] confpix90reg2_1;
    wire [7:0] confpix90reg3_1;
    wire [7:0] confpix105reg0_1;
    wire [7:0] confpix105reg1_1;
    wire [7:0] confpix105reg2_1;
    wire [7:0] confpix105reg3_1;
    wire [7:0] confpix120reg0_1;
    wire [7:0] confpix120reg1_1;
    wire [7:0] confpix120reg2_1;
    wire [7:0] confpix120reg3_1;
    wire [7:0] confpix135reg0_1;
    wire [7:0] confpix135reg1_1;
    wire [7:0] confpix135reg2_1;
    wire [7:0] confpix135reg3_1;
    wire [7:0] confpix150reg0_1;
    wire [7:0] confpix150reg1_1;
    wire [7:0] confpix150reg2_1;
    wire [7:0] confpix150reg3_1;
    wire [7:0] confpix165reg0_1;
    wire [7:0] confpix165reg1_1;
    wire [7:0] confpix165reg2_1;
    wire [7:0] confpix165reg3_1;
    wire [7:0] confpix180reg0_1;
    wire [7:0] confpix180reg1_1;
    wire [7:0] confpix180reg2_1;
    wire [7:0] confpix180reg3_1;
    wire [7:0] confpix195reg0_1;
    wire [7:0] confpix195reg1_1;
    wire [7:0] confpix195reg2_1;
    wire [7:0] confpix195reg3_1;
    wire [7:0] confpix210reg0_1;
    wire [7:0] confpix210reg1_1;
    wire [7:0] confpix210reg2_1;
    wire [7:0] confpix210reg3_1;
    wire [7:0] confldpuiniwin1l_1;
    wire [7:0] confldpuiniwin1h_1;
    wire [7:0] confldpuiniwin2l_1;
    wire [7:0] confldpuiniwin2h_1;
    wire [7:0] conf_ldpu_cntrl_1;
    wire [7:0] conftdpulatencyl_1;
    wire [7:0] conftdpulatencyh_1;
    wire [7:0] conf_tdpu_cntrl_1;
    wire [7:0] conf_tdpu_pattern_1;
    wire [7:0] conf_tdpu_ocupref_1;
    wire [7:0] dacrpgconf2_1;
    wire [7:0] dacrpgconf1_1;
    wire [7:0] bias_ch_sel_pulser_1;
    wire [7:0] bias_ch_dac_pa_1;
    wire [7:0] bias_ch_dac_dc_pa_1;
    wire [7:0] dac10bconf1_1;
    wire [7:0] dac10bconf2_1;
    wire [7:0] pixeladdr_1;
    wire [7:0] dll_120p_toa_cbit_1;
    wire [7:0] dll_120p_toa_cp_1;
    wire [7:0] dll_120p_toa_comp_1;
    wire [7:0] dll_120p_tot_cbit_1;
    wire [7:0] dll_120p_tot_cp_1;
    wire [7:0] dll_120p_tot_comp_1;
    wire [7:0] dll_140p_toa_cbit_1;
    wire [7:0] dll_140p_toa_cp_1;
    wire [7:0] dll_140p_toa_comp_1;
    wire [7:0] dllcntrconf_1;
    wire [7:0] selprobebiasconf_1;
    wire [7:0] confglobalenprobe_1;
    wire [7:0] confglobalsignaltdcs_1;
    wire [7:0] confglobalsignalrincdcp_1;
    wire [7:0] conf_global_cntr_1;
    wire [7:0] conf_global_occupancy_1;
    wire [7:0] enablecgeocl_1;
    wire [7:0] enablecgeoch_1;
    wire [7:0] conf_anaperi_selprobemon_1;
    wire [7:0] bgconf_1;
    wire [7:0] pllcpconf_1;
    wire [7:0] pllbwconf_1;
    wire [7:0] pllcntr1_1;
    wire [7:0] pllcntr2_1;
    wire [7:0] conf_anaperi_plllocksamples_1;
    wire [7:0] conf_anaperi_1;
    wire [7:0] psdelay1_1;
    wire [7:0] psdelay2_1;
    wire [7:0] psdelaylum_1;
    wire [7:0] pscntr1_1;
    wire [7:0] pscntr2_1;
    wire [7:0] entestpadsconf1_1;
    wire [7:0] entestpadsconf2_1;
    wire [7:0] global_extclock_1;
    wire [7:0] clktestpadsconf_1;
    wire [7:0] probedigtestpadsconf_1;
    wire [7:0] conf_fccu_trigid_l_1;
    wire [7:0] conf_fccu_trigid_h_1;
    wire [7:0] fccucntrconf_1;
    wire [7:0] cmdcalgenconf1_1;
    wire [7:0] cmdcalgenconf2_1;
    wire [7:0] cmdcalgenconf3_1;
    wire [7:0] logRegister_1;

    wire [1:0] type_1;
    wire [9:0] vth_1;
    wire [231:0] vthc_1;
    wire [28:0] pixelOn_1;  
    wire  [1:0] txRate_1;
    wire en_TDPU_1;
    wire [7:0] frameData_1;
    wire en8b10b_1;
    //fast command
    wire trigger, bcr, cal, gbrst, settrigid, synclumi, fastcmd_locked;
    wire [11:0] trigid;

    //clocks
    wire clk200_in, clk200; 
    wire clk40_in, clk40;   
    reg SSTEP;
    wire clk80,clk160,clk320,clk640;
    wire clk_seri,clk_para;
    wire locked;
    wire rst;
    wire rst_i2c;
  
    //clk200M clocks from board    
    IBUFDS IBUFDS_clk200 (
        .O          (clk200_in),
        .I          (REFCLK_P),
        .IB         (REFCLK_N)
    );
    BUFG BUFG_clk200 (
        .O          (clk200),
        .I          (clk200_in)
    );
    //clk40M clocks from board  
 
    IBUFDS IBUFDS_clk40 (
        .O          (clk40_in),
        .I          (LPGBT_CLK40M_P),
        .IB         (LPGBT_CLK40M_N)
    );
    BUFG BUFG_clk40 (
        .O          (clk40),
        .I          (clk40_in)
    );

//--------------------------fast-cmd----------------------

  fastcmd_decoder fastCMD(
    .reset(rst),
    .clk160(clk160),
    .clk200(clk200), 
    .FAST_CMD_P(FAST_CMD_P),
    .FAST_CMD_N(FAST_CMD_N),
    .trigger_o(trigger),
    .bcr_o(bcr),
    .cal_o(cal),
    .gbrst_o(gbrst),
    .settrigid_o(settrigid),
    .synclumi_o(synclumi),
    .trigid_o(trigid),
    .locked_o(fastcmd_locked)
  );
  
//-------------------clk generator-------------------
    reg [1:0] txRate_r;
    always @(posedge clk40) begin
        txRate_r <= txRate;
    end

    wire xor1,xor0;
    assign xor1 = txRate[1]^txRate_r[1];
    assign xor0 = txRate[0]^txRate_r[0];

    always @(posedge clk40) begin
        SSTEP <= xor1 | xor0;
    end   

    mmcme2 clk_gen
    (
        .SSTEP(SSTEP),
        .STATE(txRate),
        .RST(!LPGBT_HARD_RSTB),
        .CLKIN(clk40),
        .SRDY(),
        .LOCKED_OUT(locked),
        .CLK0OUT(clk80),
        .CLK1OUT(clk160),
        .CLK2OUT(clk320),
        .CLK3OUT(clk_seri),
        .CLK4OUT(clk_para),
        .CLK5OUT(clk640),
        .CLK6OUT()
    );

    assign rst = !locked;
    assign rst_i2c = !LPGBT_HARD_RSTB;

//-------------------chip0 data generator------------------
  assign type = conf_tdpu_cntrl_0[3:2];
  assign vth = dac10bconf2_0[2]? {dac10bconf2_0[1:0],dac10bconf1_0} : 10'b0;
  assign txRate = conf_tdpu_cntrl_0[1:0];
  assign en_TDPU = conf_tdpu_cntrl_0[5];
  assign frameData = conf_tdpu_pattern_0;
  assign en8b10b = conf_tdpu_cntrl_0[4]; 

  wire CharIsK;
  wire [7:0] data_to_code;
  timingSource timingData(
    .type(type),
    .en_TDPU(en_TDPU),
    .trigger(trigger),
    .reset(rst),
    .clk40(clk40),
    .clk160(clk160),
    .clk_S(clk80),  
    .dataclk(clk_para), 
    .vth(vth),
    .vthc(vthc),
    .pixelOn(pixelOn),
    .CharIsK(CharIsK),
    .frameData(frameData),
    .data_to_code(data_to_code)
      );

  wire [9:0] data_to_ser;
  enc_8b10b timingEncode( 
    .reset(rst),
    .clk(clk_para),
    .ena(en8b10b),
    .KI(CharIsK),
    .datain(data_to_code),
    .dataout(data_to_ser)
    ); 

    oserdesData10b timingSerializer(
    .din(data_to_ser),
    .reset(rst),
    .clkPara(clk_para),
    .clkSeri(clk_seri),
    .data_P(TIMING_DOUT_P[0]),
    .data_N(TIMING_DOUT_N[0])
    );

    wire [7:0] lumi_to_ser;
    lumiSource lumiData(
        .W1H(confldpuiniwin1h_0[2:0]),
        .W1L(confldpuiniwin1l_0[2:0]),
        .W2H(confldpuiniwin2h_0[2:0]),
        .W2L(confldpuiniwin2l_0[2:0]),
        .clk40(clk40),
        .clk80(clk80),
        .rst(rst),
        .enable(conf_ldpu_cntrl_0[0]),
        .bcr(bcr),
        .dout(lumi_to_ser)
        );

    oserdesData8b lumiSerializer(
        .din(~lumi_to_ser),
        .reset(rst),
        .enable(conf_ldpu_cntrl_0[3]),
        .clkPara(clk80),
        .clkSeri(clk320),
        .data_P(LUMI_DOUT_N[0]),
        .data_N(LUMI_DOUT_P[0])
    );

//-------------------chip1 data generator------------------
  assign type_1 = conf_tdpu_cntrl_1[3:2];
  assign vth_1 = dac10bconf2_1[2]? {dac10bconf2_1[1:0],dac10bconf1_1} : 10'b0;
  assign txRate_1 = conf_tdpu_cntrl_1[1:0];
  assign en_TDPU_1 = conf_tdpu_cntrl_1[5];
  assign frameData_1 = conf_tdpu_pattern_1;
  assign en8b10b_1 = conf_tdpu_cntrl_1[4];

  wire CharIsK_1;
  wire [7:0] data_to_code_1;
  timingSource timingData_1(
    .type(type_1),
    .en_TDPU(en_TDPU_1),
    .trigger(trigger),
    .reset(rst),
    .clk40(clk40),
    .clk160(clk160),
    .clk_S(clk80),  
    .dataclk(clk_para), 
    .vth(vth_1),
    .vthc(vthc_1),
    .pixelOn(pixelOn_1),
    .CharIsK(CharIsK_1),
    .frameData(frameData_1),
    .data_to_code(data_to_code_1)
      );

  wire [9:0] data_to_ser_1;
  enc_8b10b timingEncode_1( 
    .reset(rst),
    .clk(clk_para),
    .ena(en8b10b_1),
    .KI(CharIsK_1),
    .datain(data_to_code_1),
    .dataout(data_to_ser_1)
    ); 

    oserdesData10b timingSerializer_1(
    .din(data_to_ser_1),
    .reset(rst),
    .clkPara(clk_para),
    .clkSeri(clk_seri),
    .data_P(TIMING_DOUT_N[1]),
    .data_N(TIMING_DOUT_P[1])
    );


    wire [7:0] lumi_to_ser_1;
    lumiSource lumiData_1(
        .W1H(confldpuiniwin1h_1[2:0]),
        .W1L(confldpuiniwin1l_1[2:0]),
        .W2H(confldpuiniwin2h_1[2:0]),
        .W2L(confldpuiniwin2l_1[2:0]),
        .clk40(clk40),
        .clk80(clk80),
        .rst(rst),
        .enable(conf_ldpu_cntrl_1[0]),
        .bcr(bcr),
        .dout(lumi_to_ser_1)
        );

    oserdesData8b lumiSerializer_1(
        .din(lumi_to_ser_1),
        .reset(rst),
        .enable(conf_ldpu_cntrl_1[3]),
        .clkPara(clk80),
        .clkSeri(clk320),
        .data_P(LUMI_DOUT_P[1]),
        .data_N(LUMI_DOUT_N[1])
     );
//--------------------------------------------------------
    // Glitch filter  
    wire gf_i2c_sda;
    glitch_filter #(
    .CLK_FREQ    (CLK_FREQ)
    )i_gf_i2c_sda_in(
        .in   (I2C_SDA),
        .out  (gf_i2c_sda),
        .rise (),
        .fall (),
        .clk  (clk40)
    );

    wire gf_i2c_scl;
    glitch_filter #(
    .CLK_FREQ    (CLK_FREQ)
    )i_gf_i2c_scl_in(
        .in   (I2C_SCL),
        .out  (gf_i2c_scl),
        .rise (),
        .fall (),
        .clk  (clk40)
    );

    //------------------------I2C for chip0----------------------
    wire i2c_sda_o;
    wire [7:0] wb_data_i;
    wire [7:0] wb_data_o;
    wire [15:0] wb_addr_o;
    wire wb_ack_s;
    wire wb_we_s;
    wire wb_stb_s;

    wire I2C_SDA_0;  
    assign I2C_SDA_0 = i2c_sda_o ? 1'bz : 1'b0;

    localparam ALTIROC_I2C_SLAVE_ADRLEN = 2;
    localparam ALTIROC_I2C_SLAVE_DATALEN = 1;
    localparam ALTIROC_I2C_SLAVE_TIMEOUT = 1023;
    localparam ALTIROC_I2C_SLAVE_ADDR_3MSB = 3'b000;
    localparam ALTIROC_I2C_SLAVE_ADDR_BROADCAST_4LSB = 4'b0;

    i2c_slave_wb_master_rstb #(
        .ADRLEN (ALTIROC_I2C_SLAVE_ADRLEN),
        .DATLEN (ALTIROC_I2C_SLAVE_DATALEN),
        .TIMEOUT(ALTIROC_I2C_SLAVE_TIMEOUT*4)
    ) i2c_slave_wb_master (
        .chip_addr_i        ({ALTIROC_I2C_SLAVE_ADDR_3MSB, I2C_ADDR[3:1], 1'b0}),
        .broadcast_addr_i   ({ALTIROC_I2C_SLAVE_ADDR_3MSB, ALTIROC_I2C_SLAVE_ADDR_BROADCAST_4LSB}),
        .clock              (clk40),
        .rst_n              (!rst_i2c),
        .i2c_scl_i          (gf_i2c_scl),
        .i2c_sda_i          (gf_i2c_sda),
        .i2c_sda_o          (i2c_sda_o),
        .wb_adr_o           (wb_addr_o),
        .wb_wen_o           (wb_we_s),
        .wb_stb_o           (wb_stb_s),
        .wb_cyc_o           (),
        .wb_ack_i           (wb_ack_s),
        .wb_dat_i           (wb_data_i),
        .wb_dat_o           (wb_data_o),
        .enable_o           (),
        .err_wb_adr_o       ()
    );

    reg [9:0] reg_addr;
    always @(posedge clk40) begin
        if(wb_addr_o[9:0]>=60&&wb_addr_o[9:0]<119) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 60;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 61;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 62;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 63;
        end
        else if(wb_addr_o[9:0]>=120&&wb_addr_o[9:0]<179) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 120;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 121;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 122;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 123;
        end
        else if(wb_addr_o[9:0]>=180&&wb_addr_o[9:0]<239) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 180;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 181;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 182;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 183;
        end
        else if(wb_addr_o[9:0]>=240&&wb_addr_o[9:0]<299) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 240;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 241;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 242;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 243;
        end
        else if(wb_addr_o[9:0]>=300&&wb_addr_o[9:0]<359) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 300;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 301;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 302;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 303;
        end
        else if(wb_addr_o[9:0]>=360&&wb_addr_o[9:0]<419) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 360;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 361;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 362;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 363;
        end
        else if(wb_addr_o[9:0]>=420&&wb_addr_o[9:0]<479) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 420;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 421;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 422;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 423;
        end
        else if(wb_addr_o[9:0]>=480&&wb_addr_o[9:0]<539) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 480;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 481;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 482;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 483;
        end
        else if(wb_addr_o[9:0]>=540&&wb_addr_o[9:0]<599) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 540;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 541;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 542;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 543;
        end
        else if(wb_addr_o[9:0]>=600&&wb_addr_o[9:0]<659) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 600;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 601;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 602;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 603;
        end
        else if(wb_addr_o[9:0]>=660&&wb_addr_o[9:0]<719) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 660;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 661;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 662;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 663;
        end
        else if(wb_addr_o[9:0]>=720&&wb_addr_o[9:0]<779) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 720;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 721;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 722;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 723;
        end
        else if(wb_addr_o[9:0]>=780&&wb_addr_o[9:0]<839) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 780;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 781;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 782;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 783;
        end
        else if(wb_addr_o[9:0]>=840&&wb_addr_o[9:0]<899) begin
            if(wb_addr_o[9:0]%4==0) reg_addr <= 840;
            if(wb_addr_o[9:0]%4==1) reg_addr <= 841;
            if(wb_addr_o[9:0]%4==2) reg_addr <= 842;
            if(wb_addr_o[9:0]%4==3) reg_addr <= 843;
        end
        else begin
            reg_addr <= wb_addr_o[9:0];
        end
    end

    memory_wb_slave #(.date(DATE))
        memory_wb_slave(
        .confpix0reg0(confpix0reg0_0),
        .confpix0reg1(confpix0reg1_0),
        .confpix0reg2(confpix0reg2_0),
        .confpix0reg3(confpix0reg3_0),
        .confpix1reg0(confpix1reg0_0),
        .confpix1reg1(confpix1reg1_0),
        .confpix1reg2(confpix1reg2_0),
        .confpix1reg3(confpix1reg3_0),
        .confpix2reg0(confpix2reg0_0),
        .confpix2reg1(confpix2reg1_0),
        .confpix2reg2(confpix2reg2_0),
        .confpix2reg3(confpix2reg3_0),
        .confpix3reg0(confpix3reg0_0),
        .confpix3reg1(confpix3reg1_0),
        .confpix3reg2(confpix3reg2_0),
        .confpix3reg3(confpix3reg3_0),
        .confpix4reg0(confpix4reg0_0),
        .confpix4reg1(confpix4reg1_0),
        .confpix4reg2(confpix4reg2_0),
        .confpix4reg3(confpix4reg3_0),
        .confpix5reg0(confpix5reg0_0),
        .confpix5reg1(confpix5reg1_0),
        .confpix5reg2(confpix5reg2_0),
        .confpix5reg3(confpix5reg3_0),
        .confpix6reg0(confpix6reg0_0),
        .confpix6reg1(confpix6reg1_0),
        .confpix6reg2(confpix6reg2_0),
        .confpix6reg3(confpix6reg3_0),
        .confpix7reg0(confpix7reg0_0),
        .confpix7reg1(confpix7reg1_0),
        .confpix7reg2(confpix7reg2_0),
        .confpix7reg3(confpix7reg3_0),
        .confpix8reg0(confpix8reg0_0),
        .confpix8reg1(confpix8reg1_0),
        .confpix8reg2(confpix8reg2_0),
        .confpix8reg3(confpix8reg3_0),
        .confpix9reg0(confpix9reg0_0),
        .confpix9reg1(confpix9reg1_0),
        .confpix9reg2(confpix9reg2_0),
        .confpix9reg3(confpix9reg3_0),
        .confpix10reg0(confpix10reg0_0),
        .confpix10reg1(confpix10reg1_0),
        .confpix10reg2(confpix10reg2_0),
        .confpix10reg3(confpix10reg3_0),
        .confpix11reg0(confpix11reg0_0),
        .confpix11reg1(confpix11reg1_0),
        .confpix11reg2(confpix11reg2_0),
        .confpix11reg3(confpix11reg3_0),
        .confpix12reg0(confpix12reg0_0),
        .confpix12reg1(confpix12reg1_0),
        .confpix12reg2(confpix12reg2_0),
        .confpix12reg3(confpix12reg3_0),
        .confpix13reg0(confpix13reg0_0),
        .confpix13reg1(confpix13reg1_0),
        .confpix13reg2(confpix13reg2_0),
        .confpix13reg3(confpix13reg3_0),
        .confpix14reg0(confpix14reg0_0),
        .confpix14reg1(confpix14reg1_0),
        .confpix14reg2(confpix14reg2_0),
        .confpix14reg3(confpix14reg3_0),
        .confpix15reg0(confpix15reg0_0),
        .confpix15reg1(confpix15reg1_0),
        .confpix15reg2(confpix15reg2_0),
        .confpix15reg3(confpix15reg3_0),
        .confpix30reg0(confpix30reg0_0),
        .confpix30reg1(confpix30reg1_0),
        .confpix30reg2(confpix30reg2_0),
        .confpix30reg3(confpix30reg3_0),
        .confpix45reg0(confpix45reg0_0),
        .confpix45reg1(confpix45reg1_0),
        .confpix45reg2(confpix45reg2_0),
        .confpix45reg3(confpix45reg3_0),
        .confpix60reg0(confpix60reg0_0),
        .confpix60reg1(confpix60reg1_0),
        .confpix60reg2(confpix60reg2_0),
        .confpix60reg3(confpix60reg3_0),
        .confpix75reg0(confpix75reg0_0),
        .confpix75reg1(confpix75reg1_0),
        .confpix75reg2(confpix75reg2_0),
        .confpix75reg3(confpix75reg3_0),
        .confpix90reg0(confpix90reg0_0),
        .confpix90reg1(confpix90reg1_0),
        .confpix90reg2(confpix90reg2_0),
        .confpix90reg3(confpix90reg3_0),
        .confpix105reg0(confpix105reg0_0),
        .confpix105reg1(confpix105reg1_0),
        .confpix105reg2(confpix105reg2_0),
        .confpix105reg3(confpix105reg3_0),
        .confpix120reg0(confpix120reg0_0),
        .confpix120reg1(confpix120reg1_0),
        .confpix120reg2(confpix120reg2_0),
        .confpix120reg3(confpix120reg3_0),
        .confpix135reg0(confpix135reg0_0),
        .confpix135reg1(confpix135reg1_0),
        .confpix135reg2(confpix135reg2_0),
        .confpix135reg3(confpix135reg3_0),
        .confpix150reg0(confpix150reg0_0),
        .confpix150reg1(confpix150reg1_0),
        .confpix150reg2(confpix150reg2_0),
        .confpix150reg3(confpix150reg3_0),
        .confpix165reg0(confpix165reg0_0),
        .confpix165reg1(confpix165reg1_0),
        .confpix165reg2(confpix165reg2_0),
        .confpix165reg3(confpix165reg3_0),
        .confpix180reg0(confpix180reg0_0),
        .confpix180reg1(confpix180reg1_0),
        .confpix180reg2(confpix180reg2_0),
        .confpix180reg3(confpix180reg3_0),
        .confpix195reg0(confpix195reg0_0),
        .confpix195reg1(confpix195reg1_0),
        .confpix195reg2(confpix195reg2_0),
        .confpix195reg3(confpix195reg3_0),
        .confpix210reg0(confpix210reg0_0),
        .confpix210reg1(confpix210reg1_0),
        .confpix210reg2(confpix210reg2_0),
        .confpix210reg3(confpix210reg3_0),
        .confldpuiniwin1l(confldpuiniwin1l_0),
        .confldpuiniwin1h(confldpuiniwin1h_0),
        .confldpuiniwin2l(confldpuiniwin2l_0),
        .confldpuiniwin2h(confldpuiniwin2h_0),
        .conf_ldpu_cntrl(conf_ldpu_cntrl_0),
        .conftdpulatencyl(conftdpulatencyl_0),
        .conftdpulatencyh(conftdpulatencyh_0),
        .conf_tdpu_cntrl(conf_tdpu_cntrl_0),
        .conf_tdpu_pattern(conf_tdpu_pattern_0),
        .conf_tdpu_ocupref(conf_tdpu_ocupref_0),
        .dacrpgconf2(dacrpgconf2_0),
        .dacrpgconf1(dacrpgconf1_0),
        .bias_ch_sel_pulser(bias_ch_sel_pulser_0),
        .bias_ch_dac_pa(bias_ch_dac_pa_0),
        .bias_ch_dac_dc_pa(bias_ch_dac_dc_pa_0),
        .dac10bconf1(dac10bconf1_0),
        .dac10bconf2(dac10bconf2_0),
        .pixeladdr(pixeladdr_0),
        .dll_120p_toa_cbit(dll_120p_toa_cbit_0),
        .dll_120p_toa_cp(dll_120p_toa_cp_0),
        .dll_120p_toa_comp(dll_120p_toa_comp_0),
        .dll_120p_tot_cbit(dll_120p_tot_cbit_0),
        .dll_120p_tot_cp(dll_120p_tot_cp_0),
        .dll_120p_tot_comp(dll_120p_tot_comp_0),
        .dll_140p_toa_cbit(dll_140p_toa_cbit_0),
        .dll_140p_toa_cp(dll_140p_toa_cp_0),
        .dll_140p_toa_comp(dll_140p_toa_comp_0),
        .dllcntrconf(dllcntrconf_0),
        .selprobebiasconf(selprobebiasconf_0),
        .confglobalenprobe(confglobalenprobe_0),
        .confglobalsignaltdcs(confglobalsignaltdcs_0),
        .confglobalsignalrincdcp(confglobalsignalrincdcp_0),
        .conf_global_cntr(conf_global_cntr_0),
        .conf_global_occupancy(conf_global_occupancy_0),
        .enablecgeocl(enablecgeocl_0),
        .enablecgeoch(enablecgeoch_0),
        .conf_anaperi_selprobemon(conf_anaperi_selprobemon_0),
        .bgconf(bgconf_0),
        .pllcpconf(pllcpconf_0),
        .pllbwconf(pllbwconf_0),
        .pllcntr1(pllcntr1_0),
        .pllcntr2(pllcntr2_0),
        .conf_anaperi_plllocksamples(conf_anaperi_plllocksamples_0),
        .conf_anaperi(conf_anaperi_0),
        .psdelay1(psdelay1_0),
        .psdelay2(psdelay2_0),
        .psdelaylum(psdelaylum_0),
        .pscntr1(pscntr1_0),
        .pscntr2(pscntr2_0),
        .entestpadsconf1(entestpadsconf1_0),
        .entestpadsconf2(entestpadsconf2_0),
        .global_extclock(global_extclock_0),
        .clktestpadsconf(clktestpadsconf_0),
        .probedigtestpadsconf(probedigtestpadsconf_0),
        .conf_fccu_trigid_l(conf_fccu_trigid_l_0),
        .conf_fccu_trigid_h(conf_fccu_trigid_h_0),
        .fccucntrconf(fccucntrconf_0),
        .cmdcalgenconf1(cmdcalgenconf1_0),
        .cmdcalgenconf2(cmdcalgenconf2_0),
        .cmdcalgenconf3(cmdcalgenconf3_0),
        .logRegister(logRegister_0),

        .clk_wb  (clk40),
        .wb_rst  (rst_i2c),
        .wb_stb_i(wb_stb_s),
        .wb_ack_o(wb_ack_s),
        .wb_wen_i(wb_we_s),
        .wb_dat_i(wb_data_o),
        .wb_dat_o(wb_data_i),
        // .wb_adr_i(wb_addr_o[9:0])
        .wb_adr_i(reg_addr)
    ); 

//------------------------I2C for chip1----------------------
    //  i2c_to_wb_top
    wire i2c_sda_o_1;
    wire [7:0] wb_data_i_1;
    wire [7:0] wb_data_o_1;
    wire [15:0] wb_addr_o_1;
    wire wb_ack_s_1;
    wire wb_we_s_1;
    wire wb_stb_s_1;

    wire I2C_SDA_1;
    assign I2C_SDA_1 = i2c_sda_o_1 ? 1'bz : 1'b0;

    i2c_slave_wb_master_rstb #(
        .ADRLEN (ALTIROC_I2C_SLAVE_ADRLEN),
        .DATLEN (ALTIROC_I2C_SLAVE_DATALEN),
        .TIMEOUT(ALTIROC_I2C_SLAVE_TIMEOUT*4)
    ) i2c_slave_wb_master_1 (
        .chip_addr_i        ({ALTIROC_I2C_SLAVE_ADDR_3MSB, I2C_ADDR[3:1], 1'b1}),
        .broadcast_addr_i   ({ALTIROC_I2C_SLAVE_ADDR_3MSB, ALTIROC_I2C_SLAVE_ADDR_BROADCAST_4LSB}),
        .clock              (clk40),
        .rst_n              (!rst_i2c),
        .i2c_scl_i          (gf_i2c_scl),
        .i2c_sda_i          (gf_i2c_sda),
        .i2c_sda_o          (i2c_sda_o_1),
        .wb_adr_o           (wb_addr_o_1),
        .wb_wen_o           (wb_we_s_1),
        .wb_stb_o           (wb_stb_s_1),
        .wb_cyc_o           (),
        .wb_ack_i           (wb_ack_s_1),
        .wb_dat_i           (wb_data_i_1),
        .wb_dat_o           (wb_data_o_1),
        .enable_o           (),
        .err_wb_adr_o       ()
    );

    reg [9:0] reg_addr_1;
    always @(posedge clk40) begin
        if(wb_addr_o_1[9:0]>=60&&wb_addr_o_1[9:0]<119) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 60;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 61;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 62;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 63;
        end
        else if(wb_addr_o_1[9:0]>=120&&wb_addr_o_1[9:0]<179) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 120;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 121;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 122;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 123;
        end
        else if(wb_addr_o_1[9:0]>=180&&wb_addr_o_1[9:0]<239) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 180;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 181;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 182;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 183;
        end
        else if(wb_addr_o_1[9:0]>=240&&wb_addr_o_1[9:0]<299) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 240;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 241;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 242;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 243;
        end
        else if(wb_addr_o_1[9:0]>=300&&wb_addr_o_1[9:0]<359) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 300;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 301;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 302;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 303;
        end
        else if(wb_addr_o_1[9:0]>=360&&wb_addr_o_1[9:0]<419) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 360;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 361;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 362;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 363;
        end
        else if(wb_addr_o_1[9:0]>=420&&wb_addr_o_1[9:0]<479) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 420;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 421;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 422;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 423;
        end
        else if(wb_addr_o_1[9:0]>=480&&wb_addr_o_1[9:0]<539) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 480;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 481;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 482;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 483;
        end
        else if(wb_addr_o_1[9:0]>=540&&wb_addr_o_1[9:0]<599) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 540;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 541;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 542;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 543;
        end
        else if(wb_addr_o_1[9:0]>=600&&wb_addr_o_1[9:0]<659) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 600;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 601;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 602;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 603;
        end
        else if(wb_addr_o_1[9:0]>=660&&wb_addr_o_1[9:0]<719) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 660;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 661;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 662;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 663;
        end
        else if(wb_addr_o_1[9:0]>=720&&wb_addr_o_1[9:0]<779) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 720;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 721;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 722;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 723;
        end
        else if(wb_addr_o_1[9:0]>=780&&wb_addr_o_1[9:0]<839) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 780;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 781;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 782;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 783;
        end
        else if(wb_addr_o_1[9:0]>=840&&wb_addr_o_1[9:0]<899) begin
            if(wb_addr_o_1[9:0]%4==0) reg_addr_1 <= 840;
            if(wb_addr_o_1[9:0]%4==1) reg_addr_1 <= 841;
            if(wb_addr_o_1[9:0]%4==2) reg_addr_1 <= 842;
            if(wb_addr_o_1[9:0]%4==3) reg_addr_1 <= 843;
        end
        else begin
            reg_addr_1 <= wb_addr_o_1[9:0];
        end
    end

    memory_wb_slave #(.date(DATE))
        memory_wb_slave_1(
        .confpix0reg0(confpix0reg0_1),
        .confpix0reg1(confpix0reg1_1),
        .confpix0reg2(confpix0reg2_1),
        .confpix0reg3(confpix0reg3_1),
        .confpix1reg0(confpix1reg0_1),
        .confpix1reg1(confpix1reg1_1),
        .confpix1reg2(confpix1reg2_1),
        .confpix1reg3(confpix1reg3_1),
        .confpix2reg0(confpix2reg0_1),
        .confpix2reg1(confpix2reg1_1),
        .confpix2reg2(confpix2reg2_1),
        .confpix2reg3(confpix2reg3_1),
        .confpix3reg0(confpix3reg0_1),
        .confpix3reg1(confpix3reg1_1),
        .confpix3reg2(confpix3reg2_1),
        .confpix3reg3(confpix3reg3_1),
        .confpix4reg0(confpix4reg0_1),
        .confpix4reg1(confpix4reg1_1),
        .confpix4reg2(confpix4reg2_1),
        .confpix4reg3(confpix4reg3_1),
        .confpix5reg0(confpix5reg0_1),
        .confpix5reg1(confpix5reg1_1),
        .confpix5reg2(confpix5reg2_1),
        .confpix5reg3(confpix5reg3_1),
        .confpix6reg0(confpix6reg0_1),
        .confpix6reg1(confpix6reg1_1),
        .confpix6reg2(confpix6reg2_1),
        .confpix6reg3(confpix6reg3_1),
        .confpix7reg0(confpix7reg0_1),
        .confpix7reg1(confpix7reg1_1),
        .confpix7reg2(confpix7reg2_1),
        .confpix7reg3(confpix7reg3_1),
        .confpix8reg0(confpix8reg0_1),
        .confpix8reg1(confpix8reg1_1),
        .confpix8reg2(confpix8reg2_1),
        .confpix8reg3(confpix8reg3_1),
        .confpix9reg0(confpix9reg0_1),
        .confpix9reg1(confpix9reg1_1),
        .confpix9reg2(confpix9reg2_1),
        .confpix9reg3(confpix9reg3_1),
        .confpix10reg0(confpix10reg0_1),
        .confpix10reg1(confpix10reg1_1),
        .confpix10reg2(confpix10reg2_1),
        .confpix10reg3(confpix10reg3_1),
        .confpix11reg0(confpix11reg0_1),
        .confpix11reg1(confpix11reg1_1),
        .confpix11reg2(confpix11reg2_1),
        .confpix11reg3(confpix11reg3_1),
        .confpix12reg0(confpix12reg0_1),
        .confpix12reg1(confpix12reg1_1),
        .confpix12reg2(confpix12reg2_1),
        .confpix12reg3(confpix12reg3_1),
        .confpix13reg0(confpix13reg0_1),
        .confpix13reg1(confpix13reg1_1),
        .confpix13reg2(confpix13reg2_1),
        .confpix13reg3(confpix13reg3_1),
        .confpix14reg0(confpix14reg0_1),
        .confpix14reg1(confpix14reg1_1),
        .confpix14reg2(confpix14reg2_1),
        .confpix14reg3(confpix14reg3_1),
        .confpix15reg0(confpix15reg0_1),
        .confpix15reg1(confpix15reg1_1),
        .confpix15reg2(confpix15reg2_1),
        .confpix15reg3(confpix15reg3_1),
        .confpix30reg0(confpix30reg0_1),
        .confpix30reg1(confpix30reg1_1),
        .confpix30reg2(confpix30reg2_1),
        .confpix30reg3(confpix30reg3_1),
        .confpix45reg0(confpix45reg0_1),
        .confpix45reg1(confpix45reg1_1),
        .confpix45reg2(confpix45reg2_1),
        .confpix45reg3(confpix45reg3_1),
        .confpix60reg0(confpix60reg0_1),
        .confpix60reg1(confpix60reg1_1),
        .confpix60reg2(confpix60reg2_1),
        .confpix60reg3(confpix60reg3_1),
        .confpix75reg0(confpix75reg0_1),
        .confpix75reg1(confpix75reg1_1),
        .confpix75reg2(confpix75reg2_1),
        .confpix75reg3(confpix75reg3_1),
        .confpix90reg0(confpix90reg0_1),
        .confpix90reg1(confpix90reg1_1),
        .confpix90reg2(confpix90reg2_1),
        .confpix90reg3(confpix90reg3_1),
        .confpix105reg0(confpix105reg0_1),
        .confpix105reg1(confpix105reg1_1),
        .confpix105reg2(confpix105reg2_1),
        .confpix105reg3(confpix105reg3_1),
        .confpix120reg0(confpix120reg0_1),
        .confpix120reg1(confpix120reg1_1),
        .confpix120reg2(confpix120reg2_1),
        .confpix120reg3(confpix120reg3_1),
        .confpix135reg0(confpix135reg0_1),
        .confpix135reg1(confpix135reg1_1),
        .confpix135reg2(confpix135reg2_1),
        .confpix135reg3(confpix135reg3_1),
        .confpix150reg0(confpix150reg0_1),
        .confpix150reg1(confpix150reg1_1),
        .confpix150reg2(confpix150reg2_1),
        .confpix150reg3(confpix150reg3_1),
        .confpix165reg0(confpix165reg0_1),
        .confpix165reg1(confpix165reg1_1),
        .confpix165reg2(confpix165reg2_1),
        .confpix165reg3(confpix165reg3_1),
        .confpix180reg0(confpix180reg0_1),
        .confpix180reg1(confpix180reg1_1),
        .confpix180reg2(confpix180reg2_1),
        .confpix180reg3(confpix180reg3_1),
        .confpix195reg0(confpix195reg0_1),
        .confpix195reg1(confpix195reg1_1),
        .confpix195reg2(confpix195reg2_1),
        .confpix195reg3(confpix195reg3_1),
        .confpix210reg0(confpix210reg0_1),
        .confpix210reg1(confpix210reg1_1),
        .confpix210reg2(confpix210reg2_1),
        .confpix210reg3(confpix210reg3_1),
        .confldpuiniwin1l(confldpuiniwin1l_1),
        .confldpuiniwin1h(confldpuiniwin1h_1),
        .confldpuiniwin2l(confldpuiniwin2l_1),
        .confldpuiniwin2h(confldpuiniwin2h_1),
        .conf_ldpu_cntrl(conf_ldpu_cntrl_1),
        .conftdpulatencyl(conftdpulatencyl_1),
        .conftdpulatencyh(conftdpulatencyh_1),
        .conf_tdpu_cntrl(conf_tdpu_cntrl_1),
        .conf_tdpu_pattern(conf_tdpu_pattern_1),
        .conf_tdpu_ocupref(conf_tdpu_ocupref_1),
        .dacrpgconf2(dacrpgconf2_1),
        .dacrpgconf1(dacrpgconf1_1),
        .bias_ch_sel_pulser(bias_ch_sel_pulser_1),
        .bias_ch_dac_pa(bias_ch_dac_pa_1),
        .bias_ch_dac_dc_pa(bias_ch_dac_dc_pa_1),
        .dac10bconf1(dac10bconf1_1),
        .dac10bconf2(dac10bconf2_1),
        .pixeladdr(pixeladdr_1),
        .dll_120p_toa_cbit(dll_120p_toa_cbit_1),
        .dll_120p_toa_cp(dll_120p_toa_cp_1),
        .dll_120p_toa_comp(dll_120p_toa_comp_1),
        .dll_120p_tot_cbit(dll_120p_tot_cbit_1),
        .dll_120p_tot_cp(dll_120p_tot_cp_1),
        .dll_120p_tot_comp(dll_120p_tot_comp_1),
        .dll_140p_toa_cbit(dll_140p_toa_cbit_1),
        .dll_140p_toa_cp(dll_140p_toa_cp_1),
        .dll_140p_toa_comp(dll_140p_toa_comp_1),
        .dllcntrconf(dllcntrconf_1),
        .selprobebiasconf(selprobebiasconf_1),
        .confglobalenprobe(confglobalenprobe_1),
        .confglobalsignaltdcs(confglobalsignaltdcs_1),
        .confglobalsignalrincdcp(confglobalsignalrincdcp_1),
        .conf_global_cntr(conf_global_cntr_1),
        .conf_global_occupancy(conf_global_occupancy_1),
        .enablecgeocl(enablecgeocl_1),
        .enablecgeoch(enablecgeoch_1),
        .conf_anaperi_selprobemon(conf_anaperi_selprobemon_1),
        .bgconf(bgconf_1),
        .pllcpconf(pllcpconf_1),
        .pllbwconf(pllbwconf_1),
        .pllcntr1(pllcntr1_1),
        .pllcntr2(pllcntr2_1),
        .conf_anaperi_plllocksamples(conf_anaperi_plllocksamples_1),
        .conf_anaperi(conf_anaperi_1),
        .psdelay1(psdelay1_1),
        .psdelay2(psdelay2_1),
        .psdelaylum(psdelaylum_1),
        .pscntr1(pscntr1_1),
        .pscntr2(pscntr2_1),
        .entestpadsconf1(entestpadsconf1_1),
        .entestpadsconf2(entestpadsconf2_1),
        .global_extclock(global_extclock_1),
        .clktestpadsconf(clktestpadsconf_1),
        .probedigtestpadsconf(probedigtestpadsconf_1),
        .conf_fccu_trigid_l(conf_fccu_trigid_l_1),
        .conf_fccu_trigid_h(conf_fccu_trigid_h_1),
        .fccucntrconf(fccucntrconf_1),
        .cmdcalgenconf1(cmdcalgenconf1_1),
        .cmdcalgenconf2(cmdcalgenconf2_1),
        .cmdcalgenconf3(cmdcalgenconf3_1),
        .logRegister(logRegister_1),

        .clk_wb  (clk40),
        .wb_rst  (rst_i2c),
        .wb_stb_i(wb_stb_s_1),
        .wb_ack_o(wb_ack_s_1),
        .wb_wen_i(wb_we_s_1),
        .wb_dat_i(wb_data_o_1),
        .wb_dat_o(wb_data_i_1),
        // .wb_adr_i(wb_addr_o_1[9:0])
        .wb_adr_i(reg_addr_1)
    );
    assign I2C_SDA = I2C_SDA_0;
    assign I2C_SDA = I2C_SDA_1;

    //--------------------------vthc for chip0------------------------------
    assign vthc[7:0] = confpix0reg3_0;
    assign vthc[15:8] = confpix1reg3_0;
    assign vthc[23:16] = confpix2reg3_0;
    assign vthc[31:24] = confpix3reg3_0;
    assign vthc[39:32] = confpix4reg3_0;
    assign vthc[47:40] = confpix5reg3_0;
    assign vthc[55:48] = confpix6reg3_0;
    assign vthc[63:56] = confpix7reg3_0;
    assign vthc[71:64] = confpix8reg3_0;
    assign vthc[79:72] = confpix9reg3_0;
    assign vthc[87:80] = confpix10reg3_0;
    assign vthc[95:88] = confpix11reg3_0;
    assign vthc[103:96] = confpix12reg3_0;
    assign vthc[111:104] = confpix13reg3_0;
    assign vthc[119:112] = confpix14reg3_0;
    assign vthc[127:120] = confpix15reg3_0;
    assign vthc[135:128] = confpix30reg3_0;
    assign vthc[143:136] = confpix45reg3_0;
    assign vthc[151:144] = confpix60reg3_0;
    assign vthc[159:152] = confpix75reg3_0;
    assign vthc[167:160] = confpix90reg3_0;
    assign vthc[175:168] = confpix105reg3_0;
    assign vthc[183:176] = confpix120reg3_0;
    assign vthc[191:184] = confpix135reg3_0;
    assign vthc[199:192] = confpix150reg3_0;
    assign vthc[207:200] = confpix165reg3_0;
    assign vthc[215:208] = confpix180reg3_0;
    assign vthc[223:216] = confpix195reg3_0;
    assign vthc[231:224] = confpix210reg3_0;

    //-------------------------pixelOn for chip0---------------------------
    assign pixelOn[0] = confpix0reg1_0[5] & confpix0reg1_0[4];
    assign pixelOn[1] = confpix1reg1_0[5] & confpix1reg1_0[4];
    assign pixelOn[2] = confpix2reg1_0[5] & confpix2reg1_0[4];
    assign pixelOn[3] = confpix3reg1_0[5] & confpix3reg1_0[4];
    assign pixelOn[4] = confpix4reg1_0[5] & confpix4reg1_0[4];
    assign pixelOn[5] = confpix5reg1_0[5] & confpix5reg1_0[4];
    assign pixelOn[6] = confpix6reg1_0[5] & confpix6reg1_0[4];
    assign pixelOn[7] = confpix7reg1_0[5] & confpix7reg1_0[4];
    assign pixelOn[8] = confpix8reg1_0[5] & confpix8reg1_0[4];
    assign pixelOn[9] = confpix9reg1_0[5] & confpix9reg1_0[4];
    assign pixelOn[10] = confpix10reg1_0[5] & confpix10reg1_0[4];
    assign pixelOn[11] = confpix11reg1_0[5] & confpix11reg1_0[4];
    assign pixelOn[12] = confpix12reg1_0[5] & confpix12reg1_0[4];
    assign pixelOn[13] = confpix13reg1_0[5] & confpix13reg1_0[4];
    assign pixelOn[14] = confpix14reg1_0[5] & confpix14reg1_0[4];
    assign pixelOn[15] = confpix15reg1_0[5] & confpix15reg1_0[4];
    assign pixelOn[16] = confpix30reg1_0[5] & confpix30reg1_0[4];
    assign pixelOn[17] = confpix45reg1_0[5] & confpix45reg1_0[4];
    assign pixelOn[18] = confpix60reg1_0[5] & confpix60reg1_0[4];
    assign pixelOn[19] = confpix75reg1_0[5] & confpix75reg1_0[4];
    assign pixelOn[20] = confpix90reg1_0[5] & confpix90reg1_0[4];
    assign pixelOn[21] = confpix105reg1_0[5] & confpix105reg1_0[4];
    assign pixelOn[22] = confpix120reg1_0[5] & confpix120reg1_0[4];
    assign pixelOn[23] = confpix135reg1_0[5] & confpix135reg1_0[4];
    assign pixelOn[24] = confpix150reg1_0[5] & confpix150reg1_0[4];
    assign pixelOn[25] = confpix165reg1_0[5] & confpix165reg1_0[4];
    assign pixelOn[26] = confpix180reg1_0[5] & confpix180reg1_0[4];
    assign pixelOn[27] = confpix195reg1_0[5] & confpix195reg1_0[4];
    assign pixelOn[28] = confpix210reg1_0[5] & confpix210reg1_0[4];

    //--------------------------vthc for chip1------------------------------
    assign vthc_1[7:0] = confpix0reg3_1;
    assign vthc_1[15:8] = confpix1reg3_1;
    assign vthc_1[23:16] = confpix2reg3_1;
    assign vthc_1[31:24] = confpix3reg3_1;
    assign vthc_1[39:32] = confpix4reg3_1;
    assign vthc_1[47:40] = confpix5reg3_1;
    assign vthc_1[55:48] = confpix6reg3_1;
    assign vthc_1[63:56] = confpix7reg3_1;
    assign vthc_1[71:64] = confpix8reg3_1;
    assign vthc_1[79:72] = confpix9reg3_1;
    assign vthc_1[87:80] = confpix10reg3_1;
    assign vthc_1[95:88] = confpix11reg3_1;
    assign vthc_1[103:96] = confpix12reg3_1;
    assign vthc_1[111:104] = confpix13reg3_1;
    assign vthc_1[119:112] = confpix14reg3_1;
    assign vthc_1[127:120] = confpix15reg3_1;
    assign vthc_1[135:128] = confpix30reg3_1;
    assign vthc_1[143:136] = confpix45reg3_1;
    assign vthc_1[151:144] = confpix60reg3_1;
    assign vthc_1[159:152] = confpix75reg3_1;
    assign vthc_1[167:160] = confpix90reg3_1;
    assign vthc_1[175:168] = confpix105reg3_1;
    assign vthc_1[183:176] = confpix120reg3_1;
    assign vthc_1[191:184] = confpix135reg3_1;
    assign vthc_1[199:192] = confpix150reg3_1;
    assign vthc_1[207:200] = confpix165reg3_1;
    assign vthc_1[215:208] = confpix180reg3_1;
    assign vthc_1[223:216] = confpix195reg3_1;
    assign vthc_1[231:224] = confpix210reg3_1;

    //-------------------------pixelOn for chip1---------------------------
    assign pixelOn_1[0] = confpix0reg1_1[5] & confpix0reg1_1[4];
    assign pixelOn_1[1] = confpix1reg1_1[5] & confpix1reg1_1[4];
    assign pixelOn_1[2] = confpix2reg1_1[5] & confpix2reg1_1[4];
    assign pixelOn_1[3] = confpix3reg1_1[5] & confpix3reg1_1[4];
    assign pixelOn_1[4] = confpix4reg1_1[5] & confpix4reg1_1[4];
    assign pixelOn_1[5] = confpix5reg1_1[5] & confpix5reg1_1[4];
    assign pixelOn_1[6] = confpix6reg1_1[5] & confpix6reg1_1[4];
    assign pixelOn_1[7] = confpix7reg1_1[5] & confpix7reg1_1[4];
    assign pixelOn_1[8] = confpix8reg1_1[5] & confpix8reg1_1[4];
    assign pixelOn_1[9] = confpix9reg1_1[5] & confpix9reg1_1[4];
    assign pixelOn_1[10] = confpix10reg1_1[5] & confpix10reg1_1[4];
    assign pixelOn_1[11] = confpix11reg1_1[5] & confpix11reg1_1[4];
    assign pixelOn_1[12] = confpix12reg1_1[5] & confpix12reg1_1[4];
    assign pixelOn_1[13] = confpix13reg1_1[5] & confpix13reg1_1[4];
    assign pixelOn_1[14] = confpix14reg1_1[5] & confpix14reg1_1[4];
    assign pixelOn_1[15] = confpix15reg1_1[5] & confpix15reg1_1[4];
    assign pixelOn_1[16] = confpix30reg1_1[5] & confpix30reg1_1[4];
    assign pixelOn_1[17] = confpix45reg1_1[5] & confpix45reg1_1[4];
    assign pixelOn_1[18] = confpix60reg1_1[5] & confpix60reg1_1[4];
    assign pixelOn_1[19] = confpix75reg1_1[5] & confpix75reg1_1[4];
    assign pixelOn_1[20] = confpix90reg1_1[5] & confpix90reg1_1[4];
    assign pixelOn_1[21] = confpix105reg1_1[5] & confpix105reg1_1[4];
    assign pixelOn_1[22] = confpix120reg1_1[5] & confpix120reg1_1[4];
    assign pixelOn_1[23] = confpix135reg1_1[5] & confpix135reg1_1[4];
    assign pixelOn_1[24] = confpix150reg1_1[5] & confpix150reg1_1[4];
    assign pixelOn_1[25] = confpix165reg1_1[5] & confpix165reg1_1[4];
    assign pixelOn_1[26] = confpix180reg1_1[5] & confpix180reg1_1[4];
    assign pixelOn_1[27] = confpix195reg1_1[5] & confpix195reg1_1[4];
    assign pixelOn_1[28] = confpix210reg1_1[5] & confpix210reg1_1[4];


    ila_1 lumi_prob(
        .clk(clk40),

        .probe0(clk40),
        .probe1(clk80),
        .probe2(clk320),        
        .probe3(clk_para),
        .probe4(clk_seri),        
        .probe5(bcr),        
        .probe6(data_to_ser),
        .probe7(lumi_to_ser)
    );


endmodule

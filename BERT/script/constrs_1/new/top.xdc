# ATLAS HGTD Module Emulator V2
# XC7S15-2CPGA196C

# set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 2.5 [current_design]
# FLASH SPIx4 MX25V8035FM1I
set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]

# Reset from lpGBT GPIO
set_property PACKAGE_PIN K1 [get_ports LPGBT_HARD_RSTB]
set_property IOSTANDARD LVCMOS12 [get_ports LPGBT_HARD_RSTB]
set_property PULLUP true [get_ports LPGBT_HARD_RSTB]

# CLK 40MHz from lpGBT ECLK
set_property PACKAGE_PIN G2 [get_ports LPGBT_CLK40M_P]
# set_property PACKAGE_PIN G1 [get_ports LPGBT_CLK40M_N]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports LPGBT_CLK40M_P]
create_clock -period 24.951 -name LPGBT_CLK [get_ports LPGBT_CLK40M_P]

# ELINKs
set_property PACKAGE_PIN M1 [get_ports FAST_CMD_P]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports FAST_CMD_P]
# set_property PACKAGE_PIN M2 [get_ports FAST_CMD_N]
# set_property IOSTANDARD DIFF_HSUL_12 [get_ports FAST_CMD_N]

set_property PACKAGE_PIN C2 [get_ports {TIMING_DOUT_P[0]}]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports {TIMING_DOUT_P[0]}]
# set_property PACKAGE_PIN C1 [get_ports TIMING_DOUT_N[0]]
# set_property IOSTANDARD DIFF_HSUL_12 [get_ports TIMING_DOUT_N[0]]

set_property PACKAGE_PIN P2 [get_ports {TIMING_DOUT_P[1]}]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports {TIMING_DOUT_P[1]}]
# set_property PACKAGE_PIN P3 [get_ports TIMING_DOUT_N[1]]
# set_property IOSTANDARD DIFF_HSUL_12 [get_ports TIMING_DOUT_N[1]]

set_property PACKAGE_PIN H1 [get_ports {LUMI_DOUT_P[0]}]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports {LUMI_DOUT_P[0]}]
# set_property PACKAGE_PIN J1 [get_ports LUMI_DOUT_N[0]]
# set_property IOSTANDARD DIFF_HSUL_12 [get_ports LUMI_DOUT_N[0]]

set_property PACKAGE_PIN N4 [get_ports {LUMI_DOUT_P[1]}]
set_property IOSTANDARD DIFF_HSUL_12 [get_ports {LUMI_DOUT_P[1]}]
# set_property PACKAGE_PIN M4 [get_ports LUMI_DOUT_N[1]]
# set_property IOSTANDARD DIFF_HSUL_12 [get_ports LUMI_DOUT_N[1]]

set_property PACKAGE_PIN L4 [get_ports {I2C_ADDR[1]}]
set_property IOSTANDARD LVCMOS12 [get_ports {I2C_ADDR[1]}]
set_property PACKAGE_PIN L3 [get_ports {I2C_ADDR[2]}]
set_property IOSTANDARD LVCMOS12 [get_ports {I2C_ADDR[2]}]
set_property PACKAGE_PIN L2 [get_ports {I2C_ADDR[3]}]
set_property IOSTANDARD LVCMOS12 [get_ports {I2C_ADDR[3]}]

set_property PACKAGE_PIN P4 [get_ports I2C_SCL]
set_property IOSTANDARD LVCMOS12 [get_ports I2C_SCL]
set_property PULLUP true [get_ports I2C_SCL]
set_property PACKAGE_PIN N3 [get_ports I2C_SDA]
set_property IOSTANDARD LVCMOS12 [get_ports I2C_SDA]
set_property PULLUP true [get_ports I2C_SDA]

#################################################################
# Local CLK 200MHz
set_property PACKAGE_PIN G14 [get_ports REFCLK_P]
# set_property PACKAGE_PIN F14 [get_ports REFCLK_N]
set_property IOSTANDARD LVDS_25 [get_ports REFCLK_P]
create_clock -period 5.000 -name REFCLK [get_ports REFCLK_P]

set_property PACKAGE_PIN H14 [get_ports {DIPSW[0]}]
set_property IOSTANDARD LVCMOS25 [get_ports {DIPSW[0]}]
set_property PULLUP true [get_ports {DIPSW[0]}]
set_property PACKAGE_PIN J14 [get_ports {DIPSW[1]}]
set_property IOSTANDARD LVCMOS25 [get_ports {DIPSW[1]}]
set_property PULLUP true [get_ports {DIPSW[1]}]
set_property PACKAGE_PIN L14 [get_ports {DIPSW[2]}]
set_property IOSTANDARD LVCMOS25 [get_ports {DIPSW[2]}]
set_property PULLUP true [get_ports {DIPSW[2]}]

set_property PACKAGE_PIN B6 [get_ports {TESTPIN[0]}]
set_property IOSTANDARD LVCMOS12 [get_ports {TESTPIN[0]}]
set_property PACKAGE_PIN A5 [get_ports {TESTPIN[1]}]
set_property IOSTANDARD LVCMOS12 [get_ports {TESTPIN[1]}]

set_property PACKAGE_PIN A2 [get_ports {TP[1]}]
set_property IOSTANDARD LVCMOS12 [get_ports {TP[1]}]
set_property PACKAGE_PIN A3 [get_ports {TP[2]}]
set_property IOSTANDARD LVCMOS12 [get_ports {TP[2]}]

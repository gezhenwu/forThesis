set curtime [clock seconds]
set formattime [clock format $curtime -format {%d}]
reset_runs [get_runs]
set_property generic "DATE=$formattime" [current_fileset]
launch_runs impl_1 -to_step write_bitstream -jobs 128
wait_on_runs [get_runs impl_1]
file copy -force ../altiroc_emulator/altiroc_emulator.runs/impl_1/top.bit ../output/altiroc_emulator.bit
#file copy -force ../altiroc_emulator/altiroc_emulator.runs/impl_1/top.ltx ../output/altiroc_emulator.ltx
write_cfgmem  -format mcs -size 1 -interface SPIx4 -loadbit {up 0x00000000 "../output/altiroc_emulator.bit"} -force -file "../output/altiroc_emulator.mcs"
# The configuration files for lpGBT v0 


| Name | Module Power Enable | Module Reset | MUX channel selection | PSclk output | Elink clk output | Elink tx/downlink output | Elink rx/uplink input | Elink EC channel |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |------ |
| config_min_timing.txt | No        | Yes    | Ch0 | PS1, PS2 40MHz | None         | None           | None           | enable |
| config_min_lumi.txt   | -         | -      | Ch0 | PS0 40MHz      | None         | None           | None           | enable |
| config_max_timing.txt | m0~m13    | No     | Ch0 | PS1, PS2 40MHz | m0~m13 40MHz | m0~m13 320Mbps | m0~m13 320Mbps | enable |
| config_max_lumi.txt   | -         | -      | Ch0 | PS0 40MHz      | None         | None           | m0~m13 320Mbps | enable |
| config_m0_timing.txt  | m0 and m1 | m1~m13 | Ch0 | PS1, PS2 40MHz | m0 40MHz     | m0 320Mbps     | m0 320Mbps     | enable |
| config_m0_lumi.txt    | -         | -      | Ch0 | PS0 40MHz      | None         | None           | m0 320Mbps     | enable |

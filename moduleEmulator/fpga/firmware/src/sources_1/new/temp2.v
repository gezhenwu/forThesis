       // Store the power bits
       rom[0] = {7'h28, 16'h0000, 16'hFFFF};

       // Store CLKOUT0 divide and phase
       rom[24] = (S2_CLKOUT0_FRAC_EN == 0) ?
                 {7'h09, 16'h8000, S2_CLKOUT0[31:16]}:
                 {7'h09, 16'h8000, S2_CLKOUT0_FRAC_CALC[31:16]};
       rom[25] = (S2_CLKOUT0_FRAC_EN == 0) ?
                 {7'h08, 16'h1000, S2_CLKOUT0[15:0]}:
                 {7'h08, 16'h1000, S2_CLKOUT0_FRAC_CALC[15:0]};

       // Store CLKOUT1 divide and phase
       rom[26] = {7'h0A, 16'h1000, S2_CLKOUT1[15:0]};
       rom[27] = {7'h0B, 16'hFC00, S2_CLKOUT1[31:16]};

       // Store CLKOUT2 divide and phase
       rom[28] = {7'h0C, 16'h1000, S2_CLKOUT2[15:0]};
       rom[29] = {7'h0D, 16'hFC00, S2_CLKOUT2[31:16]};

       // Store CLKOUT3 divide and phase
       rom[30] = {7'h0E, 16'h1000, S2_CLKOUT3[15:0]};
       rom[31] = {7'h0F, 16'hFC00, S2_CLKOUT3[31:16]};

       // Store CLKOUT4 divide and phase
       rom[32] = {7'h10, 16'h1000, S2_CLKOUT4[15:0]};
       rom[33] = {7'h11, 16'hFC00, S2_CLKOUT4[31:16]};

       // Store CLKOUT5 divide and phase
       rom[34] = {7'h06, 16'h1000, S2_CLKOUT5[15:0]};
       rom[35] = (S2_CLKOUT0_FRAC_EN == 0) ?
                 {7'h07, 16'hC000, S2_CLKOUT5[31:16]}:
                 {7'h07, 16'hC000, S2_CLKOUT5[31:30], S2_CLKOUT0_FRAC_CALC[35:32],S2_CLKOUT5[25:16]};

       // Store CLKOUT6 divide and phase
       rom[36] = {7'h12, 16'h1000, S2_CLKOUT6[15:0]};
       rom[37] = (S2_CLKFBOUT_FRAC_EN == 0) ?
                 {7'h13, 16'hC000, S2_CLKOUT6[31:16]}:
                 {7'h13, 16'hC000, S2_CLKOUT6[31:30], S2_CLKFBOUT_FRAC_CALC[35:32],S2_CLKOUT6[25:16]};

       // Store the input divider
       rom[38] = {7'h16, 16'hC000, {2'h0, S2_DIVCLK[23:22], S2_DIVCLK[11:0]} };

       // Store the feedback divide and phase
       rom[39] = (S2_CLKFBOUT_FRAC_EN == 0) ?
                 {7'h14, 16'h1000, S2_CLKFBOUT[15:0]}:
                 {7'h14, 16'h1000, S2_CLKFBOUT_FRAC_CALC[15:0]};
       rom[40] = (S2_CLKFBOUT_FRAC_EN == 0) ?
                 {7'h15, 16'h8000, S2_CLKFBOUT[31:16]}:
                 {7'h15, 16'h8000, S2_CLKFBOUT_FRAC_CALC[31:16]};

       // Store the lock settings
       rom[41] = {7'h18, 16'hFC00, {6'h00, S2_LOCK[29:20]} };
       rom[42] = {7'h19, 16'h8000, {1'b0 , S2_LOCK[34:30], S2_LOCK[9:0]} };
       rom[43] = {7'h1A, 16'h8000, {1'b0 , S2_LOCK[39:35], S2_LOCK[19:10]} };

       // Store the filter settings
       rom[44] = {7'h4E, 16'h66FF,
                 S2_DIGITAL_FILT[9], 2'h0, S2_DIGITAL_FILT[8:7], 2'h0,
                 S2_DIGITAL_FILT[6], 8'h00 };
       rom[45] = {7'h4F, 16'h666F,
                 S2_DIGITAL_FILT[5], 2'h0, S2_DIGITAL_FILT[4:3], 2'h0,
                 S2_DIGITAL_FILT[2:1], 2'h0, S2_DIGITAL_FILT[0], 4'h0 };
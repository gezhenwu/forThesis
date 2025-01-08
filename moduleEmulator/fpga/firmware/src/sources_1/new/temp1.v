    .S3_CLKFBOUT_MULT(32),
    .S3_CLKFBOUT_PHASE(000_000),
    .S3_CLKFBOUT_FRAC(000),
    .S3_CLKFBOUT_FRAC_EN(0),
    .S3_BANDWIDTH("OPTIMIZED"),
    .S3_DIVCLK_DIVIDE(1),
    // Set clockout 0 to a divide of 4.750, 0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT0_DIVIDE(16),
    .S3_CLKOUT0_PHASE(000_000),
    .S3_CLKOUT0_DUTY(50000),
    .S3_CLKOUT0_FRAC(000),
    .S3_CLKOUT0_FRAC_EN(0),
    // Set clockout 1 to a divide of 1, 45.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT1_DIVIDE(8),
    .S3_CLKOUT1_PHASE(000_000),
    .S3_CLKOUT1_DUTY(50000),
    // Set clock out 0 to a divide of 1, 90.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT2_DIVIDE(4),
    .S3_CLKOUT2_PHASE(000_000),
    .S3_CLKOUT2_DUTY(50000),
    // Set clockout3 to a divide of 1, 135.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT3_DIVIDE(4),
    .S3_CLKOUT3_PHASE(000_000),
    .S3_CLKOUT3_DUTY(50000),
    // Set clockout4 to a divide of 1, 180.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT4_DIVIDE(20),
    .S3_CLKOUT4_PHASE(180_000),
    .S3_CLKOUT4_DUTY(50000),
    // Set clockout5 to a divide of 1, 225.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT5_DIVIDE(32),
    .S3_CLKOUT5_PHASE(000_000),
    .S3_CLKOUT5_DUTY(50000),
    // Set clockout6 to a divide of 1, 270.0 deg phase offset, 50/50 duty cycle
    .S3_CLKOUT6_DIVIDE(32),
    .S3_CLKOUT6_PHASE(000_000),
    .S3_CLKOUT6_DUTY(50000),
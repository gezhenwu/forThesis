i=0
alldata = []


for V_bias_current in range (48,49,5):    #0~127
    for V_modulation_enable in range (1,2): # 0~1, always enable
        for V_modulation_current in range (32,33,5):  #0~127           
            for V_emphasis_amp in range (0,1):  #0~7
                for V_emphasis_rising_edge_enable in range (0,1):   #0~1
                    for V_emphasis_falling_edge_enable in range (0,1):  #0~1

                        for T_modulation_current in range (2,127,5):  #0~127
                            for T_emphasis_enable in range (1,2):   #0~1, always enable
                                for T_emphasis_short in range (0,2):    #0~1
                                    for T_emphasis_amp in range (2,127,5):    #0~127

                                        i = i+1
                                        print(i)
                                        print(T_modulation_current,T_emphasis_enable,T_emphasis_short,T_emphasis_amp)
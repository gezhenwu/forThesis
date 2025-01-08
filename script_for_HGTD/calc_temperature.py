import math

Ka = 273.15

### for MON_NTC_PEB
Rp = 10
T2 = 25.0 + Ka
Bx = 3435.0

V12 = 1.2
R0 = 100
Vt = 88.53513002214498/1000. # put the output voltage of ADC here(unit:V)

Rt = (Vt*R0)/(V12-Vt)

temp = 1/((1/T2)+(math.log(Rt/Rp)/Bx)) - Ka

print(temp)

### for vtrx+ NTC
#Rp = 1
#T2 = 25.0 + Ka
#Bx = 3500.0

#V12 = 1.2
#R0 = 10
#Vt = 96.87062878850999/1000. # put the output voltage of ADC here(unit:V)

#Rt = (Vt*R0)/(V12-Vt)
#print(Rt)

#temp = 1/((1/T2)+(math.log(Rt/Rp)/Bx)) - Ka

#print(temp)

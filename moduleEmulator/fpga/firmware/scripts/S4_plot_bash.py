import os

counter = 0
epath = ['009','00d','00a','00e','00b','00f','010','014','011','015','012','016','013','017','018','01a','019','01b']
for elink in epath:
    module = 5+counter//2
    counter += 1    
    fileName = './rawData_csv/module%d'%module+'_vth0_'+elink+'.csv'
    file_exist = os.path.isfile(fileName)
    if file_exist is False:
        pass
    else:
        print(elink)
        os.system('python3 data_sum.py *%s'%elink)
        
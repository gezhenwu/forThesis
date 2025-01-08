import yaml

class Sync_Elink(object):
    def read_yaml_to_dict(self, yaml_path: str, ):
        with open(yaml_path) as file:
            dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
        return dict_value
    
    def which_speed(self, str):
        if str == "01": speed = 320
        elif str == "10": speed = 640
        elif str == "11": speed = 1280
        else: speed = 0

        return speed
    
    def RX_value_found(self, dict, lpGBT_nb):
        link_nb = 0
        group_nb = 0
        m = 0
        matrix = [['' for x in range(7)] for y in range(25)]
        list_old = [0 for x in range(28)]
        list = [0 for x in range(16)]
        speed = []
        for key in dict['Links']:
            if key['Link'] == link_nb or -1:
                for key2 in key['EgroupsToHost']:
                    if key2['Egroup'] == group_nb:
                        B1 = key2['WidthToHost']
                        B2 = key2['EnableToHost']
                        if B2 > 16: B2 = B2 - 65536
                        B2 = bin(B2)[2:].zfill(4)
                        if B2 == '0000':
                            matrix[link_nb][group_nb] = '000000'
                        else:
                            matrix[link_nb][group_nb] = B2+bin(B1-1)[2:].zfill(2)
                        group_nb += 1
                        if group_nb > 6: 
                            group_nb = 0
                link_nb += 1   
                if key['Link'] == -1: 
                    link_nb == 24
                if link_nb > 24:
                    link_nb = 0

        for k in matrix[lpGBT_nb]:
            if m in [0,2,4,6]:
                speed.append(self.which_speed(k[4:]))
            for j in range(4):
                list_old[(m+1)*4-j-1] = int(k[j])
            m += 1
        for w1 in range(4):
            list[w1]= list_old[w1] | list_old[w1+4]
        for w2 in range(4,8):
            list[w2]= list_old[w2+4] | list_old[w2+8]
        for w3 in range(8,12):
            list[w3]= list_old[w3+8] | list_old[w3+12]
        for w4 in range(12,14):
            list[w4]= list_old[w4+12] | list_old[w4+14]
        return(matrix, list, speed)
    
    def TX_value_found(self, dict):
        link_nb = 0
        group_nb = 0
        matrix = [['' for x in range(4)] for y in range(24)]
        for key in dict['Links']:
            if key['Link'] == link_nb:
                for key2 in key['EgroupsFromHost']:
                    if key2['Egroup'] == group_nb:
                        B1 = key2['WidthFromHost']
                        B2 = key2['EnableFromHost']
                        if B2 > 16: B2 = B2 - 65536
                        B2 = bin(B2)[2:].zfill(4)
                        if B2 == '0000':
                            matrix[link_nb][group_nb] = '000000'
                        else:
                            matrix[link_nb][group_nb] = B2+bin(B1+1)[2:].zfill(2)
                        group_nb += 1
                        if group_nb > 3: 
                            group_nb = 0
                link_nb += 1   
                if link_nb > 23:
                    link_nb = 0
        return(matrix)

    def __init__(self, file_FELIX):
        self.file_FELIX = file_FELIX

    def sync(self, matrix, list, file_lpGBT, lumi = False):
        lpGBT_nb = int(lumi)
        lpGBT_RX_group_nb = 0
        lpGBT_RXcn_group_nb = 0
        lpGBT_clk_group_nb = 0
        ePortRx = '0xC8'
        ePortRxcn = '0xD0'
        ePortClk = '0x6E'
        ePortTxcn = '0xAE'
        channel = 1
        channel2 = 0
        data = []
        with open(file_lpGBT, encoding='utf-8') as lpGBTfile:
            lpGBTlineList = lpGBTfile.readlines()
            for lpGBTline in lpGBTlineList:
                if "{} ".format(ePortRx) in lpGBTline :
                    lpGBTline = (bin(int(lpGBTline.replace("{} ".format(ePortRx), ''),16))[2:].zfill(8))[6:] # get the last two bits
                    lpGBTline = lpGBTline.replace(lpGBTline, ePortRx+' 0x'+hex(int(matrix[lpGBT_nb][lpGBT_RX_group_nb]+lpGBTline,2))[2:].upper()+'\n') # replace first six bits and preserve last two bits
                    ePortRx = '0x' + hex(int(ePortRx ,16) + 1)[2:].upper()
                    lpGBT_RX_group_nb += 1
                    if ePortRx == '0xCF': ePortRx = 'end'
                if "{} ".format(ePortRxcn) in lpGBTline :
                    number = matrix[lpGBT_nb][lpGBT_RXcn_group_nb][channel-1:channel]
                    if number == '1':
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortRxcn+' 0x6\n') 
                    elif number == '0':
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortRxcn+' 0x0\n') 
                    else: print('error in '+ePortRxcn)
                    ePortRxcn = '0x' + hex(int(ePortRxcn ,16) + 1)[2:].upper()
                    channel += 1
                    if channel == 5: 
                        channel = 1
                        lpGBT_RXcn_group_nb += 1
                    if ePortRxcn == '0xEC': ePortRxcn = 'end'
                if "{} ".format(ePortClk) in lpGBTline :
                    if list[lpGBT_clk_group_nb] == 1:
                        #lpGBTline = (bin(int(lpGBTline.replace("{} ".format(ePortClk), ''),16))[2:].zfill(8))[:2]
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortClk+' 0x'+hex(int('00111001',2))[2:].upper()+'\n')
                    else:
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortClk+' 0x'+hex(int('0',2))[2:].upper()+'\n') 
                    ePortClk = '0x' + hex(int(ePortClk ,16) + 2)[2:].upper()
                    lpGBT_clk_group_nb += 1
                    if ePortClk == '0x8A': ePortClk = 'end'
                if "0xA8 " in lpGBTline :
                    lpGBTline = lpGBTline.replace(lpGBTline, '0xA8 0xFF\n')
                if "0xAA " in lpGBTline :
                    lpGBTline = lpGBTline.replace(lpGBTline, '0xAA 0x'+hex(int(str(list[7])+str(list[6])+str(list[5])+str(list[4])+str(list[3])+str(list[2])+str(list[1])+str(list[0]),2))[2:].upper()+'\n')
                if "0xAB " in lpGBTline :
                    lpGBTline = lpGBTline.replace(lpGBTline, '0xAB 0x'+hex(int(str(list[13])+str(list[12])+str(list[11])+str(list[10])+str(list[9])+str(list[8]),2))[2:].upper()+'\n')
                if "{} ".format(ePortTxcn) in lpGBTline :
                    number = list[channel2]
                    if number == 1:
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortTxcn+' 0x7\n') 
                    elif number == 0:
                        lpGBTline = lpGBTline.replace(lpGBTline, ePortTxcn+' 0x0\n') 
                    else: print('error in '+ePortTxcn)
                    ePortTxcn = '0x' + hex(int(ePortTxcn ,16) + 1)[2:].upper()
                    channel2 += 1
                    if ePortTxcn == '0xBE': ePortTxcn = 'end'
                if lumi == True:
                    if "0x5D " in lpGBTline :
                        lpGBTline = lpGBTline.replace(lpGBTline, '0x5D 0x39\n')
                    if "0x60 " in lpGBTline :
                        lpGBTline = lpGBTline.replace(lpGBTline, '0x60 0x0\n')
                    if "0x63 " in lpGBTline :
                        lpGBTline = lpGBTline.replace(lpGBTline, '0x63 0x0\n')
                data.append(lpGBTline)
        lpGBTfile.close
        return data

    def module_on(self, lumi):
        # get a dictionary from FELIX config
        dict = self.read_yaml_to_dict(self.file_FELIX)
        if(lumi):
            # get a list control lumi RX
            enable, speed = self.RX_value_found(dict,1)[1:]
        else:
            # get a list control timing RX
            enable, speed = self.RX_value_found(dict,0)[1:]
        return enable, speed

    def sync_FELIX_TO_lpGBT(self, file_lpGBT):
        # get a dictionary from FELIX config
        dict = self.read_yaml_to_dict(self.file_FELIX)
        # get a matrix and a list to control RX
        matrix, list, speed  = self.RX_value_found(dict,0)
        print(speed)
        timing = self.sync(matrix, list, file_lpGBT,lumi = False)
        lumi = self.sync(matrix, list, file_lpGBT,lumi = True)
        return timing, lumi
    
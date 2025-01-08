#!/bin/env python

import os,sys
import csv

## Currently, store each block into individual file
## Group hits, three hexdecimal to form a total hit map 
## Total 24 bits with following definition
### Column 4-bit, row 4-bit, CRC 1-bit, TOT 8-bit, TOA 7-bit
def GroupHits(trailer_tmp, inputlist, chipch, block, ndata, asicID, trigger_nb):
    nHex=len(inputlist)
    # print(nHex)

    nHits=nHex/3
    
    ## output formatting 
    datablocks=[]
    #title=["Index", "timestamp", "pixel", "crc", "tot", "toa", "column", "row"]
    
    ## CSV file
    #outputfile=open(outputfilename, "w")
    #writer=csv.writer(outputfile)
    #writer.writerow(title)


    for ihit in range(int(nHits)):
        ## Retrieve column and row information
        part1_tmp=int( inputlist[ihit*3], 16 )  ## convert to decimal/binary
        column_tmp=part1_tmp >> 4 ## retrieve first 4-bit for column and convert to decimal
        row_tmp=part1_tmp & 0b00001111 ## retrieve second 4-bit by masking first 4-bit
        pixid=15*column_tmp+row_tmp
        # print("Column: %s, Row: %s"%(column_tmp, row_tmp ) )
        # ## Retrieve TOT and TOA
        part2_tmp=int( inputlist[ihit*3+1], 16 )
        # CRC=part2_tmp >> 7  ## retrieve CRC which is the highest bin for second hexdecimal        
        try:
            CRC=int( trailer_tmp[2], 16)
        except:
            CRC=-1
        part3_tmp=int( inputlist[ihit*3+2], 16 )
        # part23= ( ( ( part2_tmp & 0b01111111 ) << 8) | part3_tmp ) ## Add two hexdecimal together and mask highest bit
        # print(bin(part23))
        TOT=(part2_tmp<<1) | (part3_tmp>>7)
        TOA= part3_tmp & 0b01111111 ## retrieve TOA with last 7-bits, mask the highest bit
        # print("TOT: %s, TOA: %s"%(TOT, TOA) )
        #data_list_tmp=[ihit, 1.79e09, pixid, CRC, TOT, TOA, column_tmp, row_tmp]
        data_list_total_tmp=[ihit+ndata, 1, pixid, CRC, TOT, TOA, chipch, block, column_tmp, row_tmp, asicID, trigger_nb]
        datablocks.append(data_list_total_tmp)
        #writer.writerow(data_list_tmp)


    #outputfile.close()
    return datablocks


## Read block data from .dat file
def ReadBlockData(inputfile,outputfiletotalname,asicID):
    infile=open(inputfile)
    trigger_nb = infile.read().count("==> BLOCK")
    infile=open(inputfile)

    blockData=[]

    EnterBlock=False

    ## These would be refreshed for each block
    block_dic_tmp={}
    block_dic_tmp["Info"]=""
    block_dic_tmp["blockid"]=0
    block_dic_tmp["Header"]=[]
    block_dic_tmp["Hits"]=[]
    block_dic_tmp["Trailer"]=[]
    block_dic_tmp["chipch"]=0

    block_line_tmp=""
    
    ## Number of data read
    nData=0

    ## Make output directory
    #outputdir_postfix=((inputfile.split("/")[-1]).split(".")[0])

    #outputdir="output/"+outputdir_postfix
    #print(outputdir)
    #if os.path.exists(outputdir)==False:
    #    os.makedirs(outputdir)
    #    
    #outputfiletotalname=outputdir+"/"+outputdir_postfix+".csv" 

    title_total=["Index", "timestamp", "pixel", "crc", "tot", "toa", "chipch", "blockid", "column", "row", "asic", "trigger_nb"]
    
    if asicID == 1:
        outputfiletotal=open(outputfiletotalname, "a")
    else:
        outputfiletotal=open(outputfiletotalname, "w")

    writer_total=csv.writer(outputfiletotal)
    # if asicID == 0:
    #     writer_total.writerow(title_total)

    if 'Index' not in open(outputfiletotalname).read():
        writer_total.writerow(title_total)

    for line in infile:
        #  print(line)
        if line.startswith("==> BLOCK"):
            # print("Found Block")
            chipch=line.split('=')[3]
            if chipch=="600":
                continue
            EnterBlock=True ## Flag to read following lines
            LineIndex=0 ## Refresh line index to read header
            blockid=int(line.split()[2])
            #blockInfo=line 
            ## Refresh block information
            #  block_dic_tmp={}
            block_dic_tmp["Info"]=""
            block_dic_tmp["blockid"]=blockid
            block_dic_tmp["Header"]=[]
            block_dic_tmp["Hits"]=[]
            block_dic_tmp["Trailer"]=[]
            block_dic_tmp["chipch"]=chipch
            block_line_tmp=""
            continue

        elif EnterBlock==True: ## Read Block
            block_line_tmp=block_line_tmp+" "+(line.split("\n"))[0]
            if line.find(")")!=-1: ## To the end of block
                header_tmp=(block_line_tmp.split())[0:3]
                # print(header_tmp)
                trailer_tmp=(block_line_tmp.split("<<")[0]).split()[-3:]
                # print( trailer_tmp )
                #  hit_info_tmp=(block_line_tmp.split())[3:-3]
                hit_info_tmp=(block_line_tmp.split("<<")[0]).split()[3:-3]

                datablock_tmp=GroupHits(trailer_tmp, hit_info_tmp, block_dic_tmp["chipch"], block_dic_tmp["blockid"], nData, asicID, trigger_nb = trigger_nb) ## group and writeout csv format
                writer_total.writerows(datablock_tmp)

                nData=nData+len(hit_info_tmp)/3
                EnterBlock=False
            else:
                continue

    outputfiletotal.close()
# -*- coding: utf-8 -*-
"""
@author: tantirim
@date: 2020-04-06

Wrapper to load openEphys binary data
"""
#%% 
import sys, os, time
import numpy as np
import gc

sys.path.append(r"C:\Users\tantirim\Documents\GitHub\analysis-tools") # path to folder with Binary.py
import Binary

#%% Import data


Folder = r'\\S-VFS-EXT01\JLab$\X\User\Malinda X\ephys\2021-04-16_19-25-53_600um_2'
Exp_num = 1 # experiment number in folder  1 or 2 or n
Rec_num = 1 # recording number in folder  1 or 2 or n

Data_dict, Rate, info = Binary.Load(Folder, Processor='100', Experiment=Exp_num, Recording=Rec_num, Unit='uV', ChannelMap=[]) 

data = Data_dict['100'][str(Exp_num-1)][str(Rec_num-1)]
raw_sf = float(Rate['100'][str(Exp_num-1)]) # sampling rate

ch_num = info['continuous'][0]['num_channels']
info_ch_info = info['continuous'][0]['channels']
ch_names = []
for x in range(ch_num):  
    ch_names.append(info_ch_info[x]['channel_name']) # get channel names
    
print('Import complete,', round(len(data)/raw_sf/60,1), 'min long,', round(sys.getsizeof(data)/1024/1024,2),'MBs')
del Data_dict
gc.collect()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:03:34 2020

@author: davidjany
"""
import os ,shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

#%% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path+'/Samples.xlsx')
df  = xl.parse(sheet_name=0)




#%% Auxiliary functions

def create_dir(name): #creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path+'/'+name)


    
def get_manufacturer(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
            if mat == matrix:
                k = i
                break
    return df['manufacturer'][k]

def get_Tg(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df2['chemical name']):
            if mat == matrix:
                k = i
                break
    return df2['Tg (deg C)'][k]

def get_columns_T(v , dataframe):
    if v ==0.05:
        return dataframe.iloc[1:,0:2]
    elif v == 0.025:
        return dataframe.iloc[1:,2:4]
    elif v == 0.015:
        return dataframe.iloc[1:,4:6]
    elif v == 0.005:
        return dataframe.iloc[1:,6:8]
    else:
        return dataframe.iloc[1:,8:10]
   
def get_columns_F(v ,sample , dataframe):
    if df["pst"][sample] != 'vinyltriethoxysilane':
        if v ==0.05:
            return dataframe.iloc[1:,0:2]
        elif v == 0.025:
            return dataframe.iloc[1:,4:6]
        elif v == 0.015:
            return dataframe.iloc[1:,8:10]
        elif v == 0.005:
            return dataframe.iloc[1:,12:14]
        else:
            return dataframe.iloc[1:,16:18]
    
    else:
        if v ==0.05:
            return dataframe.iloc[1:,2:4]
        elif v == 0.025:
            return dataframe.iloc[1:,6:8]
        elif v == 0.015:
            return dataframe.iloc[1:,10:12]
        elif v == 0.005:
            return dataframe.iloc[1:,14:16]

#%% Mapping
    
def map_data_origin(workbook , sample): #fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['sample no.'][sample]
    
def map_material_type(workbook ,sample):  #fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    sheet["C46"] = df['filler volume fraction'][sample]

def map_viscoelasticity(workbook , sample , tsweep=False , fsweep=False ):
    sheet = workbook['5.2 Properties-Viscoelastic']
    vf = df["filler volume fraction"][sample]
    s = df["sample no."][sample]
    if tsweep:
        sheet["B11"] = "Temperature sweep"
        sheet["C16"] , sheet["D16"] = 5 , "Hz"
        sheet["C15"] = 0.01
        
        if df["pst"][sample] != 'vinyltriethoxysilane':
            
            DF = get_columns_T(vf , pd.read_csv(original_path+"/RawData/DF_N.csv"))
            SM = get_columns_T(vf , pd.read_csv(original_path+ "/RawData/SM_N.csv"))
            LM = get_columns_T(vf , pd.read_csv(original_path + "/RawData/LM_N.csv"))
        
        else:
            DF = get_columns_T(vf , pd.read_csv(original_path + "/RawData/DF_T.csv"))
            SM = get_columns_T(vf , pd.read_csv(original_path + "/RawData/SM_T.csv"))
            LM = get_columns_T(vf , pd.read_csv(original_path+ "/RawData/LM_T.csv"))
            
        DF.columns = ["Temperature (Celsius)" , "Y"]
        SM.columns = ["Temperature (Celsius)" , "Y"]
        LM.columns = ["Temperature (Celsius)" , "Y"]
        DF.to_excel(s+"_dampingfactor.xlsx", index=False)
        sheet["C21"] = s+"_dampingfactor.xlsx"
        SM.to_excel(s+"_storagemod.xlsx" , index=False)
        sheet["C19"] =  s+"_storagemod.xlsx"
        LM.to_excel(s+"_lossmod.xlsx", index=False)
        sheet["C20"] = s+"_lossmod.xlsx"
        return s+"_dampingfactor.xlsx" , s+"_storagemod.xlsx" , s+"_lossmod.xlsx"
        
    if fsweep:
        sheet["B11"] = "Frequency sweep"
        sheet["C16"] , sheet["D16"] = 160 , "Celsius"
        sheet["C15"] = 0.01
        DF = get_columns_F(vf , sample , pd.read_csv(original_path+ "/RawData/DF_NT_frequency.csv"))
        SM = get_columns_F(vf , sample , pd.read_csv(original_path+ "/RawData/SM_NT_frequency.csv"))
        LM = get_columns_F(vf , sample , pd.read_csv(original_path+ "/RawData/LM_NT_frequency.csv"))
        DF.columns = ["Frequency (Hz)" , "Y"]
        SM.columns = ["Frequency (Hz)" , "Y"]
        LM.columns = ["Frequency (Hz)" , "Y"]
        DF.to_excel(s+"_dampingfactor.xlsx", index=False)
        sheet["C21"] = s+"_dampingfactor.xlsx"
        SM.to_excel(s+"_storagemod.xlsx", index=False)
        sheet["C19"] =  s+"_storagemod.xlsx"
        LM.to_excel(s+"_lossmod.xlsx", index=False)
        sheet["C20"] = s+"_lossmod.xlsx"
        return s+"_dampingfactor.xlsx" , s+"_storagemod.xlsx" , s+"_lossmod.xlsx"
    
def map_Tg(workbook ,sample): #fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.4 Properties-Thermal']
    sheet["B9"] = "Temperature for maximum of loss modulus"
    sheet["C26"] = df['Tg'][sample]
    

def copy_image(sample , files): 
    path = os.getcwd()
    for f in files:
        os.rename(os.path.join(path , f), os.path.join(path,sample,f))      
    
def mapping():    #Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['sample no.'].shape[0]
    for i in range( nb_sample):
        if df["pst"][i] == 'vinyltriethoxysilane':
            file = original_path+'/master_template_treated.xlsx'
        elif df["pst"][i] == 'no filler':
            file = original_path+'/master_template_control.xlsx'
        else:
            file = original_path+'/master_template_untreated.xlsx'
            
        workbook = load_workbook(filename=file)    
        map_data_origin(workbook ,i)
        map_material_type(workbook ,i)             
        map_Tg(workbook ,i)
        if df["Viscoelastic"][i] == 'Temperature':
            files = map_viscoelasticity(workbook , i , tsweep=True , fsweep=False )
        else:
            files = map_viscoelasticity(workbook , i , tsweep=False , fsweep=True )
             
        S = df["sample no."][i]
        os.mkdir(S)   
        copy_image(S , files)
        workbook.save(filename=S+'/' + S +'_template.xlsx')
        
        
#%% Launch program    
mapping()
    
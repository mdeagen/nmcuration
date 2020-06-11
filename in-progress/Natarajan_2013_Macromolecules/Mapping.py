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

xl = pd.ExcelFile(original_path+'/Samples_ma302281b.xlsx')
df  = xl.parse(sheet_name=0)
xl = pd.ExcelFile(original_path+'/Reference_Tg_values.xlsx')
df2  = xl.parse(sheet_name=0)



#%% Auxiliary functions

def create_dir(name): #creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path+'/'+name)

def get_abbreviation(sample , component): #gets the abbreviation for a matrix and pst sample
    if component == 'matrix':
        matrix = df['matrix'][sample]
        for i, mat in enumerate(df['chemical name']):
            if mat == matrix:
                k = i
                break
        return df['abbreviation'][k]
    if component == 'pst':
        PST = df['pst'][sample]
        for i, pst in enumerate(df['chemical name']):
            if pst == PST:
                k = i
                break
        return df['abbreviation'][k]
    
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

#%% Mapping
    
def map_data_origin(workbook , sample): #fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['sample no.'][sample]
    
def map_material_type(workbook ,sample):  #fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    sheet["B6"] = df['matrix'][sample]
    sheet["B8"] = get_abbreviation(sample, 'matrix')
    sheet["B48"] = df['pst'][sample]
    sheet["B49"] = get_abbreviation(sample, 'pst')
    sheet["C45"] = df['filler mass fraction'][sample]
    sheet["C15"] = df['Mw'][sample]
    sheet["B13"] = get_manufacturer(sample)

    
def map_synthesis_process(workbook ,sample):  #fill in cells in '3. Synthesis and Processing' sheet for a sample
    sheet = workbook['3. Synthesis and Processing']
    sheet["B47"] = df['annealed'][sample]
    
def map_Tg(workbook ,sample): #fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.4 Properties-Thermal']
    sheet["C26"] = df['delta Tg'][sample] + get_Tg(sample) 
    
def map_microstructre(workbook , sample):
    sheet = workbook['6. Microstructure']
    sheet["B5"] = df['image microstructure file'][sample]

def copy_image(sample): 
    file = str(df['image microstructure file'][sample])
    if file[-1] =='g':
        shutil.copyfile(original_path+"/Images/"+df['image microstructure file'][sample], 'S'+str(sample+1)+"/"+df['image microstructure file'][sample])      
    else:
        pass
    
def mapping():    #Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['sample no.'].shape[0]
    for i in range(nb_sample):
        file = original_path+'/master_template_ma302281b.xlsx'
        workbook = load_workbook(filename=file) 
        
        map_data_origin(workbook ,i)
        map_material_type(workbook ,i)
        map_synthesis_process(workbook ,i)
        map_Tg(workbook ,i)
        map_microstructre(workbook, i)
        
        sample = 'S'+str(i+1)
        os.mkdir(sample)   
        copy_image(i)
        workbook.save(filename=sample+'/S'+str(i+1)+'_template.xlsx')
        
        
#%% Launch program    
mapping()
    
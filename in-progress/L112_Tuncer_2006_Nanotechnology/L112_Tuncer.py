#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 7 14:27:42 2020
@author: harrisondavis
"""

# L112_Tuncer_2006_Nanotechnology

import os, shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

arr = os.listdir('.')
print(arr)
# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/L112_Tuncer_TT.xlsx')
df = xl.parse(sheet_name=0)

l = 0
# %% Auxiliary functions

def create_dir(name):  # creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path + '/' + name)

def get_wt(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['wt'][k]

def get_temp(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Onset Temp'][k]

def get_data(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Datafiles'][k]

# %% Mapping

def map_data_origin(workbook, sample):  # fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['Sample'][sample]
    sheet["B6"] = "S1"


def map_wt(workbook, sample):  # fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    temp = df['wt'][sample]
    if temp > 0:
        sheet["C46"] = df['wt'][sample]
        sheet["B28"] = "Silica"
        sheet["B31"] = "Evonik (Degussa Chemicals), Germany"
        sheet["B32"] = "AEROSIL R812"


def map_loss(workbook, sample):  # fill in cells in '5.3 Properties-Electrical' sheet for a sample
    sheet = workbook['5.3 Properties-Electrical']
    sheet["C25"] = df['Breakdown'][sample]
    sheet["C27"] = df["Datafile"][sample]
    sheet["B29"] = df['Breakdown'][sample]



def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/L112_Tuncer_Master.xlsx'
        workbook = load_workbook(filename=file)

        map_data_origin(workbook, i)
        map_wt(workbook, i)
        map_glass(workbook, i)
        map_loss(workbook, i)

        sample = 'S' + str(i + 1)
        os.mkdir(sample)
        workbook.save(filename=sample + '/S' + str(i + 1) + '_template.xlsx')


    os.chdir(original_path)
    for i in range(nb_sample):
        files = [df['Datafiles'][i]]
        for f in files:
            shutil.copy(f, original_path + '/SUBMISSION' + '/S' + str(i + 1))



# %% Launch program
mapping()
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

# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/L112_Tuncer_TT.xlsx')
df = xl.parse(sheet_name=0)

l = 0
# %% Auxiliary functions

def create_dir(name):  # creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path + '/' + name)

def get_control(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Control'][k]

def get_data(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Datafile'][k]

# %% Mapping

def map_data_origin(workbook, sample):  # fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['Sample'][sample]
    sheet["B6"] = "S1"


def map_control(workbook, sample):  # fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    temp = df['Sample'][sample]
    if temp != "S1":
        sheet["B27"] = "The filler particles are barium titanate and calcium copper titanate. In addition, BTO particles were prepared using conventional solid-state synthesis at Oak Ridge National Laboratory for comparison"
        sheet["B28"] = "Barium titanate"
        sheet["B30"] = "BTO"

def map_data(workbook, sample):  # fill in cells in '5.3 Properties-Electrical' sheet for a sample
    sheet = workbook['5.3 Properties-Electrical']
    sheet["C27"] = df['Datafile'][sample]


def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/L112_Tuncer_Master.xlsx'
        workbook = load_workbook(filename=file)

        map_data_origin(workbook, i)
        map_control(workbook, i)
        map_data(workbook, i)

        sample = 'S' + str(i + 1)
        os.mkdir(sample)
        workbook.save(filename=sample + '/S' + str(i + 1) + '_template.xlsx')


    os.chdir(original_path)
    for i in range(nb_sample):
        files = [df['Datafile'][i]]
        for f in files:
            shutil.copy(f, original_path + '/SUBMISSION' + '/S' + str(i + 1))



# %% Launch program
mapping()
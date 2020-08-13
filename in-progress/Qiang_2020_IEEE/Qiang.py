#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Aug 11 11:04:12 2020
@author: harrisondavis
"""

# Qiang_2020_IEEE

import os, shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/Qiang_2020_TT.xlsx')
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

def get_wt(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['wt'][k]

def get_scale(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Scale Parameter'][k]

def get_shape(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Shape Parameter'][k]

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
    sheet["B6"] = df['Control'][sample]


def map_control(workbook, sample):  # fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    sheet["C46"] = df['wt'][sample]
    temp = df['wt'][sample]
    if temp > 0:
        sheet["B27"] = "The fillers used in the study are commercially available untreated SiO2 fillers provided by Sigma-Aldrich."
        sheet["B30"] = "SiO2"
        sheet["B31"] = "Sigma-Aldrich"

def map_data(workbook, sample):  # fill in cells in '5.3 Properties-Electrical' sheet for a sample
    sheet = workbook['5.3 Properties-Electrical']
    sheet["C27"] = df['Datafile'][sample]
    sheet["B29"] = df['Scale Parameter'][sample]
    sheet["B30"] = df['Shape Parameter'][sample]


def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/Qiang_2020_Master.xlsx'
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
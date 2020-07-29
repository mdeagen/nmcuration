#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 28 11:03:34 2020
@author: harrisondavis
"""

# Bera_2011_TActa

import os, shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/Bera_2011_TActa_Tidy_Table.xlsx')
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

def get_loss(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Weight Loss'][k]


def get_dtg(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['DTG'][k]

def get_glass(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Glass Transition Temp'][k]

# %% Mapping

def map_data_origin(workbook, sample):  # fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['Sample'][sample]


def map_wt(workbook, sample):  # fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    sheet["C46"] = df['wt'][sample]


def map_temp(workbook, sample):  # fill in cells in '3. Synthesis and Processing' sheet for a sample
    sheet = workbook['3. Synthesis and Processing']
    sheet["B49"] = df['Onset Temp'][sample]
    sheet["B56"] = df['DTG'][sample]


def map_glass(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.4 Properties-Thermal']
    sheet["C26"] = df['Glass Transition Temp'][sample]


def map_loss(workbook, sample):  # fill in cells in '5.5 Properties-Volumetric' sheet for a sample
    sheet = workbook['5.5 Properties-Volumetric']
    sheet["C5"] = df['Weight Loss'][sample]


def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/Bera_2011_Master_Template.xlsx'
        workbook = load_workbook(filename=file)

        map_data_origin(workbook, i)
        map_wt(workbook, i)
        map_temp(workbook, i)
        map_glass(workbook, i)
        map_loss(workbook, i)

        sample = 'S' + str(i + 1)
        os.mkdir(sample)
        workbook.save(filename=sample + '/S' + str(i + 1) + '_template.xlsx')


# %% Launch program
mapping()
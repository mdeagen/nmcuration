#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:03:34 2020
@author: harrisondavis
"""

# WangS_2020_IEEE

import os, shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/WangS_2020_IEEE_Tidy_Table.xlsx')
df = xl.parse(sheet_name=0)

l = 0
# %% Auxiliary functions

def create_dir(name):  # creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path + '/' + name)

def get_control(sample, component):  # gets the abbreviation for a matrix and pst sample
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['control'][k]

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
    return df['Temp'][k]

def get_modulus(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['modulus'][k]


def get_breakdown(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['breakdown'][k]


# %% Mapping

def map_data_origin(workbook, sample):  # fill in cells in '1. Data Origin' sheet for a sample
    sheet = workbook['1. Data Origin']
    sheet["B5"] = df['Sample'][sample]
    sheet["B6"] = df['Control Sample'][sample]


def map_wt(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['2. Material Types']
    sheet["C46"] = df['wt'][sample]


def map_temp(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['3. Synthesis and Processing']
    sheet["B48"] = df['Temp'][sample]


def map_modulus(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.1 Properties-Mechanical']
    sheet["C6"] = df['Modulus'][sample]


def map_breakdown(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.3 Properties-Electrical']
    sheet["C25"] = df['Breakdown'][sample]


def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/WangS_2020_IEEE_Master.xlsx'
        workbook = load_workbook(filename=file)

        map_data_origin(workbook, i)
        map_wt(workbook, i)
        map_temp(workbook, i)
        map_modulus(workbook, i)
        map_breakdown(workbook, i)

        sample = 'S' + str(i + 1)
        os.mkdir(sample)
        workbook.save(filename=sample + '/S' + str(i + 1) + '_template.xlsx')


# %% Launch program
mapping()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur July 30 16:23:42 2020
@author: harrisondavis
"""

# Koerner_2005_TActa

import os, shutil
from openpyxl import load_workbook
import pandas as pd

original_path = os.getcwd()

# %% Load spreadsheet with data for all samples

xl = pd.ExcelFile(original_path + '/Koerner_2005_Polymer_Tidy_Table.xlsx')
df = xl.parse(sheet_name=0)

l = 0
# %% Auxiliary functions

def create_dir(name):  # creates a directory and change the location to it
    path = os.getcwd()
    os.mkdir(name)
    os.chdir(path + '/' + name)


def get_vt(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Volume Fraction'][k]

def get_E(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Youngs Moduli'][k]

def get_ys(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Yield Stress'][k]

def get_ye(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Yield Elongation'][k]

def get_rs(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Rupture Stress'][k]

def get_re(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Rupture Elongation'][k]

def get_bulk(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Bulk Conductivity'][k]

def get_melt(sample):
    matrix = df['matrix'][sample]
    for i, mat in enumerate(df['chemical name']):
        if mat == matrix:
            k = i
            break
    return df['Melting Enthalpy'][k]

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


def map_vt(workbook, sample):  # fill in cells in '2. Material Types' sheet for a sample
    sheet = workbook['2. Material Types']
    temp = df['Volume Fraction'][sample]
    if temp > 0:
        sheet["C46"] = df['Volume Fraction'][sample]
        sheet["B27"] = "Carbon Nanotubes"
        sheet["B28"] = "CNT"

def map_synth(workbook, sample):  # fill in cells in '3. Synthesis and Processing' sheet for a sample
    sheet = workbook['3. Synthesis and Processing']
    sheet["B8"] = 'After short, light grinding of the carbon nanotubes (PRT-HT-19, Applied Science Inc.) with a mortar and pestle, they are combined with a small amount of polymer (Morthane PS455-203, Huntsman Polyurethanes, aromatic polyester based thermoplastic polyurethane) in a polar medium, such as THF, for several hours [9].'
    sheet["B15"] = 'THF'


def map_mech(workbook, sample):  # fill in cells in '5.1 Properties-Mechanical' sheet for a sample
    sheet = workbook['5.1 Properties-Mechanical']
    sheet["G8"] = df['Datafiles'][sample]
    sheet["C6"] = df['Youngs Moduli'][sample]
    sheet["C7"] = df['Rupture Stress'][sample]
    sheet["C8"] = df['Yield Stress'][sample]
    sheet["C12"] = df['Rupture Elongation'][sample]
    sheet["C13"] = df['Yield Elongation'][sample]


def map_elec(workbook, sample):  # fill in cells in '5.3 Properties-Electrical' sheet for a sample
    sheet = workbook['5.3 Properties-Electrical']
    sheet["C5"] = df['Bulk Conductivity'][sample]


def map_therm(workbook, sample):  # fill in cells in '5.4 Properties-Thermal' sheet for a sample
    sheet = workbook['5.4 Properties-Thermal']
    sheet["C22"] = df['Melting Enthalpy'][sample]


def mapping():  # Fill in every cell for every sample
    create_dir('SUBMISSION')
    nb_sample = df['Sample'].shape[0]
    for i in range(nb_sample):
        file = original_path + '/Koerner_2005_Polymer_Master.xlsx'
        workbook = load_workbook(filename=file)

        map_data_origin(workbook, i)
        map_vt(workbook, i)
        map_elec(workbook,i)
        map_mech(workbook, i)
        map_therm(workbook, i)

        sample = 'S' + str(i + 1)
        os.mkdir(sample)
        workbook.save(filename=sample + '/S' + str(i + 1) + '_template.xlsx')


# %% Launch program
mapping()
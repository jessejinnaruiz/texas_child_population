#!/usr/bin/env python
"""
This script contains code used by the following jupytr notebooks or python scripts:
1. 
2. 
"""
# ===========
# ENVIRONMENT
# ===========

import os
import sys
import pandas as pd
from env import path
from env import file1
from env import file2
from env import fipsfile
from env import usbp_uac
from env import census

def get_population_data():
    dfps = pd.read_csv(path+file1, sep= ',', header=0)
    return dfps

def get_fips_codes():
    fips = pd.read_csv(path+fipsfile)
    return fips

def get_bp_data():
    uac = pd.read_csv(path+usbp_uac)
    return uac

def get_dfps_data():
    dfps_case = pd.read_csv(path+file2)
    return dfps_case

def get_census_data():
    census1 = pd.read_csv(path+census)
    return census1
# ===========
# ENVIRONMENT
# ===========

import pandas as pd
import numpy as np
import acquire

dfps = acquire.get_population_data()

def fix_col_names(df):
    df = df.rename(str.lower, axis='columns')
    return df

def rename_dfps_cols(dfps):
    dfps = dfps.rename(columns={'child population': 'child_pop', 
    '% of children in total population': 'perct_children', 'total population': 'tot_pop'})
    return dfps

def fix_counties(df):
    '''This function takes a column named county in a dataframe and changes the string values to lowercase and removes spaces for consistency. Returns df'''
    df['county'] = df['county'].str.lower().str.replace(' ', '')
    return df

def fix_mclennan_typo(df):
    df.county = df.county.str.replace('mclennon', 'mclennan')
    return df

def fix_dates(df):
    df.year = pd.to_datetime(df['year'].astype('str'), format='%Y')
    df = df.rename(columns={'year': 'datetime'})
    df['year'] = df['datetime'].dt.year
    return df

def fix_region(df):
    df['region_id'] = df.region.str.split(pat='-', n=1, expand=True)[0]
    df.region =  df.region.str.split(pat='-', n=1, expand=True)[1]
    df = df.drop('region_id', axis=1)
    return df

def drop_agg_counties(df):
    agg_index = list(df[df['child_pop'].isnull()].index)
    df = df.drop(df.index[[agg_index]])
    return df

# -*- coding: utf-8 -*-

import pandas as pd


## create empty df

df = pd.DataFrame()


# create a column

df['name'] = ['Adam', 'Xavier', 'Ada']
df['employed'] = ['Yes', 'Yes', 'No']
df['age'] = [32,32,21]

## create a function

def mean_age_by_group(dataframe,col):
    #groups the data by a column and return mean age per group
    return dataframe.groupby(col).mean()

## create a function

def uppercase_column_name(dataframe):
    # cap all the column headers
    dataframe.columns = dataframe.columns.str.upper()
    # return dataframe
    return dataframe

# create a pipeline that applies botg functions
(df.pipe(mean_age_by_group,col='employed')
    # then apply uppercase function
    .pipe(uppercase_column_name))
    
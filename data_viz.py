import pandas as pd
# import numpy as np
import sqlite3
import plotly.express as px


def viz():
    con = sqlite3.connect('e_chem.db')
    df0 = pd.read_sql('SELECT * FROM bathes_percents', con)
    df1 = pd.read_sql('SELECT * FROM bathes', con)
    df2 = pd.read_sql('SELECT * FROM dosing', con)
    df3 = pd.read_sql('SELECT * FROM drains', con)
    df4 = pd.read_sql('SELECT * FROM substance', con)

    dic_col_rename = {df4.sub_num.to_list()[i] : df4.name.to_list()[i] for i in range(len(df4.sub_num.to_list()))}
    df0 = df0.rename(columns = dic_col_rename).drop(columns = [None], axis = 1)
    df1 = df1.rename(columns = dic_col_rename).drop(columns = [None], axis = 1)
    df2 = df2.rename(columns = dic_col_rename).drop(columns = [None], axis = 1)
    df3 = df3.rename(columns = dic_col_rename).drop(columns = [None], axis = 1)


if '__name__' == 'main':
    viz()
"""
Módulo encargado de mostrar dataframe crudo.
"""

import pandas as pd

def mostrar_dataframe(df):
    print(df.head())
    print("="*20)
    print(df.info())
    print(df.describe())
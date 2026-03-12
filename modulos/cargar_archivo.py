"""
Módulo encargado de cargar el archivo de datos y retornarlo como una variable.
"""
import pandas as pd

def cargar_csv():
    df = pd.read_csv("ai_job_replacement_dirty.csv")
    return df 

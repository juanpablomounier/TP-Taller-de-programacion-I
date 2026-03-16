"""
Módulo encargado de cargar el archivo de datos y retornarlo como una variable.
"""
import pandas as pd

def cargar_xlsx():
    df = pd.read_excel("datos/crudos/ai_job_replacement.xlsx")
    return df 

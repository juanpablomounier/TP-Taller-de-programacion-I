"""
Módulo encargado de limpiar dataframe.
"""

import pandas as pd

def limpiar_dataset(df, industria):
    df = discriminar_industria(df, industria)
    df = eliminar_variables_similares(df)
    df = eliminar_variables_innecesarias(df)
    df = redondear_variables(df)
    return df

################################################

def discriminar_industria(df, industria):
    print(f"Industria analizada: {industria}\n")
    health_df = df[df["industry"] == industria]
    return health_df

def eliminar_variables_similares(df):
    correlacion_riesgos = df["automation_risk_percent"].corr(df["ai_replacement_score"])
    #print(f"La correlacion de riesgo y puntaje de reemplazo es {correlacion_riesgo}")
    if correlacion_riesgos >= 0.8:
        df = df.drop(columns=["automation_risk_percent", "ai_disruption_intensity"])
    correlacion_adaptacion = df["skill_transition_pressure"].corr(df["reskilling_urgency_score"])
    #print(f"La correlacion de presion de transisión y readaptación es {correlacion_adaptacion}")
    if correlacion_adaptacion >= 0.8:
        df = df.drop("skill_transition_pressure", axis = 1)
    return df

def eliminar_variables_innecesarias(df):
    df = df.drop(columns =["automation_risk_category", "job_id", "remote_feasibility_score", "wage_volatility_index"])
    return df

def redondear_variables(df):
    columnas_numericas = df.select_dtypes(include=['number']).columns
    df[columnas_numericas] = df[columnas_numericas].round(2)
    return df
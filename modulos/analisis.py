"""
Módulo encargado de realizar los análisis.

Análisis 1: **Correlación Educación-Riesgo**: Calculen el coeficiente de correlación entre `education_requirement_level` y `ai_replacement_score`.

Análisis 2: **Análisis de Demandas**: Determinen qué tipo de roles presentan la mayor "Urgencia de Re-capacitación" y si estos coinciden con los de salarios más bajos.

Análisis 3: **Filtros Temporales**: Realicen un análisis comparativo centrado en el periodo post-pandemia (2022 en adelante).

"""

def analizar_dataframe(df):
    correlacion_educacion_riesgo = analizar_correlacion(df)
    recapacitacion_urgente, correlacion_recapacitacion_salario = analizar_recapacitacion(df)
    recapacitacion_post, correlacion_post = analizar_post_pandemia(df)
    analisis_periodos = analizar_periodos(recapacitacion_urgente, recapacitacion_post)
    return correlacion_educacion_riesgo, recapacitacion_urgente, correlacion_recapacitacion_salario, recapacitacion_post, correlacion_post, analisis_periodos

#####################################################################

def analizar_correlacion(df):
    correlacion_educacion_riesgo = df["education_requirement_level"].corr(df["ai_replacement_score"])
    return correlacion_educacion_riesgo

def analizar_recapacitacion(df):
    promedio_recapacitacion = df.groupby("job_role")["reskilling_urgency_score"].mean()
    recapacitacion_urgente = promedio_recapacitacion.sort_values(ascending=False)
    salario_medio_rol = df.groupby("job_role")[["salary_before_usd", "salary_after_usd"]].mean()
    salario_medio_rol["salary_mean"] = (salario_medio_rol["salary_before_usd"] + salario_medio_rol["salary_after_usd"]) / 2
    df_final = salario_medio_rol.join(promedio_recapacitacion)
    correlacion_recapacitacion_salario = df_final["reskilling_urgency_score"].corr(df_final["salary_mean"])
    return recapacitacion_urgente, correlacion_recapacitacion_salario

def analizar_post_pandemia(df):
    df_post = df[df["year"] >= 2022].copy()
    recapacitacion_post, correlacion_post = analizar_recapacitacion(df_post)
    return recapacitacion_post, correlacion_post

def analizar_periodos(recapacitacion_urgente_pre, recapacitacion_urgente_post):
    recapacitacion_urgente_pre, recapacitacion_urgente_post = recapacitacion_urgente_pre.align(recapacitacion_urgente_post, join="inner")
    comparacion_recapacitacion = recapacitacion_urgente_pre.corr(recapacitacion_urgente_post)
    return comparacion_recapacitacion

    
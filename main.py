import pandas as pd 
from  modulos import cargar_archivo, mostrar_df_crudo, limpiar_dataframe, analisis

df = cargar_archivo.cargar_xlsx()
mostrar_df_crudo.mostrar_dataframe(df)
df_definitivo = limpiar_dataframe.limpiar_dataset(df, "Healthcare")
df_definitivo.to_excel('datos/limpios/dataframe definitivo.xlsx', index=False)
correlacion_educacion_riesgo, recapacitacion_urgente, correlacion_recapacitacion_salario, analisis_post_pandemia, correlacion_post, analisis_periodos = analisis.analizar_dataframe(df_definitivo)
print(df_definitivo)
print(f"La correlación educación-riesgo es: {round(correlacion_educacion_riesgo, 2)}\n")
print(f"Top 5 roles con mayor recapacitación:\n{recapacitacion_urgente.head()}")
print(f"La correlación capacitación-salario es: {round(correlacion_recapacitacion_salario, 2)}\n")
print(f"Para el período post pandemia: \n{analisis_post_pandemia} \n donde la correlación es: {round(correlacion_post, 2)}\n")
print(f"La relación pre y post pandemia es: {round(analisis_periodos,2)}\n")




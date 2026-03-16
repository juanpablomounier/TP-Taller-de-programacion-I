# Trabajo Práctico: Impacto de la IA en el Empleo (2020-2026)
## Sector Asignado: Salud (Healthcare)

### 1. Introducción Académica
El avance de la Inteligencia Artificial no es solo un fenómeno técnico, sino una fuerza socioeconómica que está redefiniendo la naturaleza del trabajo. En los próximos años, diversos sectores experimentarán cambios sin precedentes en sus estructuras salariales, demandas de habilidades y estabilidad laboral. Este Trabajo Práctico propone analizar estas tendencias con rigor científico y pensamiento crítico.

### 2. Ficha del Proyecto: Grupo 3
*   **Sector**: Salud.
*   **Objetivo General**: Investigar la relación entre el nivel educativo y el riesgo de automatización en salud, determinando si la formación académica actúa como barrera protectora frente a la IA.

### 3. Fase I: Diagnóstico y Saneamiento (Caja Negra)
Ustedes trabajarán con la fuente de datos `ai_job_replacement_dirty.csv`. **Advertencia**: La fuente posee anomalías estructuradas.
- **Auditoría de Calidad**: Realicen un reporte inicial sobre el estado de la información. Deben identificar inconsistencias lógicas, errores de formato y vacíos de datos sin guía externa.
- **Protocolo de Curación**: Implementen y documenten un proceso sistemático de limpieza. Cada decisión (casteo de tipos, manejo de nulos, eliminación de duplicados) debe estar técnicamente justificada en su bitácora.
- **Normalización**: Traduzcan y estandaricen los campos para asegurar una lectura fluida en español.

### 4. Fase II: Análisis Estadístico y Exploratorio (EDA)
Utilizando las librerías Pandas y NumPy, resuelvan las siguientes problemáticas:
- **Correlación Educación-Riesgo**: Calculen el coeficiente de correlación entre `education_requirement_level` y `ai_replacement_score`.
- **Análisis de Demandas**: Determinen qué tipo de roles presentan la mayor "Urgencia de Re-capacitación" y si estos coinciden con los de salarios más bajos.
- **Filtros Temporales**: Realicen un análisis comparativo centrado en el periodo post-pandemia (2022 en adelante).

### 5. Fase III: Visualización y Comunicación
Diseñen las siguientes piezas utilizando Matplotlib:
- **Boxplot Salarial**: Gráfico de cajas para comparar la dispersión de salarios pre y post IA en el sector salud.
- **Scatter Plot**: Relación entre el riesgo de automatización y el crecimiento de la demanda de habilidades.
- **Gráfico de Barras**: Top 5 de países con mayor adopción de IA en el sector salud.

### 6. Fase IV: Reflexión Crítica (Anti-LLM)
*Responda basándose estrictamente en los hallazgos de su procesamiento de datos:*
- ¿Sugieren los datos que la salud es un sector "seguro" para trabajadores con baja formación académica?
- Si tuviera que proponer una nueva habilidad obligatoria para los médicos del futuro basándose en la "brecha de habilidades" actual, ¿cuál sería?

### 7. Requerimientos de Entrega y Defensa
1.  **Informe Profesional**: PDF o Markdown con resumen ejecutivo, bitácora de saneamiento e interpretación de resultados.
2.  **Código Fuente**: Script o Notebook estructurado, comentado y reproducible.
3.  **Defensa Oral**: Justificación técnica de la limpieza e interpretación de las visualizaciones ante el curso.




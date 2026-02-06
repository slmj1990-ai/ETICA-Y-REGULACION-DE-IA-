Ética, Regulación y Producción Científica en Inteligencia Artificial

Descripción del Proyecto

Este proyecto analiza la relación entre la producción científica en inteligencia artificial (IA), la regulación y gobernanza pública, y las consideraciones éticas asociadas a su uso, tanto a nivel país como por sector de aplicación.

A partir de datos abiertos y APIs públicas, se investiga si los países que lideran la investigación en IA también desarrollan marcos regulatorios más sólidos, y cómo se distribuyen las preocupaciones éticas en distintos sectores como salud, finanzas o educación.

El proyecto combina ingeniería de datos, consumo de APIs, limpieza de datos y análisis exploratorio, con un enfoque transversal en ética y políticas públicas de IA.


 Preguntas de Investigación

¿Los países con mayor producción científica en IA también tienen más políticas de gobernanza?

¿Existe una relación entre desarrollo económico y regulación de la IA?

¿Qué sectores presentan mayor concentración de consideraciones éticas?

¿Existen brechas entre innovación, regulación y ética?


 Estructura del Proyecto

project/
│
├── data/
│   ├── raw/
│   │   ├── oecd_ai_policies.csv
│   │   └── etica_ia.csv
│   │
│   └── processed/
│       ├── oecd_ai_policies_clean.csv
│       ├── etica_ia_clean.csv
│       ├── worldbank_gdp.csv
│       └── openalex_ai.csv
│
├── notebooks/
│   ├── code.ipynb        # Análisis principal y visualizaciones
│   └── APIs.ipynb        # Extracción de datos desde APIs
│
├── values/
│   ├── cleaning.py       # Funciones de limpieza de datos
│   └── functions.py     # Funciones auxiliares de análisis
│
└── README.md


Fuentes de Datos

OECD AI Policy Observatory

Políticas públicas, estrategias nacionales y gobernanza en IA

Fuente: OCDE (archivo CSV)


2.  OpenAlex API

Producción científica relacionada con inteligencia artificial

Utilizada para medir el volumen de publicaciones por país


3.  World Bank API

Indicadores económicos (PIB per cápita)

Usada para contextualizar el nivel de desarrollo económico


4. Dataset de Ética en IA (por sector)

Dimensiones éticas de sistemas de IA según sector de aplicación

Sectores como salud, finanzas, educación, seguridad, etc.

Enfoque exploratorio y comparativo


 Metodología

Limpieza y normalización de datos con pandas

Estandarización de:

Nombres de columnas

Nombres de países

Formatos temporales

Eliminación de duplicados

Agregación por país y sector

Análisis exploratorio de datos (EDA)

Visualización con Matplotlib y Seaborn


Comparaciones principales:

Producción científica vs gobernanza en IA

Regulación vs desarrollo económico

Distribución ética por sector


Principales Resultados

Existe una relación positiva general entre producción científica en IA y número de políticas de gobernanza.

La relación no es lineal: algunos países investigan intensamente sin una regulación equivalente.

Los países con mayor PIB per cápita tienden a presentar más políticas en IA, aunque hay excepciones.

Las consideraciones éticas no se distribuyen homogéneamente entre sectores:

Salud y finanzas concentran mayor atención ética.

Sectores comerciales y de marketing muestran menor énfasis.

La mayoría de las políticas identificadas corresponden a soft governance (marcos, guías, principios) y no a regulación vinculante.



 Limitaciones del Estudio

Información incompleta del país de afiliación en algunas publicaciones científicas

Definiciones heterogéneas de “regulación” entre datasets

El dataset ético no constituye un estándar regulatorio oficial

La producción científica se mide por volumen, no por impacto o calidad

Estas limitaciones se tienen en cuenta en la interpretación de resultados.


Tecnologías Utilizadas

Python

pandas

NumPy

Matplotlib

Seaborn

REST APIs

Jupyter Notebook




Trabajo Futuro

Análisis temporal de la evolución regulatoria

Diferenciación entre regulación dura y soft governance

Inclusión de métricas de calidad científica (citaciones)

Análisis ético comparativo por país



:D Autora
Sara Leticia Marín Jáuregui
Estudiante de Análisis de Datos
Proyecto desarrollado con fines académicos y de portafolio

 Licencia

Este proyecto tiene fines educativos.
Los datos pertenecen a sus respectivas fuentes (OCDE, Banco Mundial, OpenAlex).

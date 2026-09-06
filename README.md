# Detección de Fallas en Maquinaria Industrial con Machine Learning
Aprendizaje de Máquina — Universidad Industrial de Santander (UIS).
## Integrantes
- Lesly Gabriela Rodriguez 2251510
- Maria Jose Chavez Torres 2251727

## Descripción
En la industria moderna, las fallas inesperadas en maquinaria generan altos costos de producción, tiempos de parada no planificados y riesgos de seguridad. El mantenimiento predictivo busca anticipar estas fallas antes de que ocurran, utilizando datos de sensores y modelos de aprendizaje automático para identificar patrones que indican un posible mal funcionamiento.

Este proyecto, tiene como objetivo aplicar técnicas de clasificación para predecir si una máquina va a fallar y, en caso de falla, identificar el tipo de falla, a partir de variables como temperatura, velocidad rotacional, torque y desgaste de la herramienta.

## Dataset
Se utiliza el dataset [Machine Predictive Maintenance Classification](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification) de Kaggle, compuesto por 10,000 registros y 10 variables, incluyendo mediciones de temperatura del aire y del proceso, velocidad rotacional, torque y desgaste de herramienta, junto con la variable objetivo que indica si hubo falla y de qué tipo.
## Estructura del repositorio
```
├── data/           # Dataset original
├── notebooks/      # Notebooks de análisis y modelado
├── informe/        # Informe en LaTeX
├── README.md
```

## Metodología
1. Análisis exploratorio de datos (EDA)
2. Modelos Supervisados
3. Modelos no Supervisados
4. Evaluación de resultados

## Herramientas Usadas
- Python
    - Pandas
    - scikit-learn
    - Matplotib
    - Seaborn


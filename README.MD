# University Ranking Risk Analysis

This project analyzes the risk of universities' rankings fluctuating using a Monte Carlo simulation approach. The analysis involves pre-processing data, running simulations, and visualizing the results.

## Project Structure

- `preprocesamiento.py`: Contains functions for data loading, cleaning, and preparation.
- `montecarlo.py`: Implements the Monte Carlo simulation for ranking changes and identifies universities at risk.
- `app.py`: Main script to execute the entire process, from data loading to visualization.
- `requirements.txt`: List of Python dependencies required to run the project.

## Features

1. **Data Preprocessing**:
   - Load and clean data from a CSV file.
   - Remove unwanted characters and fill missing values.
   - Clean up column names.

2. **Monte Carlo Simulation**:
   - Simulate possible changes in university rankings based on selected metrics.
   - Identify universities with the highest risk of rank fluctuation.

3. **Visualization**:
   - Generate a bar plot showing universities with the highest risk of rank fluctuations.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/university-ranking-risk-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd university-ranking-risk-analysis
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the analysis, simply execute the `app.py` script:
bash

python app.py
This will process the data, run the Monte Carlo simulations, and generate the output files and visualizations.

##  Output Files
./data/universities_processed.csv: Processed university data.
./data/rank_changes.csv: Results from the Monte Carlo simulations.
./data/risk_universities.csv: List of universities identified as high risk.
./data/risk_universities_plot.png: Bar plot showing the universities with the highest risk of rank fluctuation.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.


### README.md in Spanish

```markdown
# Análisis de Riesgo en el Ranking de Universidades

Este proyecto analiza el riesgo de fluctuación en los rankings de universidades utilizando un enfoque de simulación de Monte Carlo. El análisis incluye la pre-procesamiento de datos, la ejecución de simulaciones y la visualización de los resultados.

## Estructura del Proyecto

- `preprocesamiento.py`: Contiene funciones para la carga, limpieza y preparación de datos.
- `montecarlo.py`: Implementa la simulación de Monte Carlo para cambios en los rankings e identifica universidades en riesgo.
- `app.py`: Script principal que ejecuta todo el proceso, desde la carga de datos hasta la visualización.
- `requirements.txt`: Lista de dependencias de Python necesarias para ejecutar el proyecto.

## Características

1. **Preprocesamiento de Datos**:
   - Carga y limpia datos desde un archivo CSV.
   - Elimina caracteres no deseados y rellena valores faltantes.
   - Limpia los nombres de las columnas.

2. **Simulación de Monte Carlo**:
   - Simula posibles cambios en los rankings de universidades basados en métricas seleccionadas.
   - Identifica universidades con mayor riesgo de fluctuación en su ranking.

3. **Visualización**:
   - Genera un gráfico de barras que muestra las universidades con mayor riesgo de fluctuación en su ranking.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/yourusername/university-ranking-risk-analysis.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd university-ranking-risk-analysis
    ```

3. Instala los paquetes de Python requeridos:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el análisis, simplemente ejecuta el script `app.py`:
bash
python app.py

Esto procesará los datos, ejecutará las simulaciones de Monte Carlo y generará los archivos de salida y visualizaciones.

## Archivos de Salida
./data/universities_processed.csv: Datos de universidades procesados.
./data/rank_changes.csv: Resultados de las simulaciones de Monte Carlo.
./data/risk_universities.csv: Lista de universidades identificadas como de alto riesgo.
./data/risk_universities_plot.png: Gráfico de barras que muestra las universidades con mayor riesgo de fluctuación en su ranking.

## Contribuir
¡Las contribuciones son bienvenidas! Por favor, haz un fork del repositorio y envía un pull request con tus mejoras.

Licencia
Este proyecto está bajo la licencia MIT.
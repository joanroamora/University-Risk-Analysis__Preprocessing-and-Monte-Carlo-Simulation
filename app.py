from preprocesamiento import load_data, clean_plus_signs, fill_missing_values, clean_column_names, save_data
from montecarlo import simulate_rank_changes, identify_risk_universities, plot_top_risk_universities

def main():
    input_filepath = './data/universities.csv'
    
    print("Cargando los datos...")
    df = load_data(input_filepath)
    
    print("Eliminando signos '+' y limpiando los datos...")
    df_cleaned = clean_plus_signs(df)
    
    print("Llenando los valores faltantes...")
    df_filled = fill_missing_values(df_cleaned)
    
    print("Verificando y limpiando nombres de columnas...")
    df_final = clean_column_names(df_filled)
    
    processed_filepath = './data/universities_processed.csv'
    print(f"Guardando el DataFrame procesado en '{processed_filepath}'...")
    save_data(df_final, processed_filepath)
    
    metrics_to_simulate = ['ar score', 'er score', 'fsr score']
    
    print("Realizando simulaciones de Montecarlo...")
    rank_changes = simulate_rank_changes(df_final, metrics_to_simulate)
    
    print("Identificando universidades en riesgo de cambiar de posición...")
    risk_universities = identify_risk_universities(rank_changes)
    
    rank_changes_filepath = './data/rank_changes.csv'
    risk_universities_filepath = './data/risk_universities.csv'
    
    print(f"Guardando los resultados de la simulación en '{rank_changes_filepath}'...")
    rank_changes.to_csv(rank_changes_filepath, index=False)
    
    print(f"Guardando las universidades en riesgo en '{risk_universities_filepath}'...")
    risk_universities.to_csv(risk_universities_filepath, index=False)
    
    print("Generando gráfico de las universidades con mayor riesgo de fluctuación...")
    plot_top_risk_universities(rank_changes)
    
    print("Proceso completado.")

if __name__ == "__main__":
    main()

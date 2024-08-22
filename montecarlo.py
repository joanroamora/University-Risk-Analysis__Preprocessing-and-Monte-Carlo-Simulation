import numpy as np
import pandas as pd

def simulate_rank_changes(df, metric_columns, num_simulations=1000, std_dev=0.02):
    rank_changes = pd.DataFrame(index=df.index)
    
    for metric in metric_columns:
        simulated_ranks = np.zeros((df.shape[0], num_simulations))
        
        for i in range(num_simulations):
            # Simular fluctuaciones en la métrica actual
            simulated_metric = df[metric] + np.random.normal(0, std_dev, df.shape[0])
            
            # Recalcular el ranking basado en la métrica simulada
            simulated_ranks[:, i] = simulated_metric.rank(ascending=False)
        
        # Calcular el ranking promedio y la desviación estándar de las simulaciones
        rank_changes[f'{metric}_mean_rank'] = simulated_ranks.mean(axis=1)
        rank_changes[f'{metric}_std_rank'] = simulated_ranks.std(axis=1)
    
    return rank_changes

def identify_risk_universities(rank_changes, threshold=1.5):
    risk_universities = rank_changes[rank_changes.filter(like='_std_rank').max(axis=1) > threshold]
    return risk_universities

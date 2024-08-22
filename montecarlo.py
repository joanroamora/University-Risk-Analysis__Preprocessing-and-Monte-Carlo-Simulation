import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_rank_changes(df, metric_columns, num_simulations=1000, std_dev=0.02):
    rank_changes = pd.DataFrame(index=df.index)
    
    for metric in metric_columns:
        simulated_ranks = np.zeros((df.shape[0], num_simulations))
        
        for i in range(num_simulations):
            simulated_metric = df[metric] + np.random.normal(0, std_dev, df.shape[0])
            simulated_ranks[:, i] = simulated_metric.rank(ascending=False)
        
        rank_changes[f'{metric}_mean_rank'] = simulated_ranks.mean(axis=1)
        rank_changes[f'{metric}_std_rank'] = simulated_ranks.std(axis=1)
    
    return rank_changes

def identify_risk_universities(rank_changes, threshold=1.5):
    risk_universities = rank_changes[rank_changes.filter(like='_std_rank').max(axis=1) > threshold]
    return risk_universities

def plot_top_risk_universities(rank_changes, top_n=10, output_filepath='./data/risk_universities_plot.png'):
    std_columns = rank_changes.filter(like='_std_rank')
    std_columns['mean_std'] = std_columns.mean(axis=1)
    
    top_risk_universities = std_columns.nlargest(top_n, 'mean_std')
    
    ax = top_risk_universities.drop(columns='mean_std').plot(kind='bar', stacked=True, figsize=(12, 8))
    ax.set_title(f'Top {top_n} Universities with Highest Risk of Rank Fluctuation')
    ax.set_ylabel('Standard Deviation of Rank')
    ax.set_xlabel('University Index')
    ax.legend(title='Metric')
    
    plt.tight_layout()
    plt.savefig(output_filepath)
    plt.close()

    print(f"Gráfico guardado en '{output_filepath}'")

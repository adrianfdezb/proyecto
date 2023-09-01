import pandas as pd
import numpy as np

def scatter_plot_price_distance():
    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
    
    return chart_data
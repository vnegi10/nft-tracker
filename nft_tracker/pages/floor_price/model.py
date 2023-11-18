import plotly.graph_objects as go
from utils.data import get_nft_hist
import pandas as pd
pd.options.plotting.backend = "plotly"

def plot_nft_hist(nft_id, num_days):
    df_hist = get_nft_hist(nft_id, num_days)
    fig = df_hist.plot(title = f"Historical floor price for {nft_id}",
                       template = "seaborn",
                       labels = dict(index = "Time", value = "Price [USD]"))
    fig = go.Figure(fig)
    return fig
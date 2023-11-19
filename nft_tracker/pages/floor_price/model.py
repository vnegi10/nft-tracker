import plotly.graph_objects as go
from utils.data import get_nft_hist, get_nft_markets
import plotly.express as px
import pandas as pd

def plot_nft_hist(nft_id, num_days):
    df_hist = get_nft_hist(nft_id, num_days)
    fig = px.line(df_hist,
                  x = "Time",
                  y = "Price_usd",
                  title = f"Historical floor price for {nft_id}",
                  labels = dict(index = "Time", value = "Price [USD]"),
                  markers = True)
    fig = go.Figure(fig)
    return fig

def plot_nft_markets(order_by, num_entries):
    df_nft_markets = get_nft_markets(order_by, num_entries)
    fig = px.bar(df_nft_markets,
                 x = "id",
                 y = "floor_price_usd",
                 color = "asset_platform_id")
    fig = go.Figure(fig)
    return fig
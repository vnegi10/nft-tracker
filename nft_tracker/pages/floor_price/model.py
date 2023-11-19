import plotly.graph_objects as go
from utils.data import get_nft_hist, get_nft_markets
import plotly.express as px
from plotly.subplots import make_subplots

def plot_nft_hist(nft_id, num_days):
    df_hist = get_nft_hist(nft_id, num_days)
    fig = px.line(df_hist,
                  x = "Time",
                  y = "Price_usd",
                  labels = dict(index = "Time", value = "Price [USD]"),
                  markers = True)
    fig = go.Figure(fig)

    fig.update_layout(title_text = f"Historical floor price for {nft_id}",
                      title_x = 0.5)

    return fig

def plot_nft_markets(order_by, num_entries):
    df_nft_markets = get_nft_markets(order_by, num_entries)
    fig = make_subplots(rows=2,
                        cols=1,
                        subplot_titles = ("Floor price [USD]", \
                                          "Floor price [USD] 24-hour % change")
                        )

    fig.add_trace(go.Bar(
                  x = df_nft_markets.id,
                  y = df_nft_markets.floor_price_usd),
                  row = 1, col = 1)
    
    fig.add_trace(go.Bar(
                  x = df_nft_markets.id,
                  y = df_nft_markets.floor_price_change),
                  row = 2, col = 1)
    
    fig.update_layout(height = 750,
                      width = 1250,
                      title_text = "Prices compared for different NFTs",
                      title_x = 0.5)
    
    return fig
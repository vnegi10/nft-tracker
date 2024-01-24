import plotly.graph_objects as go
from utils.data import get_nft_hist, get_nft_markets
from utils.helpers import set_colors, send_price_alert
import plotly.express as px
from plotly.subplots import make_subplots

def plot_nft_hist(nft_id, num_days, window_size):
    df_hist = get_nft_hist(nft_id, num_days, window_size)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
                  x = df_hist['Time'],
                  y = df_hist['Price_usd'],
                  mode = 'lines+markers',
                  name = 'Daily price'))
        
    fig.add_trace(go.Scatter(
                  x = df_hist['Time'],
                  y = df_hist['SMA'],
                  mode = 'lines',
                  name = 'Simple Moving Average'))
    
    fig.add_trace(go.Scatter(
                  x = df_hist['Time'],
                  y = df_hist['EMA'],
                  line = dict(dash='dot'),
                  name = 'Exponential Moving Average'))
    
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
    
    Y = df_nft_markets.floor_price_change
    fig.add_trace(go.Bar(
                  x = df_nft_markets.id,
                  y = Y,
                  marker_color = set_colors(Y)),
                  row = 2, col = 1)
    
    fig.update_layout(height = 750,
                      width = 1250,
                      title_text = "Prices compared for different NFTs",
                      title_x = 0.5)
    
    return fig

def send_email(nft_id, num_days, window_size):

    df_hist = get_nft_hist(nft_id, num_days, window_size)

    if df_hist['Price_usd'].iloc[-1] > df_hist['SMA'].iloc[-1]:
        body = f"Current price is higher than {window_size}-day SMA"
    else:
        body = f"Current price is lower than {window_size}-day SMA"

    try:
        send_price_alert('vikas.negi10@gmail.com', 'NFT Tracker', body)
    except Exception as e:
        print(f"Unable to send the alert email: {e}")
from pages.floor_price.view import app
from dash.dependencies import Input, Output
from pages.floor_price.model import plot_nft_hist, plot_nft_markets

@app.callback(
              Output(component_id = 'plot', component_property = 'figure'),
              Input(component_id = 'MODE', component_property= 'value'),
              Input(component_id = 'NFT_ID', component_property= 'value'),
              Input(component_id = 'DURATION', component_property= 'value'),
              Input(component_id = 'WINDOW_SIZE', component_property= 'value'),
              Input(component_id = 'ORDER_BY', component_property= 'value'),
              Input(component_id = 'NUM_ENTRIES', component_property= 'value'),
              )
def graph_update(mode, nft_id, duration, window_size, order_by, num_entries):

    if mode == "market_data":
        return plot_nft_markets(order_by, int(num_entries))
    else:
        return plot_nft_hist(nft_id, int(duration), int(window_size))
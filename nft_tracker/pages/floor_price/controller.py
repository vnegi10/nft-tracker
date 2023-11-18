from pages.floor_price.view import app
from dash.dependencies import Input, Output
from pages.floor_price.model import plot_nft_hist, plot_nft_markets

@app.callback(
              Output(component_id = 'line_plot', component_property = 'figure'),
              Output(component_id = 'bar_plot', component_property = 'figure'),
              Input(component_id = 'NFT_ID', component_property= 'value'),
              Input(component_id = 'DURATION', component_property= 'value'),
              Input(component_id = 'ORDER_BY', component_property= 'value'),
              Input(component_id = 'NUM_ENTRIES', component_property= 'value'),
              )
def graph_update(nft_id, duration, order_by, num_entries):
    return plot_nft_hist(nft_id, int(duration)), \
           plot_nft_markets(order_by, int(num_entries))
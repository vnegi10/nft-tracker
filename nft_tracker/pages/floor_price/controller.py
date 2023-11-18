from pages.floor_price.view import app
from dash.dependencies import Input, Output
from pages.floor_price.model import plot_nft_hist

@app.callback(
              Output(component_id = 'line_plot', component_property = 'figure'),
              Input(component_id = 'NFT_ID', component_property= 'value'),
              Input(component_id = 'DURATION', component_property= 'value')
              )
def graph_update(nft_id, duration):
    return plot_nft_hist(nft_id, int(duration))
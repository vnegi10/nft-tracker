import dash
from dash import html
from components.dropdown import nft_dropdown
from components.radioitems import duration_radiobutton
from dash import dcc

APP_TITLE = "NFT Floor Price Tracker"
app = dash.Dash()

layout = html.Div(id = 'parent', 
                  children = [
                  html.H1(id = 'H1', children = 'NFT Floor Price Tracker', 
                  style = {'textAlign':'center', 'marginTop':40, 'marginBottom':40}),
                  
                  nft_dropdown(),
                  duration_radiobutton(),
                  
                  dcc.Graph(id = 'line_plot')
])
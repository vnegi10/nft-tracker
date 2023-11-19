import dash
from dash import html
from components.dropdown import *
from components.radioitems import *
from dash import dcc

APP_TITLE = "NFT Floor Price Tracker"
app = dash.Dash()

layout = html.Div(id = 'parent', 
                  children = [
                  html.H1(id = 'H1', children = 'NFT Floor Price Tracker', 
                  style = {'textAlign':'center', 'marginTop':40, 'marginBottom':40}),

                  # Select mode
                  mode_dropdown(),
                  html.Br(), # adds space between the rows

                  # Options for NFT markets
                  orderby_dropdown(),
                  html.Br(),
                  entries_radiobutton(),
                  
                  # Options for NFT historical data
                  nft_dropdown(),
                  html.Br(),
                  duration_radiobutton(),

                  # Add plot
                  dcc.Graph(id = 'plot')
])
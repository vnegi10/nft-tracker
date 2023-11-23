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
                  style = {'textAlign':'center', 'marginTop': 10, 'marginBottom': 10}),

                  # Select mode
                  html.Div([
                  html.P('Select mode')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),

                  mode_dropdown(),
                  html.Br(), # adds space between the rows

                  # Options for NFT markets
                  html.Div([
                  html.P('Order by')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),
                  orderby_dropdown(),

                  html.Br(),

                  html.Div([
                  html.P('Number of entries')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),
                  entries_radiobutton(),

                  html.Br(),
                  
                  # Options for NFT historical data
                  html.Div([
                  html.P('Select NFT ID')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),
                  nft_dropdown(),

                  html.Br(),

                  html.Div([
                  html.P('Historical data [days]')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),
                  duration_radiobutton(),

                  html.Br(),

                  html.Div([
                  html.P('Moving Average Window [days]')
                  ], style = {'marginBottom': 2, 'marginTop': 2}),
                  window_radiobutton(),

                  # Add plot
                  dcc.Graph(id = 'plot')
])
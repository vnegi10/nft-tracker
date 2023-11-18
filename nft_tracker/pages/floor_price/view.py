import dash
from dash import html
from components.dropdown import nft_dropdown, orderby_dropdown
from components.radioitems import duration_radiobutton, entries_radiobutton
from dash import dcc

APP_TITLE = "NFT Floor Price Tracker"
app = dash.Dash()

layout = html.Div(id = 'parent', 
                  children = [
                  html.H1(id = 'H1', children = 'NFT Floor Price Tracker', 
                  style = {'textAlign':'center', 'marginTop':40, 'marginBottom':40}),

                  # NFT markets
                  orderby_dropdown(),
                  html.Br(), # adds space between the rows
                  entries_radiobutton(),
                  dcc.Graph(id = 'bar_plot'),

                  # NFT historical data
                  nft_dropdown(),
                  html.Br(), # adds space between the rows
                  duration_radiobutton(),
                  dcc.Graph(id = 'line_plot')
])
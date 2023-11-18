from dash import dcc

def nft_dropdown():
    dropdown = dcc.Dropdown( id = 'NFT ID',
    options = [
    {'label': 'bitcoin-frogs', 'value':'bitcoin-frogs' },
    {'label': 'mutant-ape-yacht-club', 'value':'mutant-ape-yacht-club'},
    {'label': 'mad-lads', 'value':'mad-lads'},
    ],
    value = 'pudgy-penguins')
    
    return dropdown
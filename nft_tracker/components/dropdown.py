from dash import dcc

def nft_dropdown():
    dropdown = dcc.Dropdown(id = 'NFT_ID',
    options = [
    {'label': 'bitcoin-frogs', 'value':'bitcoin-frogs' },
    {'label': 'mutant-ape-yacht-club', 'value':'mutant-ape-yacht-club'},
    {'label': 'mad-lads', 'value':'mad-lads'},
    {'label': 'cryptopunks', 'value': 'cryptopunks'},
    {'label': 'the-crop-collective', 'value': 'the-crop-collective'},
    {'label': 'galxe-oat-v2', 'value': 'galxe-oat-v2'},
    {'label': 'pudgy-penguins', 'value': 'pudgy-penguins'},
    {'label': 'blendkemon', 'value': 'blendkemon'},
    {'label': 'autoglyphs', 'value': 'autoglyphs'},
    {'label': 'azuki', 'value': 'azuki'}
    ],
    value = 'pudgy-penguins')
    
    return dropdown

def orderby_dropdown():
    dropdown = dcc.Dropdown(id = 'ORDER_BY',
    options = [
    {'label': 'h24_volume_native_asc', 'value':'h24_volume_native_asc' },
    {'label': 'h24_volume_native_desc', 'value':'h24_volume_native_desc'},
    {'label': 'h24_volume_usd_asc', 'value':'h24_volume_usd_asc'},
    {'label': 'h24_volume_usd_desc', 'value':'h24_volume_usd_desc'},
    {'label': 'market_cap_usd_asc', 'value':'market_cap_usd_asc'},
    {'label': 'market_cap_usd_desc', 'value':'market_cap_usd_desc'}
    ],
    value = 'h24_volume_native_desc')
    
    return dropdown

def mode_dropdown():
    dropdown = dcc.Dropdown(id = 'MODE',
    options = [
    {'label': 'Market data', 'value':'market_data' },
    {'label': 'Historical floor price', 'value':'hist_floor_price'},
    {'label': 'Alert email', 'value':'alert_email'},
    ],
    value = 'market_data')
    
    return dropdown
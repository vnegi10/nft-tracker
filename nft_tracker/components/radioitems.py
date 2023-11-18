from dash import dcc

def duration_radiobutton():
    radio = dcc.RadioItems(id = 'DURATION',
    options = ['7', '14', '30', '60', '90', '180', '270', '365'],
    value = '30',
    inline = True,
    )
    
    return radio
from dash import dcc

def duration_radiobutton():
    radio = dcc.RadioItems(id = 'DURATION',
    options = ['7', '14', '30', '60', '90', '180', '270', '365'],
    value = '30',
    inline = True,
    )
    
    return radio

def window_radiobutton():
    radio = dcc.RadioItems(id = 'WINDOW_SIZE',
    options = ['1', '5', '10', '30', '60'],
    value = '7',
    inline = True,
    )
    
    return radio

def entries_radiobutton():
    radio = dcc.RadioItems(id = 'NUM_ENTRIES',
    options = ['10', '20', '50', '75', '100'],
    value = '10',
    inline = True,
    )
    
    return radio
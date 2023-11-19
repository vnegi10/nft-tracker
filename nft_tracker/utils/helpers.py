def set_colors(price_change):
    colors = ['red'] * len(price_change)

    for (index, change) in enumerate(price_change):
        if change > 0:
            colors[index] = 'green'

    return colors
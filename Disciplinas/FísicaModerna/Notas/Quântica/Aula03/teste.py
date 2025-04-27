from sympy import symbols, Eq, plot_implicit

x, y = symbols("x y")
plot_implicit(Eq(x ** 2 + y ** 2, 4), (x, -3, 3), (y, -3, 3), aspect_ratio=(1, 1),
              markers=[{'args': [0, 0], 'color': "blue", 'marker': "o", 'ms': 5},
                       {'args': [[-3, 3], [-3, 3]], 'color': "blue", 'ls': '-', 'lw': 2}],
              annotations=[{'xy': (0, 0), 'text': "  0", 'ha': 'left', 'va': 'top', 'color': 'blue'},
                           {'xy': (2, 2), 'text': "x=y ", 'ha': 'right', 'va': 'bottom', 'color': 'blue'}])

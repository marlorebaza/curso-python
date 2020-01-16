from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('grafica_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar: '))
    
    x_vals = list(range(total_vals))
    y_vals = list(int(input(f'Valor de \'y\' para \'x: {x}\': ')) for x in x_vals)
    
    help(fig)
    
    #fig.line(x_vals, y_vals, line_width = 2)
    
    #show(fig)
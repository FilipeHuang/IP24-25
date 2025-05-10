def approximate_sqrt(x, max_error):
    y = x/2
    y0 = 0
    while abs(y - y0) > max_error:
        y0 = y
        y = 0.5*(y0+(x/y0))
    return y
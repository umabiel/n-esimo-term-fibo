import numpy

def get_term_fibo(nterm):
    F = numpy.matrix([[1, 1], [1, 0]])
    nfibo = (F ** ( nterm - 1 ))[0, 0]
    return int(nfibo)
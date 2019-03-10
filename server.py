from flask import Flask, request, jsonify
import numpy

app = Flask(__name__)

@app.route('/nfibo/<n>', methods=['GET'])
def get_n_fibo(n):
    
    m = int(n)
    F = numpy.matrix([[1, 1], [1, 0]])
    nfibo = (F ** ( m - 1 ))[0, 0]

    res = int(nfibo)

    return jsonify({'mensaje': 'el n-esimo termino de la sucesion de Fibonacci',
                    'resultado': res} )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
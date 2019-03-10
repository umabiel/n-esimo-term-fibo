from flask import Flask, request, jsonify
import numpy
from n_term_fibo import get_term_fibo

app = Flask(__name__)

@app.route('/nfibo/<n>', methods=['GET'])
def get_n_fibo(n):

    if n.isdigit():
        m = int(n)
        res = get_term_fibo(m)
        return jsonify({'mensaje': 'el n-esimo termino de la sucesion de Fibonacci',
                        'resultado': res} ), 200
    else:
        return jsonify({'mensaje': 'El parametro ingresado no es un termino valido'} ), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
# Encontrando e-nesimo termino Fibonacci

se utilizara Python para resolver el problema de encontrar en e-enesimo termino de la sucesion de Fibonacci.

## Instalando dependencias
Para resolver el examen se utilizo Flask para crear el servicio HTTP Rest y Numpy para el calculo del  termino Fibonacci.

Se procedera ejecutando el siguiente comando para la instalacion de las dependencias.

`# pip install -r requirements.txt`

## Iniciando el Servicio HTTP
Al finalizar la instalacion, se puede iniciar el servicio HTTP ejecutando el siguiente comando.

`# python server.py`

## Probando el Servicio y encontrando el n-enesimo Termino
Desde un navegador se dirige a la siguiente ruta.

`http://localhost:8080/nfibo/<TERMINO_A_BUSCAR>`

donde reemplazaremos ***'<TERMINO_A_BUSCAR>'*** por el termino, en este caso utilizaremos el ***'50'***

`http://localhost:8080/nfibo/50`

y obtendremos un resultado en formato JSON con la siguiente estructura.

`
{
    "mensaje":"el n-enesimo termino de la sucesion de Fibonacci",
    "resultado":12586269025
    }
`

#  econ-simulation

Es una librería en étapas tempranas tiene la intención de facilitarle la realización de ejercicios microeconómicos. Disponible tanto en Gooogle Colab como en JupyterNotebook.

Creador: Diego Armando Barquero Sánchez 

Profesor encargado: Alexander Amoretti Alvarado

Si gustas colaborar al código abierto para ciencias económicas no tengas miedo de hacer un push request, explorar el código o contactar para corregir cualquier malfuncionamiento.

## Instalación

Utiliza el comando de python [pip](https://pip.pypa.io/en/stable/) to install git primeramenta, esto te permitirá accesar al repositorio y clonarlo dentro de tu servidor local (computadora).

```bash
pip install git
```

```bash
!git clone https://github.com/barquerosanchezdiegoarmando/econsimulation.git
```

```bash
%cd econsimulation
```
## Uso y explicación de las funciones disponibles
Para ello emplearemos el siguiente ejercicio Microeconómico. 

![Captura](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/536ce73e-c5c9-41a5-9f39-9e0e1498f120)


Para confirmar que la elección del consumidor es 120,20 del bien 1 y el bien 2 respectivamente, utilizaremos la librería econsimulation y la función max_utilidad_cobb_douglas(alpha,beta,m,p1,p2)

# max_utilidad_cobb_douglas()
Primeramente llamamos a la librería y le ponemos el pseudonimo "es" por practicidad.
```python
import econsimulation as es
```
A continuación llamamos a la librería por su pseudonimo "es" y utilizamos la función max_utilidad_cobb_douglas()
Input
```python
es.max_utilidad_cobb_douglas(alpha=2,beta=1,m=180,p1=1,p2=3)
```
Explicación de los parámetros
- alpha: Exponente asociacido al bien 1
- beta: Exponente asociado al bien 2
- m: Presupuestos
- p1: Precio del bien 1
- p2: Precio del bien 2
  
Output
```python
La canasta de bienes que maximiza la utilidad de consumidor es ( 119.99995118859513 , 20.000016270468286 ), con U = 287999.99999985704
```

# curva_indiferencia_tangente()

Primero vamos a crear dos variables que para el ejemplo las nombraremos "x1_vex" y "x2_vec", llamamos a la librería por su pseudonimo "es" y utilizamos la función curva_indiferencia_tangente(). Lo que estamos guardando en las variables son los pares ordenados que forman a la curva de indiferencia que maximiza la utilidad del consumidor y que es tangente a la RMS
Input
```python
x1_vec,x2_vec = es.curva_indiferencia_tangente(y1=120,y2=20,alpha=2,beta=1,N=1000,x2_max=60)
```
Explicación de los parámetros
- y1: Cantidad elejida del bien 1
- y2: Cantidad elejida del bien 2
- alpha: Exponente asociado al bien 1
- beta: Exponente asociado al bien 2
- N: Números necesarios para graficar, recomendado "1000"
- x2_max: Máxima cantidad que el consumidor/productor, se obtiene de dividir m/p2

Si gustas ver lo que se guarda en las variables creadas, puedes colocarlas en un dataframe y ver la tabla
Input
```python
import matplotlib.pyplot as pltr
import pandas as pd

df= pd.DataFrame([x1_vec, x2_vec])
print(df)
```

Output 
![Captura](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/5f12cccf-8dca-4449-9a23-54262be6dd1d)

Genial! Ahora vamos a graficarlo adecuadamente como en los libros de Microeconomía(Varian, Pearson etc...) para ello utilizaremos la siguiente función.

# graficar_indiferencia()
Es una función que emplea los datos del ejercicio y las variables x1_vec y x2_vec.

Input
```python
es.graficar_indiferencia(x_1=120,x_2=20,m=180,p1=1,p2=3,x1_vec=x1_vec,x2_vec=x2_vec)
```
Explicación de los parámetros
- x_1: Cantidad que maximiza la utilidad del bien 1
- x_2: Cantidad que maximiza la utilidad del bien 2
- m: Presupuesto
- p1: Precio del bien 1
- p2: Precio del bien 2
- x1_vec: Vector del bien 1
- x2_vec: Vector del bien 2

Output

![descarga](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/501b8620-cec7-467d-877e-4e55a88350ab)

Ahora si quisieramos ver el epsilon dado un cambio en alguna de las condiciones iniciales, entiéndase presupuesto, precios, preferencias. 

![descarga](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/5fef75cc-20da-4a37-99de-1a90a0a9cea5)

Primeramente debemos realizar la maximizamización de la utilidad dado el cambio en el precio del bien 1. 

Input
```python
es.max_utilidad_cobb_douglas(alpha=2,beta=1,m=180,p1=2,p2=3)
```
Output
```python
La canasta de bienes que maximiza la utilidad de consumidor es ( 59.99999778305689 , 20.00000147796207 ), con U = 71999.9999999997
```

Una vez obtenido el resultado del par ordenado que maximiza la utilidad debemos obtener los vectores de la curva de indiferencia tangente a la RMS. Para ello emplearemos la función de curva_indiferencia_tangente() para encontrar a la curva de indiferencia prima. 

Input
```python
x1_vec_prima,x2_vec_prima = es.curva_indiferencia_tangente(y1=60,y2=20,alpha=2,beta=1,N=1000,x2_max=60)
```

Ya teniendo lo anterior, emplearemos la siguiente función que es una ampliación de graficar_indiferencia()

# graficar_2_indiferencias()

Input
```python
es.graficar_2_indiferencias(x_1=120,x_2=20,x_1_prima=60,x_2_prima=20,m=180,m_prima=180,p1=1,p2=3,p1_prima=2,p2_prima=3,x1_vec=x1_vec,x2_vec=x2_vec,x1_vec_prima=x1_vec_prima,x2_vec_prima=x2_vec_prima)
```

Importante aclaración, en caso de que alguna cosa no cambie entonces el dato original debe mantenerse para que el grafico se realice de forma adecuada. 

Explicación de los parámetros
- x_1: Cantidad que maximiza la utilidad del bien 1 originalmente 
- x_2: Cantidad que maximiza la utilidad del bien 2 originalmente
- x_1_prima: Cantidad que maximiza la utilidad del bien 1 post cambio 
- x_2_prima: Cantidad que maximiza la utilidad del bien 2  post cambio 
- m: Presupuesto original
- m_prima: Presupuesto post cambio
- p1: Precio del bien 1
- p2: Precio del bien 2
- p1_prima: Precio del bien 1 post cambio
- p2_prima: Precio del bien 2 post cambio
- x1_vec: Vector del bien 1 original
- x2_vec: Vector del bien 2 original
- x1_vec_prima: Vector del bien 1 post cambio
- x2_vec_prima: Vector del bien 2 post cambio
  
Output

![Captura](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/63712aed-eb87-4357-a7a8-d9f9c60a996b)


## Bibliografía:
Universidad de Coppenaghen material NumeEcon: https://numeconcopenhagen.netlify.app/lectures/
Cristian Camilo Moreno - Ejercicio de teoría del consumidor: https://ccamilocristian.github.io/posts/optimizacion_teoria_consumidor/

## License

[MIT](https://choosealicense.com/licenses/mit/)

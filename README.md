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
%cd econsiulation
```
## Uso y explicación de las funciones disponibles
Para ello emplearemos el siguiente ejercicio Microeconómico. 

![imagen_ecuacion](https://github.com/barquerosanchezdiegoarmando/econsimulation/assets/126104692/842d3304-85fe-4692-9f01-b5c65f39084b)

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


## Bibliografía:
Universidad de Coppenaghen material NumeEcon: https://numeconcopenhagen.netlify.app/lectures/
Cristian Camilo Moreno - Ejercicio de teoría del consumidor: https://ccamilocristian.github.io/posts/optimizacion_teoria_consumidor/

## License

[MIT](https://choosealicense.com/licenses/mit/)

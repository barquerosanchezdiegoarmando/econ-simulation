import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy import optimize
import matplotlib.pyplot as plt

def max_utilidad_cobb_douglas(alpha,beta,m,p1,p2,do_print=True):
    def objetivo_cobb_douglas(X):
        x,y=X
        return -(x**(alpha)*y**(beta))
    def restriccion_presupuestaria(x):
        p=[p1,p2]
        return -m+p[0]*x[0]+p[1]*x[1]
    b=(0,None)
    bnds=(b,b)
    restriccion=[{'type':'eq', 'fun':restriccion_presupuestaria}]
    sol=minimize(objetivo_cobb_douglas, (0,0), method="SLSQP", constraints=restriccion, bounds=bnds)
    optimo=sol.x
    utilidad = optimo[0]**(alpha)*optimo[1]**(beta)
    
    return print('La canasta de bienes que maximiza la utilidad de consumidor es (', optimo[0],',', optimo[1],'), con U =', utilidad)
  

def curva_indiferencia_tangente(y1,y2,alpha,beta,N,x2_max):
    def u_func(x1,x2,alpha, beta):
          return x1**alpha * x2**beta

    def objective(x1,x2,alpha,u):
          return u_func(x1,x2,alpha,beta) - u
    # = 0 then on indifference curve with utility = u
    # a. utility in (y1,y2)
    u_y = u_func(y1,y2,alpha,beta)

    # b. allocate numpy arrays
    x1_vec = np.empty(N)
    x2_vec = np.linspace(1e-8,x2_max,N)

    # c. loop through x2
    for i,x2 in enumerate(x2_vec):

        x1_guess = 0 # initial guess
        sol = optimize.root(objective, x1_guess, args=(x2,alpha,u_y))
        # optimize.root -> solve objective = 0 starting from x1 = x1_guess

        x1_vec[i] = sol.x[0]

    return x1_vec,x2_vec


def graficar_indiferencia(x_1,x_2,m,p1,p2,x1_vec,x2_vec):
  x=np.arange(0.0, 250, 10)
  y=m/p2-(p1*x/p2)
  fig = plt.figure(figsize=(4,4))
  ax = fig.add_subplot(1,1,1)
  ax.plot(x1_vec,x2_vec, color = 'red')
  plt.plot(x, y)
  plt.text(x_1, x_2, f'({x_1}, {x_2})', ha='right', va='bottom', color='green', fontsize=10)
  plt.scatter(x_1, x_2, color='green', marker='o', label='Cesta de consumo elegida‹')
  plt.fill_between(x, y,0, color="lightblue", alpha=0.5)
  ax.set_xlabel('$x_1$')
  ax.set_ylabel('$x_2$')
  ax.set_xlim([0,m/p1])
  ax.set_ylim([0,m/p2])
  ax.grid(True)
  
  

def graficar_2_indiferencias(x_1,x_2,x_1_prima,x_2_prima,m,m_prima,p1,p2,p1_prima,p2_prima,x1_vec,x2_vec,x1_vec_prima,x2_vec_prima):
    x=np.arange(0.0, 250, 10)
    y_1=m/p2-(p1*x/p2)
    y_2=m_prima/p2_prima-(p1_prima*x/p2_prima)
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(x1_vec,x2_vec, color = 'red')
    ax.plot(x1_vec_prima,x2_vec_prima, color = 'red')
    plt.plot(x, y_1)
    plt.plot(x, y_2)
    plt.text(x_1, x_2, f'({x_1}, {x_2})', ha='right', va='bottom', color='green', fontsize=10)
    plt.scatter(x_1, x_2, color='green', marker='o', label='Cesta de consumo elegida‹')
    plt.text(x_1_prima, x_2_prima, f'({x_1_prima}, {x_2_prima})', ha='right', va='bottom', color='green', fontsize=10)
    plt.scatter(x_1_prima, x_2_prima, color='green', marker='o', label='Cesta de consumo elegida‹')
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    if m > m_prima:
      limite = m  # Si es verdadero, asignamos el valor de m a la variable límite
    else:
      limite = m_prima  # Si es falso, asignamos el valor de m_prima a la variable límite
    if  p1 < p1_prima:
      p1_definitivo = p1  # Si es verdadero, asignamos el valor de m a la variable límite
    else:
      p1_definitivo = p1_prima
    if  p2 < p2_prima:
      p2_definitivo = p2  # Si es verdadero, asignamos el valor de m a la variable límite
    else:
      p2_definitivo = p2_prima
    ax.set_xlim([0,limite/p1_definitivo])
    ax.set_ylim([0,limite/p2_definitivo])
    ax.grid(True)
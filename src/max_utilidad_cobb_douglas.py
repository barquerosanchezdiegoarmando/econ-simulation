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

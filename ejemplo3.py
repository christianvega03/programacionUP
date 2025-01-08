import numpy as np



def ganancias(x, y):
  # Suponiendo precios de venta y costos de producción

  return precio_A *x + precio_B *y - costo_A * x**2 - costo_B*y**2

def gradiente_ganancias(x, y):
  # Calcular las derivadas parciales de la función de ganancias
  dg_dx = precio_A - 2*costo_A*x
  dg_dy = precio_B - 2*costo_B*y
  return np.array([dg_dx, dg_dy])

def gradiente_ascendente(x0, y0, alpha, tol, max_iter):
  x = x0
  y = y0
  for i in range(max_iter):
    grad = gradiente_ganancias(x, y)
    x = x + alpha * grad[0]
    y = y + alpha * grad[1]
    if np.linalg.norm(grad) < tol:
      break
  return x, y

# Parámetros
precio_A = 1000
precio_B = 1500
costo_A = 5
costo_B = 8
x0 = 100
y0 = 200
alpha = 0.01
tol = 1e-6
max_iter = 1000

# Ejecutar el algoritmo
resultado = gradiente_ascendente(x0, y0, alpha, tol, max_iter)

print("Cantidad óptima de producto A:", resultado[0])
print("Cantidad óptima de producto B:", resultado[1])
print("Ganancias máximas:", ganancias(*resultado))
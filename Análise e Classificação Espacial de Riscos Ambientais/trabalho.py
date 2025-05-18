import numpy as np
import matplotlib.pyplot as plt

#Criar um plano 2D com pontos representando diferentes posições em um mapa.
x = np.linspace(-10, 40)
y = np.linspace(40, -10)
xz, yz = np.meshgrid(x, y)

#Calcular a “distância ao centro” de cada ponto.
z = np.sqrt(xz ** 2 + yz ** 2)

#Classificar essas distâncias em pelo menos três categorias distintas.
distancia = np.where(z > 1.2 * np.mean(z),
                      "zona crítica/perigosa",
                        np.where(z < 0.8 * np.mean(z),
                        "zona segura",
                         "zona de atenção"))

#Gerar uma visualização gráfica (como um mapa de calor ou gráfico de contorno) para mostrar os dados classificados.
plt.title("Classificação Espacial de Riscos Ambientais")
plt.imshow(z)
plt.colorbar()
plt.show()

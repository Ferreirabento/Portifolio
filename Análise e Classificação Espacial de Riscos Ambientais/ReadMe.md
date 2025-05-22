# 📍 Classificação Espacial de Riscos Ambientais

Este projeto utiliza **Programação Orientada a Arrays com NumPy** para simular e visualizar zonas de risco com base na distância de pontos em um mapa 2D. A ideia central é representar diferentes áreas de um território com base em sua distância ao centro, classificando-as em zonas de segurança, atenção e perigo.

---

## 📌 Objetivo

Criar uma simulação espacial onde cada ponto do mapa seja classificado de acordo com sua distância ao centro, permitindo uma análise visual de zonas críticas, de atenção e seguras — útil para estudos ambientais, simulações de evacuação, análise de impacto, entre outros.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 🧠 Conceitos Aplicados

- Geração de arrays e malhas 2D com `np.linspace()` e `np.meshgrid()`
- Cálculo vetorizado de distâncias com `np.sqrt()`
- Classificação de dados com expressões condicionais usando `np.where()`
- Visualização de dados com `matplotlib.pyplot.imshow()` e `plt.colorbar()`
- Programação orientada a arrays com foco em lógica e performance

---

## 📊 Resultado

O programa gera um mapa visual com zonas classificadas automaticamente:

- 🔴 **Zona Crítica** – regiões com distância muito maior que a média.
- 🟡 **Zona de Atenção** – regiões dentro da faixa de média distância.
- 🟢 **Zona Segura** – regiões com distância abaixo da média.

<p align="center">
  <img src="exemplo_mapa.png" alt="Exemplo do mapa gerado" width="600"/>
</p>

---

## 🗂️ Estrutura do Projeto


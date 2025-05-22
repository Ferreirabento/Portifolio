# 📊 Análise de Vendas Regionais (com NumPy, Pandas e Matplotlib)

Este projeto é um estudo de Análise de Dados com foco em vendas regionais trimestrais, utilizando bibliotecas essenciais do ecossistema Python: **NumPy**, **Pandas** e **Matplotlib**.

---

## 🧠 Objetivo

Transformar uma planilha de vendas em uma análise estatística clara, classificando desempenhos por região e trimestre, extraindo informações úteis como:

* Soma total de vendas por trimestre
* Classificação de desempenho (Alta performance, Na média, Necessita atenção)
* Identificação das regiões com melhores e piores resultados
* Trimestre mais lucrativo

---

## 📁 Dados Utilizados

O arquivo **`vendas_regionais.xlsx`** contém as seguintes colunas:

* `região`: nome da região
* `trimestre`: trimestre de referência (ex: Q1, Q2, etc.)
* `vendas`: valor total de vendas naquele período e região

---

## ⚙️ Tecnologias Aplicadas

* `Pandas` para leitura, transformação e organização dos dados
* `NumPy` para operações matemáticas e estatísticas com arrays
* `Matplotlib` para visualização dos dados (gráfico de calor)

---

## 🔍 Etapas do Projeto

1. **Leitura da planilha Excel**
2. **Reformulação em formato de matriz (região x trimestre)**
3. **Conversão para matriz NumPy para análises rápidas**
4. **Classificação de desempenho com base nas médias**
5. **Cálculo de estatísticas: maiores e menores valores, totais, etc.**
6. **Visualização gráfica com Matplotlib**

   > ⚠️ **Observação:** a parte gráfica do projeto (mapa de calor com `imshow`) foi adicionada com apoio externo e **não foi desenvolvida por mim**.

---

## 📈 Resultados

O código identifica:

* Quais trimestres tiveram melhor desempenho
* Quais regiões precisam de atenção
* A performance geral por trimestre
* Visualização clara com cores indicando intensidade de vendas

---

## 💼 Finalidade

Este projeto foi desenvolvido com fins **educacionais e de portfólio**, consolidando meu aprendizado em:

* Manipulação de dados com Pandas
* Análise numérica com NumPy
* Aplicação de lógica condicional com `np.where`
* Leitura e interpretação de dados estruturados

---

## 🧾 Como Executar

1. Instale as bibliotecas necessárias:

```bash
pip install numpy pandas matplotlib openpyxl
```

2. Coloque o arquivo `vendas_regionais.xlsx` no mesmo diretório do script.

3. Execute o script Python normalmente.

---

## ✍️ Autor

**João Bento Ramos Ferreira**
Em aprendizado constante em Análise de Dados com Python.
Este projeto é parte do meu portfólio pessoal.

---

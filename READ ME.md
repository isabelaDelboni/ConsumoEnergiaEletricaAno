# **Consumo de Energia Elétrica por Estado - Aplicativo Dash**

Um aplicativo web interativo para visualizar e analisar o consumo de energia elétrica por estado no Brasil. Desenvolvido com **Dash**, o projeto permite exibir gráficos baseados em dados históricos e realizar previsões utilizando um modelo de regressão linear (**Lasso**).

---

## **Recursos do Projeto**

- Visualização interativa do consumo de energia elétrica por ano, agrupada por estado.
- Interface simples com seleção de estado via dropdown.
- Previsões de consumo para os próximos 5 anos, utilizando **regressão Lasso**.
- Gráficos interativos e responsivos gerados com **Plotly**.
- Estilização personalizada com **CSS**.

---

## **Instalação**

### **Pré-requisitos**

Certifique-se de ter o **Python 3.7+** instalado em sua máquina.

### **Dependências**

Instale as bibliotecas necessárias usando o comando para instalação de dependências.

### **Clonando o Repositório**

Clone o projeto do GitHub para sua máquina local e navegue até a pasta do repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### **Como Executar**

Certifique-se de que o arquivo com os dados de consumo de energia elétrica esteja na mesma pasta que o script principal do aplicativo. Em seguida, execute o script principal com o seguinte comando:
```
python app.py
```
Em seguida abra o navegador no endereço fornecido para acessar o aplicativo.

---

## **Estrutura do Projeto**

- **app.py**: Arquivo principal contendo o código do aplicativo.
- **br_mme_consumo_energia_eletrica_uf (1).csv**: Dados históricos de consumo de energia elétrica no Brasil.
- **assets/style.css**: Arquivo CSS para personalizar o visual do aplicativo.

---

## **Dados Utilizados**

Os dados utilizados no aplicativo foram extraídos do arquivo com informações sobre:

- **Estado (sigla_uf)**: Sigla do estado brasileiro.
- **Ano (ano)**: Ano do registro de consumo.
- **Consumo (consumo)**: Consumo total de energia elétrica em MWh.
- **Número de Consumidores (numero_consumidores)**: Número de consumidores registrados.

---

## **Funcionalidades Principais**

- **Visualização de Dados**: Mostra o consumo total por estado, com opção de selecionar o estado desejado.
- **Previsões**: Permite alternar para exibir previsões de consumo para os próximos 5 anos.
- **Gráficos Interativos**: Gráficos dinâmicos gerados com **Plotly**, permitindo uma melhor análise visual.

---

## **Tecnologias Utilizadas**

- **Dash**: Framework para desenvolvimento de aplicativos web interativos.
- **Plotly**: Biblioteca para gráficos interativos.
- **Pandas**: Manipulação de dados tabulares.
- **Scikit-Learn**: Ferramentas de aprendizado de máquina.
- **NumPy**: Operações numéricas.

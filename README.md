# 🚚 Sistema Gerenciador de Rotas entre Cidades

Projeto feito para a disciplina de Matemática aplicada a computação. É sistema simples para gerenciar rotas e cidades utilizando grafos, desenvolvido em Python com as bibliotecas [NetworkX](https://networkx.org/) e [Matplotlib](https://matplotlib.org/). O objetivo principal é simular uma rede de entregas entre cidades, permitindo visualizar o grafo, buscar a melhor rota entre cidades, adicionar/remover cidades e estradas, tudo por meio de um menu interativo.

---

## ✨ Funcionalidades

- 🗺️ **Visualização do grafo:** Exibe um gráfico das cidades conectadas pelas estradas, com as distâncias entre elas.
- 🚦 **Busca pela melhor rota:** Utiliza o algoritmo de Dijkstra para encontrar a rota mais curta entre duas cidades.
- 🏙️ **Adição/remoção de cidades:** Permite ao usuário inserir novas cidades ou removê-las do sistema.
- 🛣️ **Adição de estradas:** Permite criar novas conexões (arestas) entre cidades, definindo a distância (peso).
- 💻 **Interface interativa:** Sistema simples de menu pelo terminal.

---

## ⚙️ Como funciona

O sistema representa as cidades como **nós** de um grafo, e as estradas como **arestas** ponderadas (com peso igual à distância).  
As principais operações são realizadas por meio de funções que utilizam métodos clássicos de teoria dos grafos, como visualização, busca de caminhos mínimos e manipulação dinâmica do grafo.

---

## 📋 Exemplo de uso

1. 🗺️ **Visualizar o grafo:**  
   Veja todas as cidades e estradas da rede.
   <img width="780" height="661" alt="image" src="https://github.com/user-attachments/assets/803e4b35-6213-4509-9b48-643b2eec0bb3" />


3. 🚦 **Encontrar a melhor rota:**  
   Informe a cidade de origem e destino, e o sistema retorna o menor caminho e sua distância.
   <img width="856" height="338" alt="image" src="https://github.com/user-attachments/assets/63246839-20eb-41d4-8234-3d76126297f7" />





import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo(cidades, estradas):
    G = nx.Graph()
    G.add_nodes_from(cidades)
    G.add_weighted_edges_from(estradas)
    return G

def desenhar_grafo(G, titulo="Rede de Entregas"):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(titulo)
    plt.show()

def encontrar_melhor_rota(G, origem, destino):
    try:
        caminho = nx.dijkstra_path(G, origem, destino)
        distancia = nx.dijkstra_path_length(G, origem, destino)
        return caminho, distancia
    except nx.NetworkXNoPath:
        print(f"⚠️ Não existe caminho entre {origem} e {destino}.")
        return None, None

def entrada_usuario(G):
    print("\nCidades disponíveis:", ', '.join(G.nodes))
    origem = input("Digite a cidade de origem: ").strip()
    destino = input("Digite a cidade de destino: ").strip()

    if origem not in G.nodes:
        print(f"❌ Cidade de origem '{origem}' não encontrada.")
        return None, None
    if destino not in G.nodes:
        print(f"❌ Cidade de destino '{destino}' não encontrada.")
        return None, None
    return origem, destino

def adicionar_cidade(G):
    nova = input("Nome da nova cidade: ").strip()
    if nova in G.nodes:
        print("⚠️ Cidade já existe.")
    else:
        G.add_node(nova)
        print(f"✅ Cidade '{nova}' adicionada.")

def adicionar_estrada(G):
    origem = input("Cidade de origem da estrada: ").strip()
    destino = input("Cidade de destino da estrada: ").strip()
    if origem not in G.nodes or destino not in G.nodes:
        print("❌ Ambas as cidades devem existir no grafo.")
        return
    try:
        peso = float(input("Distância entre elas (km): "))
        G.add_edge(origem, destino, weight=peso)
        print(f"✅ Estrada adicionada de {origem} a {destino} com {peso} km.")
    except ValueError:
        print("❌ Distância inválida.")

def remover_cidade(G):
    print("\nCidades disponíveis:", ', '.join(G.nodes))
    cidade = input("Nome da cidade a remover: ").strip()
    
    if cidade not in G.nodes:
        print("❌ Cidade não encontrada no sistema.")
        return
        
    G.remove_node(cidade)
    print(f"✅ Cidade '{cidade}' removida com sucesso!")

if __name__ == "__main__":
    cidades = ['Monteiro', 'Ouro Velho', 'Zabele', 'Sume', 'Sertania']
    estradas = [
        ('Monteiro', 'Ouro Velho', 10),
        ('Monteiro', 'Zabele', 15),
        ('Ouro Velho', 'Sume', 12),
        ('Zabele', 'Sume', 10),
        ('Sume', 'Sertania', 5),
        ('Zabele', 'Sertania', 20)
    ]

    G = criar_grafo(cidades, estradas)

    while True:
        print("\n=== MENU ===")
        print("1 - Visualizar grafo")
        print("2 - Encontrar melhor rota")
        print("3 - Adicionar nova cidade")
        print("4 - Remover cidade")
        print("5 - Adicionar nova estrada")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            desenhar_grafo(G)
        elif escolha == '2':
            origem, destino = entrada_usuario(G)
            if origem and destino:
                caminho, distancia = encontrar_melhor_rota(G, origem, destino)
                if caminho:
                    print(f"\n✅ Melhor rota de {origem} até {destino}: {' -> '.join(caminho)}")
                    print(f"📏 Distância total: {distancia} km")
        elif escolha == '3':
            adicionar_cidade(G)
        elif escolha == '4':
            remover_cidade(G)
        elif escolha == '5':
            adicionar_estrada(G)
        elif escolha == '0':
            print("Encerrando o programa. 👋")
            break
        else:
            print("❌ Opção inválida.")
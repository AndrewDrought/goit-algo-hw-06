import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'),
         ('D', 'H'), ('D', 'I'), ('E', 'J'), ('E', 'K'), ('F', 'L'), ('F', 'M')]

G.add_edges_from(edges)

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Аналіз графа
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print(f"Ступені вершин: {G.degree()}")

# DFS
print("DFS:")
print(list(nx.dfs_preorder_nodes(G, 'A')))

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
print("BFS:")
print(list(bfs_tree))

# Завдання 3

# Додавання ваг до ребер
G['A']['B']['weight'] = 1.0
G['B']['C']['weight'] = 2.0
G['C']['A']['weight'] = 3.0

# Застосування алгоритму Дейкстри
print("Найкоротші шляхи:")
for node in G.nodes:
    print(f"Від 'A' до '{node}': {nx.dijkstra_path(G, 'A', node)}")
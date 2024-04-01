import networkx as nx
import matplotlib.pyplot as plt
import os

# Функция для чтения ребер из файла
def read_edges_from_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            edge = line.strip().split()
            # Преобразуем строковые значения в целые числа
            edge_tuple = tuple(map(int, edge))
            edges.append(edge_tuple)
    return edges

# Вывод графа
def plot_graph(G, title):
    options = dict(
        font_size=12,
        node_size=500,
        node_color="white",
        edgecolors="black",
    )
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, **options)
    plt.title(title)
    plt.show()

# Функция восстановления цикла
def get_cycle(from_list, lastVertex):
    cycle = []
    v = from_list[lastVertex]
    while v != lastVertex:
        cycle.append(v)
        v = from_list[v]
    cycle.append(lastVertex)
    cycle.reverse()
    return cycle

# DFS функция
def dfs(G, v, visited, from_list, cycle):
    visited[v] = 1
    for to in G[v]:
        if to == from_list[v]:
            continue
        elif visited[to] == 0:
            from_list[to] = v
            dfs(G, to, visited, from_list, cycle)
            if cycle:
                return
        elif visited[to] == 1:
            from_list[to] = v
            cycle.extend(get_cycle(from_list, to))
            return

def has_cycles(cycle):
    if cycle:
        print("YES")
        print("Vertices of an undirected cycle:\n ")
        for v in cycle:
            print(v)
    else:
        print("NO")

# Путь к папке с файлами
folder_path = 'files'

# Перебираем все файлы в папке
for filename in os.listdir(folder_path):
    if filename.endswith('.edgelist'):
        file_path = os.path.join(folder_path, filename)
        edges = read_edges_from_file(file_path)
        
        # Создаем новый граф для каждого файла
        G = nx.Graph()
        G.add_edges_from(edges)
        
        # Отрисовываем граф
        plot_graph(G, f'Graph: {filename}')
        
        # Проверяем наличие циклов
        vertexCount = len(G)
        visited = [0] * vertexCount
        fromVertex = [-1] * vertexCount
        cycle = []

        for v in range(vertexCount):
            if not visited[v] and not cycle:
                dfs(G, v, visited, fromVertex, cycle)

        # Выводим информацию о наличии циклов
        print(f"The presence of cycles in an undirected graph {filename}: ")
        has_cycles(cycle)
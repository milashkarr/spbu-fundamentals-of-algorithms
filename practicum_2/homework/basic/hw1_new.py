import networkx as nx
import matplotlib.pyplot as plt
from src.plotting import plot_graph

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

# Список файлов для обработки
TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_w_cycles.edgelist",
]

# Перебираем все файлы в списке
for filename in TEST_GRAPH_FILES:
    file_path = f"C:/Users/Lada/python/practicum_2/homework/basic/{filename}"
    
    # Создаем новый граф для каждого файла
    G = nx.read_edgelist(file_path, create_using=nx.Graph, nodetype=int)
    
    # Отрисовываем граф
    plot_graph(G, f'Graph: {filename}')
    
    # Проверяем наличие циклов
    vertexCount = max(G.nodes())  # Используем max(G.nodes()) для учета возможных пропусков в номерах вершин
    visited = [0] * (vertexCount + 1)  # Используем vertexCount + 1, чтобы учесть вершины, начинающиеся с номера 1
    fromVertex = [-1] * (vertexCount + 1)
    cycle = []

    for v in G.nodes():
        v = int(v)  # Преобразуем номер вершины в целое число
        if not visited[v] and not cycle:
            dfs(G, v, visited, fromVertex, cycle)

    # Выводим информацию о наличии циклов
    print(f"The presence of cycles in an undirected graph {filename}: ")
    has_cycles(cycle)
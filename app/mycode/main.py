from pprint import pprint

from leafy.graph import Graph
from leafy.search import DFS

def run():
    dag = Graph(13, True)
    dag.add_edge(0, 1, 0.5)
    dag.add_edge(0, 2)
    dag.add_edge(0, 3)
    dag.add_edge(0, 5)
    dag.add_edge(0, 6)
    dag.add_edge(2, 3)
    dag.add_edge(3, 4)
    dag.add_edge(3, 5)
    dag.add_edge(4, 9)
    dag.add_edge(6, 4)
    dag.add_edge(6, 9)
    dag.add_edge(7, 6)
    dag.add_edge(8, 7)
    dag.add_edge(9, 10)
    dag.add_edge(9, 11)
    dag.add_edge(9, 12)
    dag.add_edge(11, 12)
    dfs = DFS(dag, 0)
    dfs.run()
    pprint(dfs.diagnostics)


if __name__ == "__main__":
    run()
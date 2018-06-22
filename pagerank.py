# -*- coding:utf-8 -*-
from pygraph.classes.digraph import digraph
class PRIterator:
    def __init__(self, dg):
        self.damping_factor = 0.80  # the damping coefficientα
        self.max_iterations = 5000  # the maximum of iterations
        self.min_delta = 0.0000001  # the parameter ϵ whose aim is to ensure the continue or end
        self.graph = dg

    def page_rank(self):
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
        damping_value = (1.0 - self.damping_factor) / graph_size  # (1−α)/N

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)
                page_rank[node] = rank

            print("Iteration number %s" % (i + 1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                break
        return page_rank

if __name__ == '__main__':
    dg = digraph()
    # input all nodes in data set DS, their style is ["A", "B", "C", "D", "E"]
    dg.add_nodes(DS)
    # input all training facts, their style is ("A", "B")
    for i in len(Fact):
        dg.add_edge(i)
    pr = PRIterator(dg)
    page_ranks = pr.page_rank()
    print("PageRank:\n", page_ranks)
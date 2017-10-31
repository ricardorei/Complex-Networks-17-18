import networkx as nx
import sys
sys.path.append('..')
from build_network import load_network, evaluate_metric

def run():
    betweeness_centrality = nx.betweenness_centrality(load_network(), weight='weight')
    evaluate_metric("Betweeness Centrality", betweeness_centrality)

if __name__ == '__main__':
    run()
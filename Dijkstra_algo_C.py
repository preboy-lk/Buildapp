import igraph

def dijkstra(G,src,des):
    return G.get_shortest_paths(src,des,weights="weight")

def load_graph_gml(filename):
    G = igraph.Graph.Load(filename,"gml")
    return G
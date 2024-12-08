# Search methods

import search

# Rumanía

# Caso 1. Origen: Arad -> Destino: Bucharest
ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("\n------------------ A y B ------------------\n")
search.breadth_first_graph_search(ab)
search.depth_first_graph_search(ab)
search.branch_and_bound_graph_search(ab)
search.branch_and_bound_with_subestimation_graph_search(ab)

print("\n--------------------------------------------------------")

# Caso 2. Origen: Oradea ->  Destino: Eforie
oe = search.GPSProblem('O', 'E'
                       , search.romania)
print("\n------------------ O y E ------------------\n")
search.breadth_first_graph_search(oe)
search.depth_first_graph_search(oe)
search.branch_and_bound_graph_search(oe)
search.branch_and_bound_with_subestimation_graph_search(oe)

print("\n--------------------------------------------------------")

# Caso 3. Origen: Giurgiu ->  Destino: Zerind
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
print("\n------------------ G y Z ------------------\n")
search.breadth_first_graph_search(gz)
search.depth_first_graph_search(gz)
search.branch_and_bound_graph_search(gz)
search.branch_and_bound_with_subestimation_graph_search(gz)

print("\n--------------------------------------------------------")

# Caso 4. Origen: Neamt ->  Destino: Dobreta
nd = search.GPSProblem('N', 'D'
                       , search.romania)
print("\n------------------ N y D ------------------\n")
search.breadth_first_graph_search(nd)
search.depth_first_graph_search(nd)
search.branch_and_bound_graph_search(nd)
search.branch_and_bound_with_subestimation_graph_search(nd)

print("\n--------------------------------------------------------")

# Caso 5. Origen: Mehadia ->  Destino: Fagaras
mf = search.GPSProblem('M', 'F'
                       , search.romania)
print("\n------------------ M y F ------------------\n")
search.breadth_first_graph_search(mf)
search.depth_first_graph_search(mf)
search.branch_and_bound_graph_search(mf)
search.branch_and_bound_with_subestimation_graph_search(mf)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
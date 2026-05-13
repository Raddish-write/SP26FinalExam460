"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    ans = ("Why a single shortest-path run from S is not enough:\n"
           "A single shortest path run is not enough for the torchbearer problem because a shortest path may possibly skip over some relic rooms and a valid route is defined here in part as one that collects every relic.\n"
           "What decision remains after all inter-location costs are known:\n"
           "After the cost to travel between every room has been calculated, the order of the rooms must then be selected.\n"
           "Why this requires a search over orders (one sentence): \n"
           "Because every node must be visited, you cannot greedily select the closest node to the last which means that valid orders must be compared in order to determine the lowest order.\n")
    return ans


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sourceList = [spawn, exit_node]
    for x in relics:
        if x not in sourceList:
            sourceList.append(x)

    return sourceList


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    val = dict()
    for key in graph:
        val[key] = float('inf')
    val[source] = 0

    min_heap = []
    heapq.heappush(min_heap, (0, source))

    while min_heap:
        (dist, node) = heapq.heappop(min_heap)

        if dist > val[node]:
            continue

        for nextNode, edgeWeight in graph[node]:
            temp = val[node] + edgeWeight
            if temp < val[nextNode]:
                val[nextNode] = temp
                heapq.heappush(min_heap, (val[nextNode], nextNode))

    return val


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    distances = dict()
    for key in sources:
        node_dist = run_dijkstra(graph, key)
        distances[key] = node_dist

    return distances


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    ans = ("3a: What the invariant means:\n"
           ">> For nodes not already finalized (in S):\n"
           "_for all finalized nodes, the stored value for that node is the shortest distance from the source_\n"
           ">> For nodes not yet finalized (not in S):\n"
           "_for all nodes not finalized, the stored value for that node is the shortest distance to that node from the source considering only finalized nodes_\n"
           "3b: Why each phase holds:\n"
           ">> Initialization: Why the invariant holds before iteration 1:\n"
           "_only the source node is finalized with a distance of 0._\n"
           "_As no intermediate nodes can be considered, every other node position is infinitely far from the source, and so the invariant holds_\n"
           ">> Maintenance: Why finalizing the min-dist node is always correct\n"
           "_Prior to any step, the stored value is either the shortest distance from the source or the shortest distance considering only finalized nodes_\n"
           "_Because each edge has a non-negative weight and thus can never lower a cumulative distance, once all intermediate nodes are considered_\n"
           "_the lowest cumulative weight chosen is the lowest distance from the source node and thus the invariant holds_\n"
           ">> Termination: What the invariant guarantees when the algorithm ends\n"
           "_Once the minheap is empty (when all edges for every node have been considered) the function ends_\n"
           "_When the function ends, all nodes will have been considered for every node and the shortest has been selected_\n"
           "_Thus the invariant holds_\n"
           "3c: Why this matters for the route planner:\n"
           ">> The route planner relies on Djikstras in order to calculate the distances of valid routes, and so must itself be correct.\n")
    return ans


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    ans = ("4a: Why Greedy Fails:\n"
           ">> Failure mode: proof that greedy fails by counterexample\n"
           "Consider the greedy strategy of choosing the nearest relic/exit node that has not yet been selected each step\n"
           ">> Counter-example setup:\n"
           "Consider the following graph:\n"
           "\t'S': [('B', 1), ('C', 2), ('D', 2)],\n"
           "\t'B': [('D', 1), ('T', 1)],\n"
           "\t'C': [('B', 1), ('T', 10)],\n"
           "\t'D': [('B', 1), ('C', 1)],\n"
           "\t'T': []\n"
           ">> Greedy selected path:\n"
           "\tS -> B -> D -> C -> T, with a distance of 13\n"
           ">> Optimal selected path:\n"
           "\tS -> D -> C -> B -> T, with a distance of 5\n"
           ">> Why greedy loses:\n"
           "Because choosing the locally optimal choice restricts future globally optimal choices, a greedy strategy does not garuntee optimality\n"
           "4b: What the algorithm must explore:\n"
           "The algorithm must explore valid orders and compare their total length, disregarding lengths higher than those already explored\n")
    return ans


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    relics_remaining = set(relics)

    """greedy may not always be optimal, but it will be valid and provides a relatively low upper bound"""
    best = _greedy(spawn, dist_table, relics_remaining, exit_node)
    visited = list()
    _explore(dist_table, spawn, relics_remaining, visited, 0, exit_node, best)

    return best

def _greedy(spawn, dist_table, relics_remaining, exit_node):
    """
    Helper function to find starting "best" distance to prune execesive branches

    Parameters
    -------
    spawn : node
    dist_table : dict[node, dict[node, float]]

    Returns
    -------
    tuple[float, list(node)]

    """

    temp_node = spawn
    set_check = relics_remaining.copy()
    """I hate python so much. Why am I able to modify collections outside of their parent function? Why does .copy() need to exist?"""
    greedy_list = list()
    dist = 0
    while set_check:
        temp_dist = float('inf')
        for key in dist_table[temp_node]:
            if (dist_table[temp_node][key] < temp_dist and key in set_check):
                neighbor = key
                temp_dist = dist_table[temp_node][key]
        set_check.remove(neighbor)
        greedy_list.append(neighbor)
        temp_node = neighbor
        dist += temp_dist

    greedy_list.append(exit_node)
    dist += dist_table[temp_node][exit_node]
    greedy_solution = [dist, greedy_list]

    return greedy_solution

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    if cost_so_far >= best[0]:
        return

    if not relics_remaining:
        cost_so_far += dist_table[current_loc][exit_node]
        relics_visited_order.append(exit_node)
        if cost_so_far <= best[0]:
            best[0] = cost_so_far
            best[1] = relics_visited_order.copy()
        cost_so_far -= dist_table[current_loc][exit_node]
        relics_visited_order.pop()

    for x in dist_table[current_loc]:
        if x in relics_remaining:
            relics_remaining.remove(x)
            relics_visited_order.append(x)
            cost_so_far += dist_table[current_loc][x]
            _explore(dist_table, x, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)
            relics_remaining.add(x)
            relics_visited_order.pop()

    return

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    solution = find_optimal_route(dist_table, spawn, relics, exit_node)
    return solution


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

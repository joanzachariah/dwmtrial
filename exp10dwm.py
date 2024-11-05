def page_rank(links, damping=0.85, max_iter=100, tol=1e-6):
    """
    Compute the PageRank of nodes in a graph.

    Parameters:
    links (dict): A dictionary where each key is a node, and the value is a list of nodes to which it links.
    damping (float): The damping factor, default is 0.85.
    max_iter (int): Maximum number of iterations.
    tol (float): Tolerance for convergence, default is 1e-6.

    Returns:
    dict: A dictionary where keys are nodes and values are the corresponding PageRank values.
    """
    
    nodes = list(links)
    N = len(nodes)
    page_rank = {node: 1.0 / N for node in nodes}

    for iteration in range(max_iter):
        old_page_rank = page_rank.copy()
        for node in nodes:
            rank_sum = sum(old_page_rank[other] / len(links[other]) 
                           for other in nodes if node in links[other] and links[other])
            page_rank[node] = (1 - damping) / N + damping * rank_sum

        if sum(abs(page_rank[node] - old_page_rank[node]) for node in nodes) < tol:
            print(f"Converged in {iteration + 1} iterations.")
            break

    return page_rank

def get_graph_from_user():
    links = {}
    nodes_input = input("Enter all nodes separated by spaces: ").strip().split()
    
    for node in nodes_input:
        links[node] = input(f"Enter the nodes that {node} links to (separated by spaces): ").strip().split()
    
    return links

if __name__ == "__main__":
    links = get_graph_from_user()
    ranks = page_rank(links)
    
    print("\nPageRank values:")
    for node, rank in ranks.items():
        print(f"{node}: {rank:.6f}")
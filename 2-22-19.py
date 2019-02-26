def parse_graph(string, edges):
    adjacency = {}
    sources = set()
    for i in range(len(string)):
        node = (i, string[i])
        adjacency[node] = set()
        sources.add(node)
    
    for u_ind, v_ind in edges:
        source = (u_ind, string[u_ind])
        dest = (v_ind, string[v_ind])
        adjacency[source].add(dest)

        sources.remove(dest)

    return adjacency, sources

def DFS(adjacency):
    seen = set()
    reverse_top = []

    # returns True if cycle is found, False otherwise
    def DFS_visit(start, single_seen):
        for node in adjacency[start]:
            if node in single_seen:
                return True
            
            if node not in seen:
                seen.add(node)
                single_seen.add(node)
                DFS_visit(node, single_seen)
                single_seen.remove(node)
        
        reverse_top.append(start)
        return False

    for node in adjacency:
        if node not in seen:
            seen.add(node)
            if DFS_visit(node, set([node])):
                return None

    return reverse_top[::-1]

def init_source_path_dict(adjacency, sources):
    dic = {}
    for source in sources:
        _, value = source
        inner_dic = {node : {node[1] : 1} for node in adjacency}
        dic[source] = inner_dic
    return dic

def update_path_dict(path_dict, u, v):
    max_new_val = 0
    _, extra_val = v
    for key in path_dict[u]:
        extra = int(extra_val == key)
        new_val = max(path_dict[u][key] + extra, path_dict[v].get(key, 0))
        path_dict[v][key] = new_val
        max_new_val = max(max_new_val, new_val)
    return max_new_val

def highest_path_value(string, edges):
    adjacency, sources = parse_graph(string, edges)
    if len(sources) == 0:
        return None

    top_sort = DFS(adjacency)
    if top_sort == None:
        return None

    output = 0
    source_path_dict = init_source_path_dict(adjacency, sources)
    for source in sources:
        path_dict = source_path_dict[source]
        for u in top_sort:
            for v in adjacency[u]:
                output = max(output, update_path_dict(path_dict, u, v))
    return output

string = "A"
edges = [(0, 0)]
assert highest_path_value(string, edges) == None

string = "ABACA"
edges = [(0, 1), (0, 2), (2, 3), (3, 4)]
assert highest_path_value(string, edges) == 3

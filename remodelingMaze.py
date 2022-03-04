class Node:
    def __init__(self, x_pos, y_pos, impassable=False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.impassable = impassable
        self.adjacent = []
        self.is_goal = False

    def add(self, o):
        self.adjacent.append(o)

    @property
    def impassable_neighbors(self):
        ret = 0
        for node in self.adjacent:
            if node.impassable:
                ret += 1
        return ret


def find_shortest_path(map):
    start_node = map[0][0]
    explored = {start_node}
    current = {start_node}
    next_nodes = set()
    path_length = 1
    while len(current) > 0:
        for node in current:
            if node.is_goal:
                return path_length
            for child in node.adjacent:
                if not child.impassable and child not in explored:
                    next_nodes.add(child)
                    explored.add(child)
        current = next_nodes
        next_nodes = set()
        path_length += 1
    return len(map) * len(map[0])


def solution(map):
    # setup node map
    nodes = [[i for i in _] for _ in map]
    for row in range(len(map)):
        for col in range(len(map[0])):
            nodes[row][col] = Node(row, col, map[row][col])

    nodes[-1][-1].is_goal = True

    # setup adjacents
    for row in range(len(nodes)):
        for col in range(len(nodes[0])):
            if row > 0:
                nodes[row][col].add(nodes[row - 1][col])
            if row < len(nodes) - 1:
                nodes[row][col].add(nodes[row + 1][col])
            if col > 0:
                nodes[row][col].add(nodes[row][col - 1])
            if col < len(nodes[0]) - 1:
                nodes[row][col].add(nodes[row][col + 1])

    # now, find min distance
    min_dist = find_shortest_path(nodes)

    cur_num = 0
    # only try to remove impassable nodes w/ 2 or less impassable neighbors
    while cur_num < 3:
        removable_nodes = [
            node
            for row in nodes
            for node in row
            if node.impassable_neighbors == cur_num and node.impassable
        ]

        for node in removable_nodes:
            node.impassable = False
            min_dist = min(find_shortest_path(nodes), min_dist)
            node.impassable = True
        cur_num += 1

    return min_dist

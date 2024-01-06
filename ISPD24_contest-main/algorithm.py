import heapq

class Point3D:
    def __init__(self, x, y, metaln):
        self.x = x
        self.y = y
        self.metaln = metaln

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.metaln == other.metaln
    
    # define subtraction
    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.metaln - other.metaln)

    def __hash__(self):
        return hash((self.x, self.y, self.metaln))

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.metaln - other.metaln)

class AStarNode:
    def __init__(self, point, g, h, parent):
        self.point = point
        self.g = g
        self.h = h
        self.parent = parent

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

def get_neighbors(point):
    moves = []
    if point.metaln == 0:
        moves = [(0, 0, 1)]
    elif point.metaln % 2 == 1:
        moves = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    else:
        moves = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

    neighbors = []
    for dx, dy, dmetaln in moves:
        new_metaln = point.metaln + dmetaln
        if new_metaln >= 0: 
            neighbors.append(Point3D(point.x + dx, point.y + dy, new_metaln))
    return neighbors

def a_star_search(start, goal): # start, goal: Point3D
    open_set = []
    heapq.heappush(open_set, AStarNode(start, 0, start.manhattan_distance(goal), None))
    cost_so_far = {start: 0}

    while open_set:
        current = heapq.heappop(open_set) # current is the node with the lowest f() value

        if current.point == goal:
            path = []
            while current:
                path.append((current.point.x, current.point.y, current.point.metaln))
                current = current.parent
            return path[::-1]

        for neighbor in get_neighbors(current.point):
            new_cost = cost_so_far[current.point] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + neighbor.manhattan_distance(goal)
                heapq.heappush(open_set, AStarNode(neighbor, new_cost, priority, current))

    return None 

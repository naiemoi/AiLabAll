import copy

class EightPuzzleAOStar:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.heuristic_dict = {}
        self.parent = {}

    def get_manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    curr_x, curr_y = i, j
                    distance += abs(x - curr_x) + abs(y - curr_y)
        return distance

    def get_neighbors(self, state):
        neighbors = []
        x, y = next((r, c) for r, l in enumerate(state) for c, v in enumerate(l) if v == 0)
        moves = [((x-1, y), "Up"), ((x+1, y), "Down"), ((x, y-1), "Left"), ((x, y+1), "Right")]
        for (nx, ny), move in moves:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def solve(self):
        open_list = [(self.get_manhattan_distance(self.start), self.start)]
        visited = []
        print("Searching for solution...")

        while open_list:
            open_list.sort(key=lambda x: x[0])  # sort by heuristic
            h, current = open_list.pop(0)
            if current == self.goal:
                print("Goal Reached!")
                return True

            visited.append(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    cost = self.get_manhattan_distance(neighbor)
                    open_list.append((cost, neighbor))

        print("No solution found.")
        return False


# Example Usage
start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
solver = EightPuzzleAOStar(start_state, goal_state)
solver.solve()
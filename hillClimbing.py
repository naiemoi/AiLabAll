# 8-Puzzle using Hill Climbing (Python)

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# map each tile to its goal position
goal_pos = {}

def goal_map():
    for i in range(3):
        for j in range(3):
            goal_pos[GOAL[i][j]] = (i, j)

def calculate_manhattan(board):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                gi, gj = goal_pos[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_8_puzzle_hill_climbing(start):
    current = [row[:] for row in start]
    current_h = calculate_manhattan(current)

    # moves: down, up, right, left
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while True:
        if current == GOAL:
            print("Goal reached using Hill Climbing")
            return

        x, y = find_blank(current)
        best_neighbor = current
        best_h = current_h

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_board = [r[:] for r in current]
                next_board[x][y], next_board[nx][ny] = next_board[nx][ny], next_board[x][y]

                h = calculate_manhattan(next_board)
                if h < best_h:
                    best_h = h
                    best_neighbor = next_board

        if best_h >= current_h:
            print("Stopped at local minimum. Goal not reached.")
            return

        current = best_neighbor
        current_h = best_h
start_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_map()
print("Starting 8-Puzzle using Hill Climbing...")
solve_8_puzzle_hill_climbing(start_board)
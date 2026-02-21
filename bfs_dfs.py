from collections import deque

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = idx // 3, idx % 3

    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors



#bfs code
def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()   # FIFO

        if state == goal_state:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for neighbor in get_neighbors(state):
                queue.append((neighbor, path + [state]))

    return None



#dfs code
def dfs(start_state, depth_limit=20):
    stack = [(start_state, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()   # LIFO

        if state == goal_state:
            return path + [state]

        if depth < depth_limit and state not in visited:
            visited.add(state)
            for neighbor in get_neighbors(state):
                stack.append((neighbor, path + [state], depth + 1))

    return None



start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

bfs_result = bfs(start_state)
dfs_result = dfs(start_state)

print("BFS steps:", len(bfs_result)-1 if bfs_result else "No solution")
print("DFS steps:", len(dfs_result)-1 if dfs_result else "No solution")
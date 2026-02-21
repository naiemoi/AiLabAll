import heapq
# from queue import Empty
# from turtle import distance
Goal_state=((1,2,3),(4,5,6),
            (7,8,0))
moves=[(-1,0),(1,0),(0,-1),(0,1)]

def manhattan_distance(state):
    distance=0
    for r in range(3):
        for c in range(3):
            value=state[r][c]
            if value!=0:
                goal_r=(value-1)//3
                goal_c=(value-1)%3
                distance+=abs(r-goal_r)+abs(c-goal_c)
    return distance
                
def get_neighbors(state):
    neighbors=[]
    for r in range(3):
        for c in range(3):
            if state[r][c]==0:
                empty_r=r
                empty_c=c
                
    for dr,dc in moves:
        new_r=empty_r+dr
        new_c=empty_c+dc
        
        if 0<=new_r<3 and 0<=new_c<3:
            new_state=[list(row) for row in state]
            new_state[empty_r][empty_c], new_state[new_r][new_c] = \
            new_state[new_r][new_c], new_state[empty_r][empty_c]
            
            neighbors.append(tuple(tuple(row) for row in new_state))
            
    return neighbors
    

def best_first_search(start_state):
    open_list = [] # priority queue hisabe use kora hoyese
    heapq.heappush(open_list,(manhattan_distance(start_state),start_state,[]))   # ekhane 3 ti jinish tuple akare eksathe dokano hoyese (priority, current_state, path)
    visited=set()  # ekhane visited set ta use kora hoyese jate same state abar na dekha hoy
    
    
    while open_list:
        _,current_state,path=heapq.heappop(open_list)  #_ =heuristic value (ignore), current_state =যে state এখন expand হবে ,path= start theke ekhane ashar path
        
        if current_state==Goal_state:
            return path+[current_state]
        if current_state in visited:
            continue
        visited.add(current_state)
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                heapq.heappush(open_list,(manhattan_distance(neighbor),neighbor,path+[current_state]))
    return None
                
        
        
        
    
    
    
    
start_state=((1,2,3),(4,5,6),(7,0,8))
solution_path=best_first_search(start_state)

if solution_path:
    print("Solution found")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
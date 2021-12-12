import sys

def count_paths(graph, current, final, visited):
    if current == final:
        return 1
    
    if current.islower():
        if current in visited and 2 in visited.values():
            return 0
        
        if current in visited:
            visited[current] += 1
        else:
            visited[current] = 1
        
    result = 0
    
    for next in graph[current]:
        if next != 'start':
            result += count_paths(graph, next, final, visited.copy())
            
    return result
        
graph = {}

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break
    
    first,second = line.split('-')
    
    if first not in graph:
        graph[first] = []
        
    if second not in graph:
        graph[second] = []
        
    graph[first].append(second)
    graph[second].append(first)
    
print(count_paths(graph, 'start', 'end', {}))    


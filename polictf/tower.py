from pwn import *
from collections import deque

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0])
    graph = {(i, j): [] for j in range(1, width-1) for i in range(1, height) if j%2 != 0}
    print graph, height, width
    for y in range(1, height):
        for x in range(1, width-1):
            if x%2 != 0:
                if maze[y-1][x] == ' ':
                    graph[(y, x)].append(('N', (y-1, x)))
                if maze[y][x] == ' ':
                    graph[(y, x)].append(('S', (y+1, x)))
                if maze[y][x-1] == ' ':
                    graph[(y, x)].append(('W', (y, x-2)))
                if maze[y][x+1] == ' ':
                    graph[(y, x)].append(('E', (y, x+2)))
    return graph

def find_path_bfs(maze):
    start, goal = (120, 1), (120-gy, gx*2+1)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        print path, current
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

r = remote('tower.chall.polictf.it' ,31337)
r.recvline()
labyrinth = r.recvlines(121)

print labyrinth

start = r.recvline()[7:]
goal = r.recvline()[6:]

g = goal.split(',')
gx = int(g[0].strip())
gy = int(g[1].strip())

result = find_path_bfs(labyrinth)
result = result.replace('W', 'a').replace('N', 'w').replace('E', 'd').replace('S', 's') 
print result

r.sendline(result)
r.interactive()

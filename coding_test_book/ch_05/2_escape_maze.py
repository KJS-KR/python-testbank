n, m = 5, 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

# 왼쪽, 오른쪽, 위, 아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                # 이전 노드의 최단 거리 + 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))

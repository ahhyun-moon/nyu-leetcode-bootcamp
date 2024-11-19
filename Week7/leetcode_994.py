class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0:
            return -1
        # Thought Process:
        # Record rotten positions in grid and use BFS to count down fresh oranges
        # while converting fresh -> rotten every minute for adjacent oranges
        fresh_count = 0
        rotten_q = deque()        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        minute = 0
        pos = [(1,0), (-1,0), (0,1), (0,-1)]
        while rotten_q and fresh_count > 0:
            minute += 1
            for _ in range(len(rotten_q)):
                x, y = rotten_q.popleft()
                for dx, dy in pos:
                    xp, yp = x + dx, y + dy
                    if 0 <= xp < m and 0 <= yp < n and grid[xp][yp] == 1:
                        fresh_count -= 1
                        grid[xp][yp] = 2
                        rotten_q.append((xp, yp))
        return minute if fresh_count == 0 else -1

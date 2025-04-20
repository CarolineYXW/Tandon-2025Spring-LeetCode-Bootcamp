from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        minute = 0
        while queue and count > 0:
            minute += 1
            rotcount = len(queue)
            for k in range(rotcount):
                orgi, orgj = queue.popleft()
                if orgi-1 >= 0 and grid[orgi-1][orgj] == 1:
                    queue.append((orgi-1, orgj))
                    grid[orgi-1][orgj] = 2
                    count -= 1
                if orgi+1 < m and grid[orgi+1][orgj] == 1:
                    queue.append((orgi+1, orgj))
                    grid[orgi+1][orgj] = 2
                    count -= 1
                if orgj-1 >= 0 and grid[orgi][orgj-1] == 1:
                    queue.append((orgi, orgj-1))
                    grid[orgi][orgj-1] = 2
                    count -= 1
                if orgj+1 < n and grid[orgi][orgj+1] == 1:
                    queue.append((orgi, orgj+1))
                    grid[orgi][orgj+1] = 2
                    count -= 1

        if count > 0:
            return -1
        return minute
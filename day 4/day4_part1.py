with(open("./day4.input") as file):
    grid = file.readlines()

    m = len(grid)
    n = len(grid[0])

    def checkValid(i, j):
         return i >= 0 and i < m and j >= 0 and j < n

    def search(i, j):
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        
        res = 0
        for d in dirs:
            valid = True
            x, y = i, j
            for z in range(1, 4):
                x += d[0]
                y += d[1]
                if not checkValid(x, y) or grid[x][y] != "XMAS"[z]:
                    valid = False
                    break
            if valid:
                res += 1
        return res

    res = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "X":
                matches = search(i, j)
                res += matches
    print(res)

    

with(open("./day4.input") as file):
    grid = file.readlines()

    m = len(grid)
    n = len(grid[0])

    def checkValid(i, j):
         return i >= 0 and i < m and j >= 0 and j < n

    def search(i, j):
        
        dirs = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        
        for d in dirs:
            if not checkValid(i+d[0], j+d[1]):
                return False

        validStrings = ["MS", "SM"]

        a = grid[i+dirs[0][0]][j+dirs[0][1]]
        b = grid[i+dirs[1][0]][j+dirs[1][1]]
        c = grid[i+dirs[2][0]][j+dirs[2][1]]
        d = grid[i+dirs[3][0]][j+dirs[3][1]]

        if (a+b) in validStrings and (c+d) in validStrings:
            return True

    res = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "A":
                if search(i, j):
                    res += 1
    print(res)

    

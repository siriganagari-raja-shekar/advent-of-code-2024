with(open("./day5.input") as file):
    
    lines = file.readlines()
    
    i = 0

    rules = {}

    while lines[i].strip() != "":
        a, b = map(int, lines[i].split("|"))
        if a not in rules:
            rules[a] = set()

        rules[a].add(b)
    
        i += 1

    i += 1

    
    res = 0
    while i < len(lines):
        nums = list(map(int, lines[i].strip().split(",")))
        
        valid = True
        for j in range(len(nums)-1):
            if nums[j] not in rules or nums[j+1] not in rules[nums[j]]:
                valid = False
                break
        if valid:
            res += nums[len(nums)//2]
        i += 1

    print(res)



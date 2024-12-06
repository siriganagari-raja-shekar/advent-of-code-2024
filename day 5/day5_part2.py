from collections import Counter
import functools
with(open("./day5.input") as file):
    
    lines = file.readlines()
    
    i = 0

    rules = {}

    vertices = set()

    while lines[i].strip() != "":
        a, b = map(int, lines[i].split("|"))
        vertices.add(a)
        vertices.add(b)
        if a not in rules:
            rules[a] = set()
        rules[a].add(b)

        i += 1

    i += 1

    def isValid(nums):

        valid = True
        for j in range(len(nums)-1):
            if nums[j] not in rules or nums[j+1] not in rules[nums[j]]:
                valid = False
                break
        return valid

    res = 0

    def compare(a, b):
        if a not in rules or b not in rules[a]:
            return 1
        else:
            return -1

    while i < len(lines):
        nums = list(map(int, lines[i].strip().split(",")))
        
        if not isValid(nums):
            nums.sort(key=functools.cmp_to_key(compare))
            res += nums[len(nums)//2]

        i += 1

    print(res)



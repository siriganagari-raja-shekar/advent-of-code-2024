with(open("./day2.input") as file):
    res = 0
    for line in file.readlines():
        nums = list(map(int, list(s for s in line.split(" "))))
        inc = False
        diff = abs(nums[1] - nums[0])
        if diff < 1 or diff > 3:
            continue
        if nums[1] > nums[0]:
            inc = True
        valid = True
        for i in range(2, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            if diff < 1 or diff > 3:
                valid = False
                break
            if inc and nums[i] < nums[i-1] or not inc and nums[i] > nums[i-1]:
                valid = False
                break
        if valid:
            res += 1

    print(res)


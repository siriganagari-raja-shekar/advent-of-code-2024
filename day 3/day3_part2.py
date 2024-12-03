import re

with(open("./day3.input") as file):

    res = 0
    enabled = True
    for line in file.readlines():

        pairs = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', line)

        for pair in pairs:
            if pair[0] == "do()":
                enabled = True
            elif pair[0] == "don't()":
                enabled = False
            else:
                if enabled:
                    res += int(pair[1]) * int(pair[2])

    print(res)



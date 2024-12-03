import re
with(open("./day3.input") as file):
    res = 0
    for line in file.readlines():

        pairs = re.findall(r'mul\((\d+),(\d+)\)', line)

        res += sum(int(i) * int(j) for i, j in pairs)

    print(res)


    

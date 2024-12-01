with(open("./day1.input") as file):
    a, b = [], []
    for line in file.readlines():
        num1, num2 = map(int, list(s  for s in line.split(" ") if s and not s.isspace()))
        a.append(num1)
        b.append(num2)

    a.sort()
    b.sort()

    res = sum(list(abs(a[i]-b[i]) for i in range(len(a))))

    print(res)


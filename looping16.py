c = 2 * 5 - 2
for r in range(-1,4):
    for s in range(0,c):
        print(end=" ")
    c = c -1
    for x in range(0, r + 1):
        print("*",end = " ")
    print()

c = 5 - 2
for r in range(4, -1, -1):
    for s in range(c, 0, -1):
        print(end=" ")
    c = c + 1
    for x in range(0, r + 1):
        print("*", end=" ")
    print()
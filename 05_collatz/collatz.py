with open ("Prob05.in.txt") as f:
    f.readline()

    for line in f.readlines():
        start = int(line.strip())
        curr = start
        count = 1
        while curr != 1:
            if curr % 2 == 0:
                curr = curr / 2
            else:
                curr = curr * 3 + 1
            count += 1
        print(str(start) + ":" + str(count))
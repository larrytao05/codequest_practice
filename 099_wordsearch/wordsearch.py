with open("Prob099.in.txt") as f:
    lines = f.readlines()
    puzzle = []
    words = []

    first = True
    while len(lines) > 0:
        line = lines.pop(0)
        if first:
            if line != "\n":
                if line.replace("\n", "") != "#PUZZLE":
                    puzzle.append(line.replace("\n", ""))
            else:
                first = False
        elif line.replace("\n", "") != "#WORDS":
            words.append(line.replace("\n", ""))


    for word in words:
        start = word[0]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j] == start:
                    if i == 0 or i == len(puzzle) - 1:
                        

    
    print(puzzle)
    print(words)
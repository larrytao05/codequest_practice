with open("Prob101.in.txt") as f:
    lines = f.readlines()
    cards = []
    columns = ["B", "I", "N", "G", "O"]
    end_loop = False
    for i in range(0, len(lines) - 5, 5):
        current_card = []
        for j in range(5):
            line = lines.pop(0).replace("\n", "")
            if line == "PLAY":
                end_loop = True
                break
            next = list(map(int, line.split(" ")))
            if j == 2:
                next.insert(2, 0)
            current_card.append(next)      
        cards.append(current_card)  
        if end_loop:
            break
    while len(lines) > 1:
        move = (columns.index(lines[0][:1]), int(lines.pop(0).replace("\n", "")[1:]))
        for i in range(len(cards)):
            for j in range(len(cards[i])):
                if cards[i][j][move[0]] == move[1]:
                    cards[i][j][move[0]] = 0


    print(cards)
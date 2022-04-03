with open("Prob07.in.txt") as f:
    f.readline()
    for line in f.readlines():
        moves = list(line.replace("\n", " ").strip(" "))
        print(len(moves))

        # horizontal
        i = 0
        cont = True
        while i in range(len(moves)) and cont:
            if moves[i] != "-":
                if i+2 < len(moves):
                    if moves[i+1] == moves[i] and moves[i+2] == moves[i]:
                        print(line + " = " + moves[i] + " WINS")
                        cont = False
                if i < 3:
                    if moves[i + 3] == moves[i] and moves[i + 6] == moves[i]:
                        print(line + " = " + moves[i] + " WINS")
                        cont = False
                elif i == 4:
                    if moves[0] == moves[i] and moves[8] == moves[i]:
                        print(line + " = " + moves[i] + " WINS")
                        cont = False
                    elif moves[2] == moves[i] and moves[6] == moves[i]:
                        print(line + " = " + moves[i] + " WINS")
                        cont = False
            i += 1 
            if i == len(moves) - 1:
                print(line.replace("\n", " ").strip(" ") + " = TIE")
with open ("Prob03.in.txt") as f:
    f.readline()
    while True:
        line = f.readline().strip()[:-2]
        if not line:
            break
        else:
            if int(line[-1]) == 3:
                print(line + "rd")
            elif int(line[-1]) == 2:
                print(line + "nd")
            elif int(line[-1]) == 1:
                print(line + "st")
            else:
                print(line + "th")
        


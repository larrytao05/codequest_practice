with open("Prob061.in.txt") as f:
    f.readline()
    
    lines = f.readlines()
    while len(lines) > 1:
        ship_info = {}
        n = lines.pop(0)
        n = int(n)
        for i in range(n):
            line = lines.pop(0)
            (name, rest) = line.split("_")
            (ship_class, rest2) = rest.split(":")
            (x,y) = rest2.split(",")
            ship_info[name] = [ord(ship_class) - 64, x, y]

        for j in range(len(ship_info)):
            distances = []
            for ship in ship_info:
                distances.append((int(ship_info[ship][1]), ship))
                ship_info[ship][1] = int(ship_info[ship][1]) - 10 * ship_info[ship][0]
            distances.sort()
            destroyed = distances.pop(0)
            print("Destroyed Ship: " + destroyed[1] + " xLoc: " + str(destroyed[0]))
            ship_info.pop(destroyed[1])
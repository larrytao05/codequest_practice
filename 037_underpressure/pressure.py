import math

with open("Prob037.in.txt") as f:
    cases = f.readline()
    lines = f.readlines()

    while len(lines) > 0:
        name = lines.pop(0).split(" ")
        final_name = ""
        values = [int(x) for x in lines.pop(0).split(" ")]

        for word in name:
            final_name += word[0]
        
        avg = sum(values)/len(values)
        solutions = []
        for i in range(len(values)):
            poop = values[i]
            counter = 0
            index = i
            valves_opened = 0
            while i != index:
                while poop/(counter+1) != avg or i != index:
                    counter += 1
                    index += 1
                    if index == len(values):
                        index = 0
                    poop += values[index]


                if poop/counter == avg:
                    valves_opened += counter - 1
                else:
                    valves_opened = math.inf

                
            solutions.append(valves_opened)
            print(f"{final_name}: {min(solutions)}")


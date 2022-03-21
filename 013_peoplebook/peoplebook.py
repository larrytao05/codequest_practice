with open("Prob013.in.txt") as f:
    f.readline()
    


    count = 0
    headers = ["Age: ", "Instagram: ", "Twitter: ", "Phone: ", "Email: "]
    for line in f.readlines():
        count += 1
        if count == 1:
            length = int(line)
        if count == length + 3:
            count = 1
        if count == 2:
            peoples = []
            li = line.strip("\n")[1:-1].split("],")
            for i in range(len(li)):
                li[i] = (li[i] + "]").strip("][").split(",")
            for i in range(6):
                if i == 0:
                    for name in li[i]:
                        peoples.append([name])
                else:
                    for j in range(len(peoples)):
                        peoples[j].append(li[i][j])
            for person in peoples:
                print("Name: " + person[0])
                for k in range(len(headers)):
                    print(headers[k] + person[k + 1])

        
        
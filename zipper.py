with open("Prob014.in.txt") as f:
    f.readline()

    upperLines = int(f.readline())

    upperLengths = list(map(int, (item.strip(" ") for item in f.readline().split(" "))))
    lowerLines = int(f.readline())
    lowerLengths =  list(map(int, (item.strip(" ") for item in f.readline().split(" "))))

    print(upperLengths)

    lines = f.readlines()

    upperMessage = ""
    lowerMessage = ""

    upperCount = 0
    lowerCount = 0
    upperIndex = 0
    lowerIndex = 0
    chars = ""
    for line in lines:
        for char in line:
            chars += char

    for char in chars.strip("\n"):
        if char.islower():
            lowerMessage += char
        elif char == "=":
            lowerMessage += " "
        elif char == "-":
            upperMessage += " "
        else:
            upperMessage += char
            

    upperMessage = list(upperMessage.replace("\n", ""))
    count = 0

    for i in range(len(upperLengths)):
        sum = 0
        for item in upperLengths[:i]:
            sum += item

        upperMessage.insert(upperLengths[i] + sum + count, "\n")
        count += 1

    lowerMessage = list(lowerMessage.replace("\n", ""))
    count = 0
    for i in range(len(lowerLengths)):
        sum = 0
        for item in lowerLengths[:i]:
            sum += item
        lowerMessage.insert(lowerLengths[i] + sum + count, "\n")
        count += 1
    print("".join(map(str, upperMessage)))
    print("".join(map(str, lowerMessage)))
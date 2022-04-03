


with open("Prob048.in.txt") as f:
    f.readline()
    lines = f.readlines()
    while len(lines) > 0:
        print("\n")
        mode = lines.pop(0)
        cipher = list(lines.pop(0))
        num_messages = int(lines.pop(0))
        for i in range(num_messages):
            message = lines.pop(0).replace("\n", "")
            final = ""
            if mode == "ENCRYPT\n":
                for char in message:
                    if char.islower():
                        val = ord(char) - 97
                        if val >= 0 and val < 26:
                            final += cipher[val]
                    elif char.isupper():
                        val = ord(char) - 65
                        if val >= 0 and val < 26:
                            final += cipher[val].capitalize()
                    else:
                        final += char
            else:
                for char in message:
                    if char.islower():
                        val = cipher.index(char)
                        final += chr(val + 97)
                    elif char.isupper():
                        val = cipher.index(char.lower())
                        final += chr(val + 65)
                    else:
                        final += char
            print(final)
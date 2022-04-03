from re import L


with open("Prob028.in.txt") as f:
    f.readline()
    lines = f.readlines()
    key = []
    for i in range(len(lines)):
        if i % 2 == 0:
            encoded = ""
            if len(key) > 0:
                
                for j in range(len(lines[i].replace("\n", ""))):
                    if ord(lines[i].replace("\n", "")[j]) - 64 > 0 and ord(lines[i].replace("\n", "")[j]) - 64 <= 26:
                        val = ord(lines[i].replace("\n", "")[j]) - 64
                        key_index = j % len(key)
                        keyval = ord(key[key_index]) - 64
                        if val + keyval <= 26:
                            encoded += chr(val + keyval + 64)
                        else:

                            newval = (val + keyval) % 26
                            print(chr(newval + 64))
                            encoded += chr(newval + 64)
                    else:
                        encoded += lines[i].replace("\n", "")[j]
                print(encoded)
            
        else:
            key = list(lines[i].replace("\n", ""))
            print(key)

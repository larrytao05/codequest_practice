with open("Prob112.in.txt") as f:
    f.readline()
    lines = f.readlines()
    for i in range(0, len(lines), 2):

        shift = int(lines[i])
        encrypted_message = lines[i + 1]
        decrypted_message = "" 

        for char in encrypted_message:
            if ord(char) - 96 <= 26 and ord(char) - 96 > 0:
                val = ord(char) - 96
                if val - shift >= 0:
                    decrypted_message += chr(val - shift + 96)
                else:
                    decrypted_message += chr(val - shift + 26 + 96)                   
            else:
                decrypted_message += char
        print(decrypted_message)
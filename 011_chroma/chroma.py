import math

with open ("Prob011.in.txt") as f:
    f.readline()
    for line in f.readlines():
        vals = list(map(int, line.strip("\n").split(" ")))
        
        chroma_key = vals[0:3]
        tolerance = vals[3]
        fg = vals[4:7]
        bg = vals[7:]

        print(math.sqrt((bg[0] - chroma_key[0])**2 + (bg[1]-chroma_key[1])**2 + (bg[2] - chroma_key[2])**2))
        print(math.sqrt((fg[0] - chroma_key[0])**2 + (fg[1]-chroma_key[1])**2 + (fg[2] - chroma_key[2])**2))

        if math.sqrt((bg[0] - chroma_key[0])**2 + (bg[1]-chroma_key[1])**2 + (bg[2] - chroma_key[2])**2) <= tolerance:
            print(str(bg[0]) + " " + str(bg[1]) + " " + str(bg[2]))
        if math.sqrt((fg[0] - chroma_key[0])**2 + (fg[1]-chroma_key[1])**2 + (fg[2] - chroma_key[2])**2) <= tolerance:
            print(str(fg[0]) + " " + str(fg[1]) + " " + str(fg[2]))

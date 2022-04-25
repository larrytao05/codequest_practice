from fractions import Fraction
from math import floor

with open("Prob_128.in.txt") as f:
    f.readline()
    lines = f.readlines()

    for line in lines:
        vals = line.replace("\n", "")
        ones = Fraction(line.split(".")[0])
        decimal = Fraction("." + line.split(".")[1])
        output = [str(ones)]
        count = 1
        while Fraction(floor(decimal)) != decimal and count < 10:
            count += 1
            new_line = Fraction(1)/decimal
            ones = Fraction(floor(new_line))
            decimal = Fraction(new_line - ones)
            output.append(str(ones))
            decimal = Fraction(decimal)

    
        print(" ".join(output))



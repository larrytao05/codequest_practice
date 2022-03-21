with open ("Prob012.in.txt") as f:
    f.readline()
    for line in f.readlines():
        lim = int(line.strip())
        nums = []
        for i in range(2, lim + 1):
            nums.append(i)

        final = []
        while nums:
            val = nums[0]
            nums.pop(0)
            final.append(val)
            count = 0
            for num in nums:
                if num % val == 0:
                    nums.remove(num)
                    count += 1
            if count > 0:
                print("Prime " + str(val) + " Composite Set Size: " + str(count))

        printval = ",".join(map(str, final))
        print("{" + printval + "}")
with open("Prob031.in.txt") as f:
    f.readline()
    lines = f.readlines()

    interest = 0.18

    while len(lines) > 0: 
        billing_period = int(lines.pop(0).replace("\n", ""))
        periods_per_year = round(365.00 / billing_period)
        sum_daily_balances = 0
        balance = 0


        for _ in range(billing_period):
            next = [float(x) if x != "" else 0.0 for x in lines.pop(0).replace("\n", "").split(",")[1:]]
            (charge, payment) = next
            balance += charge
            balance -= payment
            sum_daily_balances += balance

        print(round((sum_daily_balances / billing_period) * (interest / periods_per_year), 2))
def finance_calc_complete():
    principle = eval(input("Enter the amount you will deposit: "))
    interest = eval(input("Enter the annual % rate as a decimal: "))
    time = eval((input("Enter the number of years: ")))
    period = eval(input("Enter the number of periods the interest will accrue: "))
    payment = eval(input("Enter the amount you will pay each period: "))
    initial_principle = principle

    for i in range(time * period):
        payment_counter = (payment * (i + 1))
        earnings = (principle * (interest / period))
        principle = earnings + principle + payment
        total_earnings = (principle - initial_principle) - payment_counter
        print("Period: ", f"{(i+1)}", "You now have:", f"${principle:1.2f}", "and have deposited a total of",
              f"${payment_counter + initial_principle:1.2f}", "and earned a total of", f"${total_earnings:1.2f}")


finance_calc_complete()

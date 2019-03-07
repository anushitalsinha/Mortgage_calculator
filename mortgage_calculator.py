'''Makes a mortgage calculator'''

num_of_years = float(input("Please specify the number of years you want to take the mortgage for: "))
payment_period = 12 * num_of_years

annual_int_rate = float(input("What is the interest rate charged? "))
monthly_interest = annual_int_rate/(100*12)

loan_amount = float(input("What is the loan amount? "))

# calculate the monthly payment
r = 1 + monthly_interest
monthly_payment_numerator = loan_amount * (monthly_interest *(r ** payment_period))
monthly_payment_denominator = (r ** payment_period)-1
monthly_payment = monthly_payment_numerator/monthly_payment_denominator
print("The monthly payment is $" + str(monthly_payment))


# make a function to ask for input values

def main():
    payment_period = int(input("Please specify the number of years you want to take the mortgage for: "))*12
    annual_interest_rate = float(input("What is the interest rate charged? "))
    loan_amount = float(input("What is the loan amount? "))
    amortization_func(loan_amount, payment_period, annual_interest_rate)

# fucntion to calculate monthly installment
def pmt_func(loan_amount,payment_period,annual_interest_rate):
    monthly_interest = annual_interest_rate/(100*12)
    r = 1 + monthly_interest
    monthly_payment_numerator = loan_amount * (monthly_interest *(r ** payment_period))
    monthly_payment_denominator = (r ** payment_period)-1
    monthly_payment = monthly_payment_numerator/monthly_payment_denominator
    return monthly_payment, monthly_interest

# make an amortization table
def amortization_func(loan_amount,payment_period,annual_interest_rate):
    ''' calculates the amortization table and displays it to the user in a tabular form if asked by the user'''
    monthly_payment, monthly_interest = pmt_func(loan_amount,payment_period,annual_interest_rate)
    principal = loan_amount
    width = 11
    print("Pay_number | int_payment | pr_payment | pr_outstanding | principal")
    for i in range(payment_period):
        interest_payment = principal * monthly_interest
        principal_payment = monthly_payment - interest_payment
        principal_outstanding = principal - principal_payment
        principal = principal_outstanding
        interest_payment_str = f'{interest_payment:.2f}'
        principal_payment_str = f'{principal_payment:.2f}'
        principal_outstanding_str = f'{principal_outstanding:.2f}'
        principal_str = f'{principal:.2f}'
        print(str(i+1).rjust(width)+ '|'+ interest_payment_str.rjust(width + 2) + '|'+ principal_payment_str.rjust(width+1)+ '|'+
            principal_outstanding_str.rjust(width+5)+ '|'+principal_str.center(width))


if __name__ == "__main__":
    main()



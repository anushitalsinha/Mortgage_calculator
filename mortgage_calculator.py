# calculate the monthly payment
def pmt_func(loan_amount,payment_period,annual_interest_rate):
    monthly_interest = int_rate/(100*12)
    r = 1 + monthly_interest
    monthly_payment_numerator = loan_amount * (monthly_interest *(r ** payment_period))
    monthly_payment_denominator = (r ** payment_period)-1
    monthly_payment = monthly_payment_numerator/monthly_payment_denominator
    return monthly_payment

def main():
    '''Makes a mortgage calculator and calculates the monthly payment on the mortgage'''
    payment_period = float(input("Please specify the number of years you want to take the mortgage for: "))*12
    annual_interest_rate = float(input("What is the interest rate charged? "))
    loan_amount = float(input("What is the loan amount? "))
    print("The user input is : " + payment_period + annual_interest_rate+loan_amount + " and the monthly payment is: " +
        str(pmt_func(loan_amount, payment_period,annual_interest_rate)))

if __name__ == "__main__":
    main()
    # print(pmt_func(loan_amount,payment_period,annual_interest_rate))
  
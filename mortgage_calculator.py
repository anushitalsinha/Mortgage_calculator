# calculate the monthly payment
def pmt_func(loan_amount,pay_period,mon_int):
    r = 1 + mon_int
    mon_pay_numerator = loan_amount * (mon_int *(r ** pay_period))
    mon_pay_denominator = (r ** pay_period)-1
    monthly_payment = mon_pay_numerator/mon_pay_denominator
    return monthly_payment

def main():
    '''Makes a mortgage calculator and calculates the monthly payment on the mortgage'''
    pay_period = float(input("Please specify the number of years you want to take the mortgage for: "))*12
    ann_int_rate = float(input("What is the interest rate charged? "))
    mon_int = ann_int_rate/(100*12)
    loan_amount = float(input("What is the loan amount? "))
    pmt = pmt_func(loan_amount, pay_period, mon_int)
    k = f"The user input is : {pay_period} months, {ann_int_rate:.2f}% " + \
        f"interest, ${loan_amount:.2f} loan and the monthly payment is: ${pmt:.2f}."
    print(k)

if __name__ == "__main__":
    main()
    
  
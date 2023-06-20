#TASK 5 - CAPSTONE PROJECT

import math

print("Investment - To calculate the amount of interest you'll earn on your investement.")
print("Bond       - To calculate the amount you'll have to pay on a home loan.")

# Request for input on what the user wants to calculate
user_input = input("Enter either 'investment' or 'bond' to proceed: ")
user_input = user_input.lower() #lowers all letters, so there is no diference between size of letters

# Calculation for Investment
if user_input == "investment":
    deposit_amount = input("Enter amount of money you will deposit: ")
    interest_rate = input("Enter interest rate (only number, without '%' sign): ")
    investing_years = input("Number of years you plan on investing: ")
    interest_type = input("What type of interest you want? 'Simple' or 'Compound'. ")
    interest_type = interest_type.lower()
    P = int(deposit_amount)
    r = int(interest_rate)
    t = int(investing_years)

    # Calculation and output for Investment with simple interest
    if interest_type == "simple":
        amount = P * ( 1 + ((r/100)*t))
        print(" ")
        print("You will get back the amount of {:.2f} after {} years.".format(amount,investing_years))
    
    # Calculation and output for Investment with compound interes
    elif interest_type == "compound":
        amount = P * math.pow((1 + r/100),t)
        print(" ")
        print("You will get back the amount of {:.2f} after {} years.".format(amount,investing_years))
    
    # Outpu in case input is not simple or compound
    else:
        print(" ")
        print("Input error! Please restart the calculator and enter either 'simple' or 'compound' to proceed. ")

# Calculation and output for bond option
elif user_input == "bond":
    present_value = input("Enter the present value of the house: ")
    interest_rate1 = input("Enter interest rate (only number, without '%' sign): ")
    repay_time = input("Enter the number of months you plan to repay the bond: ")
    P = int(present_value)
    i = int(interest_rate1)/100/12
    n = int(repay_time)
    repayment = (i*P)/(1-(1+i)**(-n))
    print(" ")
    print("You will have to pay the amount {:.2f} every month.".format(repayment))

# Output in case input is not investment or bond
else:
    print(" ")
    print("Input error! Please restart the calculator and enter either 'investment' or 'bond' to proceed. ")

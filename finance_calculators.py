import math

print("Welcome to a Financial Calculator")
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calcualte the amount you'll have to pay on a home loan")
print()

#These are variables that will be used for Investment option
principal_amount = 0.00
interest_rate = 0.00
num_of_years = 0.00
total_amount = 0.00
interest = ""
interest_to_earn = 0.00

#These are the variables that will be used for Bond option
repayment = 0
present_value = 0.00
num_of_months = 0
numerator = 0
denominator = 0

invest_or_bond_values = {"investment", "bond"}  # Set of values allowed before the user proceeds

#This code converts the user's import to small letters as stipulated at the set of values allowed
invest_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#These are the set of values allowed in the program in calculating investments
simple_or_compound_values = {"simple", "compound"}

#I searched on Youtube how to validate a user's input (Joshua Bastean Youtube Channel: While loop for input validation)
#Initially my program didn't validate the user's import it just printed an error message and the user would have to start over again
#This code checks if the user's input is valid 
while invest_or_bond not in invest_or_bond_values:  # Check if input is not in the set of correct values
    print("Incorrect, please enter 'investment' or 'bond' from the menu above to proceed: ")
    invest_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()  # Changes user's input to small characters

#If user enters investment,the code asks the user a series of questions regarding the details of the investment the user wants to undertake
# The code also validates the user's input numbers        
if invest_or_bond == "investment":
    interest = input("Do you want simple or compound intesrest? Enter simple or compound: ").lower()  # Changes the user's input to small characters
    try:
    
        principal_amount = float(input("How much are you depositing? "))
        interest_rate = float(input("Enter the interest rate, just a number only without percentage sign: "))
        num_of_years = float(input("How many years do you plan on investing? "))
        if principal_amount < 0 or interest_rate < 0 or num_of_years < 0:
            raise ValueError("You cannot deposit negative money or have negative interest rate and years can't be negative. ")
    except ValueError:
        print("Please enter valid positive whole numbers. ")
        exit()

    #This code checks if the user's input is valid
    #If the user enters Capital letters, this code changes to small letters than validated
    while interest not in simple_or_compound_values:
        interest = input("Please enter 'simple' or 'compound': ").lower()

    #This code calculates the total amount to be earned for simple interest
    if interest =="simple":
        total_amount = principal_amount*(1+((interest_rate)/(100))*num_of_years)
        print(f"You will earn a total of R{round(total_amount, 2)}")  # Prints the total amount earned

    #This code calculates the total amount to be earned for compound interest
    elif interest == "compound":
        total_amount = principal_amount*math.pow(1+(interest_rate)/100, num_of_years)
        print(f"You will earn a total of R{round(total_amount, 2)}")  # Prints the total amount earned
    
#This code is executed if the user selects bond
#This code asks the user a series of questions and calculates the monthy repayment
#This code also validates the users input answers
elif invest_or_bond == "bond":
    try:
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = (float(input("Please enter the interest rate, just a number only without the percentage sign: ")))/100
        num_of_months = int(input("How many months are you planning to repay the bond? "))
        if present_value < 0 or interest_rate < 0 or num_of_months < 0:
            raise ValueError("You cannot deposit negative money or have negative interest rate and months can't be negative. ")
    except ValueError:
        print("Please make sure you have entered positive whole numbers")
        exit()
    
    #The formual to calcualte the monthly repayment was split into two variables
    #These variables are numerator and denominator
    numerator = (interest_rate)/12
    denominator =  1 - (1 + interest_rate)**(-num_of_months)

    repayment = (numerator*present_value)/denominator  # Calculates the monthly repayment

    print(f"Your monthly repayment is R{round(repayment, 2)}")  # Prints the monthly repayment value



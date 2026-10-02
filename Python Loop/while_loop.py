

# 1. Login System — while + if/else + break  ,,,,,,,,,,,,,,,,,,,, _________

correct_password = "5656"
user_pin = ""
attempt = 0
remained = 0

while attempt < 5:
    user_pin = input("Pleas enter your pin: ")
    if user_pin == correct_password:
        print("Congratulations!.....")
        break
    else:
        print("Sorry!... Your passwort is incorrect")
        attempt += 1
        remained = 5-attempt
        print("You are tried password: ", attempt, ", And You have reached the limit: ", remained)

if attempt == 5:
    print("Sorry! your account is locked")


# 2. ATM — while True + break + if/elif

balance = 1000
while True:
    print("\nYour current sufficient balance is: ", balance)
    amount = int(input("Enter withdrawal amount (0 to exit): "))

    if balance == 0:
        break

    elif amount > balance:
        print("Your Insufficient balance")
    else:
        balance = balance-amount
        print("\nWithdrawal successful: ", amount)
        print("Remaining balance: ", balance)

print("Thank you for using this program")


# 3. Shopping Cart — while + list + continue




















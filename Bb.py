from datetime import date, datetime
import os ,calendar

today = date.today()
months = list(calendar.month_name)

#(not so important stuff above)

#class bank_acc():





print("Welcome to important bank!\nhow can we help you today?")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_age(born):
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#class bankaccount:

    #def __init__(self,"type","name",age,"residents"):

def what_acc():
    bank_types = ['checking','Savings', 'Certificate of Deposit',"Unsure"]
    print("\nHi I'm Bank bot")
    print("you have chosen to create account with us today!")
    print("If you know what account you want to open just type the number that\'s beside the type of accounts shown")
    print("if not then I can help.")


    for i,type in enumerate(bank_types,1):
        print(f'{i}:{type}')


    while True:
           user_type = input("")
           if user_type == "1":
                        clear()
                        print("You have chosen checking.")
                        x = input("Do you want to continue? Yes,or no?")
                        if x.casefold() == "yes":
                            bot()
                            return "Checking"
                        elif x.casefold() == "no":
                            what_acc()
                            break
           elif user_type == "2":
                        clear()
                        print("You have chosen Savings.")
                        x = input("Do you want to continue? Yes,or no?")
                        x.casefold()
                        if x.casefold() == "yes":
                            bot()
                            return "Savings" #will be a function
                        elif x.casefold() == "no":
                            what_acc()
                            break
           elif user_type == "3":
                        clear()
                        print("You have chosen Certificate of Deposit.")
                        x = input("Do you want to continue? Yes,or no?")
                        x.casefold()
                        if x.casefold() == "yes":
                            bot()
                            return "Certificate of deposit"
                        elif x.casefold() == "no":
                            what_acc()
                            break
           elif user_type == "4":
                        clear()
                        print("You are unsure as to what account to open.")
                        x = input("Is that correct? Yes,or no?")
                        x.casefold()
                        if x.casefold() == "yes":
                            clear()
                            questions()
                            return "Unsure"
                        elif x.casefold() == "no":
                            what_acc()
                            break

def questions():
     print("You're unsure as of what type of account it right for you.")
     print("If not, type 'help' and I’ll ask a few questions to guide you.\n")
     while True:
         q1 = input("Do you plan to use your account for daily spending (like paying bills or buying things)?Type yes or no").lower()
         if q1 not in ["yes", "no"]:
             print("invalid response")
             continue
         clear()
         q2 = input("Do you want to save money and earn interest over time?Type yes or no").lower()
         if q2 not in ["yes", "no"]:
             print("invalid response")
             continue
         clear()
         q3 = input( "Are you okay with leaving your money untouched for a set time to earn higher interest?Type yes or no").lower()
         if q2 not in ["yes", "no"]:
              print("invalid response")
              continue
         break
     if q1 == "yes" and q2 == "no":
         print("I've determined that a checking account is best for you,best for everyday use and easy access to your money.")
         bot()
         return "Checking"
     elif q2 == "yes" and q3 == "no":
         print("I've determined that a Savings Account is best for you,great for saving money and earning some interest.")
         bot()
         return "Savings"
     elif q3 == "yes":
         print("I've determined that a Certificate of Deposit (CD) Account is best for you,perfect if you want higher interest and don’t need quick access.")
         bot()
         return "Certificate of deposit"
     else:
         print("It sounds like you’re not sure yet — maybe start with a Savings Account and go from there.")
         bot()
         return "Saving"

def bot():
    print(f"To create a account,I first need  need some info about yourself")
    name = input("what would you like me to call you?")
    user_home = input("Where do you live?")
    print("when were you born?")
    while True:
        bmonth = input('Month:')
        clear()
        try:
            x = int(bmonth)
            if x > 12 or x < 1:
                print("I don't think that month exists quite yet")
                x = input('Try again month:')
                clear()
            else:
                bmonth = x
                print(bmonth)
                break
        except ValueError:
            x = bmonth.capitalize()
            if x not in months:
                print(f"I don't think {x} exists quite yet,as month anyway")
            else:
                month = months.index(x)
                bmonth = month
                print(bmonth)
                break

    while True:
        print('The day of your birth must be a number')
        bday = input('Day:')
        try:
            x = int(bday)

            months_with_31_days = (1, 3, 5, 7, 8, 10, 12)
            months_with_30_days = (4, 6, 9, 11)
            feb = 2

            if bmonth in months_with_31_days and x > 31 or x < 1:
                print("day doesn't esit in month")

            elif bmonth in months_with_30_days and x > 30 or x < 1:
                print("day doesn't esit in month")

            elif bmonth == feb and x > 29 or x < 1:
                print("day doesn't esit in month")

            else:
                x = bday
                break
        except ValueError:
            print('Must be a number')

    while True:
        print("your birth year must be a number also")
        byear = input("Birth year:")
        clear()
        try:
            x = int(byear)
            if x > 2025 or x == 2025 or x < 2025:
                print("Are you sure this is your birth year?")
                check = input('yes or no')
                check.casefold()
                if check == "no":
                    byear = input("That's fine just enter a new year")
                elif check == "yes":
                    x = byear
                    break
                else:
                    check = input("not  yes or no")

        except ValueError:
            print("not a number")

    user_birth = date(int(byear), int(bmonth), int(bday))

    age = calculate_age(user_birth)

    print(f'age:{age}')

    print("Your birthday:", user_birth)
    print(f"You live at {user_home}")
    print(f"How can I help you today,{name}?")

    return name,user_birth,user_home,age


def action_sel():
    count = 0
    opition_list = ["Open an Account", "Make Deposits or Withdrawals", "check bank balance","exit program"]
#action ui
    for i,action in enumerate (opition_list,start =1):
        print (f'{i}:{action}')

    while True:
           pick_action = input("\npick a action,by typing a number")
           if pick_action == "1":
                        clear()
                        print("You have chosen Account creation.")
                        x = input("Do you want to continue? Yes,or no?")
                        x.casefold()
                        if x == "yes":
                            print("you have chosen to proceed with account creation,with our bank,important bank.")
                            print("unfortunately we are short staffed at the moment.")
                            print("so to help with you account creation,bank bot with take things from here.")
                            what_acc()
                            break
                        elif x == "no":
                            print("That's fine returning back to menu!")
                            action_sel()
                            break

           elif pick_action == "2":
                        clear()
                        print("You have chosen to Make Deposits or Withdrawals.")
                        x = input("Do you want to continue? Yes,or no?")
                        x.casefold()
                        if x == "yes":
                            print("Make Deposits or Withdrawals")#will be a function
                            break
                        elif x == "no":
                            print("That's fine returning back to menu!")
                            action_sel()
                            break

           elif pick_action == "3":
                        clear()
                        print("You have chosen to  check bank balance.")
                        x = input("Do you want to continue? Yes,or no?")
                        x.casefold()
                        if x == "yes":
                            print("check bank balance")
                        elif x == "no":
                            print("That's fine returning back to menu!")
                            action_sel()
                            break

           elif pick_action == "4":
                print("Thanks for visiting")
                break

           else:
               print("Invalid response,try again")



action_sel()














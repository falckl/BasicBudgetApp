#secondary app once the budgets are initialised.

#Find out what user wants to do, perform that action (if conditions allow - enough balance available)

#import the budget class & methods, also import objects & variables needed

from budgetV2 import Budget

from AppInitialiser import category1, category2, category3, allcats

print("""Hi! What would you like to do today?

W = withdraw
D = deposit
T = transfer between categories
C = check your balance
""")


action = input("")

if action == "W":
    #withdraw: find out where to withdraw from, use method, update budget file.
    print(f"""Where would you like to withdraw from?
    Your options are:
    {allcats}""")
    source = input("")

    if source in allcats:
        print("How much would you like to withdraw?")
        try:
            amount = int(input(""))
        except ValueError:
            print("Error, please enter a number")
        
        #use withdrawal method
        if source == "food":
            prevbalance = category1.balance
            if amount <= prevbalance:
                category1.balance = category1.withdraw(amount)
                currentbalance = category1.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        elif source == "clothing":
            prevbalance = category2.balance
            if amount <= prevbalance:
                category2.balance = category2.withdraw(amount)
                currentbalance = category2.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        elif source == "entertainment":
            prevbalance = category3.balance
            if amount <= prevbalance:
                category3.balance = category3.withdraw(amount)
                currentbalance = category3.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        print(f"You have withdrawn {amount} from {source}.\n Your balance has decreased from {prevbalance} to {currentbalance}")

        #could have more elifs for further "empty" categories which will only be accessed if they exist.

        #update main file
        #open file to read it, dictionary to update info.
        budgetfile = open("budgetfile.txt","r") #read first to copy info.
        budgetdict = {}
        for line in budgetfile:
            category, catbudget = line.split()
            catbudget = int(catbudget)
            if category == source:
                catbudget = currentbalance
            budgetdict[category] = catbudget
        budgetfile.close
        #open file and overwrite with updated values
        budgetfile = open("budgetfile.txt","w")

        list_of_strings = [f"{key} {budgetdict[key]}" for key in budgetdict]
        for st in list_of_strings:
            budgetfile.write(f"{st}\n") 

    else:
        print("Please choose a valid category")


elif action == "D":
    #deposit: find out where to make the deposit, use method, update budget file
    print(f"""Where would you like to make your deposit to?
    Your options are:
    {allcats}""")
    destination = input("")

    if destination in allcats:
        print("How much would you like to deposit?")
        try:
            amount = int(input(""))
        except ValueError:
            print("Error, please enter a number")
        
        #use deposit method
        if destination == "food":
            prevbalance = category1.balance
            print(category1.__dict__)
            category1.balance = category1.deposit(amount)
            currentbalance = category1.balance
        elif destination == "clothing":
            prevbalance = category2.balance
            category2.balance = category2.deposit(amount)
            currentbalance = category2.balance
        elif destination == "entertainment":
            prevbalance = category3.balance
            category3.balance = category3.deposit(amount)
            currentbalance = category3.balance
        print(f"You have deposited {amount} to {destination}.\n Your balance has increased from {prevbalance} to {currentbalance}")

        #update main file
        #open file to read it, dictionary to update info.
        budgetfile = open("budgetfile.txt","r") #read first to copy info.
        budgetdict = {}
        for line in budgetfile:
            category, catbudget = line.split()
            catbudget = int(catbudget)
            if category == destination:
                catbudget = currentbalance
            budgetdict[category] = catbudget
        budgetfile.close
        #open file and overwrite with updated values
        budgetfile = open("budgetfile.txt","w")

        list_of_strings = [f"{key} {budgetdict[key]}" for key in budgetdict]
        for st in list_of_strings:
            budgetfile.write(f"{st}\n") 
        
    else:
        print("Please choose a valid category")

elif action == "T":
    #transfer - find out source, destination, amount. withdraw from source, deposit at destination.
    print(f"""Where would you like to make your transfer FROM?
    Your options are:
    {allcats}""")
    source = input("")
    print("Where would you like to make this transfer to?")
    destination = input("")
    if source in allcats and destination in allcats:
        print("How much would you like to transfer?")
        try:
            amount = int(input(""))
        except ValueError:
            print("Error, please enter a number")
        
        #withdraw from source
        if source == "food":
            prevbalance = category1.balance
            if amount <= prevbalance:
                category1.balance = category1.withdraw(amount)
                currentbalance = category1.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        elif source == "clothing":
            prevbalance = category2.balance
            if amount <= prevbalance:
                category2.balance = category2.withdraw(amount)
                currentbalance = category2.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        elif source == "entertainment":
            prevbalance = category3.balance
            if amount <= prevbalance:
                category3.balance = category3.withdraw(amount)
                currentbalance = category3.balance
            else:
                print("You do not have sufficient funds to make this withdrawal")
        print(f"You have withdrawn {amount} from {source}.\n Your balance has decreased from {prevbalance} to {currentbalance}")
        
        budgetfile = open("budgetfile.txt","r") #read first to copy info.
        budgetdict = {}
        for line in budgetfile:
            category, catbudget = line.split()
            catbudget = int(catbudget)
            if category == source:
                catbudget = currentbalance
            budgetdict[category] = catbudget
        budgetfile.close
        #open file and overwrite with updated values
        budgetfile = open("budgetfile.txt","w")

        list_of_strings = [f"{key} {budgetdict[key]}" for key in budgetdict]
        for st in list_of_strings:
            budgetfile.write(f"{st}\n") 

        #deposit at destination
        if destination == "food":
            prevbalance = category1.balance
            print(category1.__dict__)
            category1.balance = category1.deposit(amount)
            currentbalance = category1.balance
        elif destination == "clothing":
            prevbalance = category2.balance
            category2.balance = category2.deposit(amount)
            currentbalance = category2.balance
        elif destination == "entertainment":
            prevbalance = category3.balance
            category3.balance = category3.deposit(amount)
            currentbalance = category3.balance
        print(f"You have deposited {amount} to {destination}.\n Your balance has increased from {prevbalance} to {currentbalance}")

        budgetfile = open("budgetfile.txt","r") #read first to copy info.
        budgetdict = {}
        for line in budgetfile:
            category, catbudget = line.split()
            catbudget = int(catbudget)
            if category == destination:
                catbudget = currentbalance
            budgetdict[category] = catbudget
        budgetfile.close
        #open file and overwrite with updated values
        budgetfile = open("budgetfile.txt","w")

        list_of_strings = [f"{key} {budgetdict[key]}" for key in budgetdict]
        for st in list_of_strings:
            budgetfile.write(f"{st}\n")

    else:
        print("Please enter a valid category")

elif action == "C":
    #check balance - find out which one
    print(f"""Which balance would you like to check?
    Your options are:
    {allcats}""")
    source = input("")
    if source in allcats:
        if source == "food":
            currentbalance = category1.balance
        elif source == "clothing":
            currentbalance = category2.balance
        elif source == "entertainment":
            currentbalance = category3.balance
        print(f"Your current balance for {source} is {currentbalance}")
    else:
        print("Please choose a valid category")

else:
    print("Please choose a valid action")
from budgetV2 import Budget

from os.path import exists

file_exists = exists("budgetfile.txt")

if file_exists == False:
    #if the file doesn't exist, write file to include total budget for each category.
    #AT SOME POINT - have this in a separate file as a function which writes budgets

    budgetfile = open("budgetfile.txt","w")

    budgetdict = {}
    #enter budgets
    
    try:
        catbudget = int(input("Please enter your budget for food: "))
    except ValueError:
        print("Error: Please enter a number")
    budgetfile.write("food " + str(catbudget) + "\n")
    category1 = Budget("food",catbudget)
    budgetdict["food"] = catbudget
    
    try:
        catbudget = int(input("Please enter your budget for clothing: "))
    except ValueError:
        print("Error: Please enter a number")
    budgetfile.write("clothing " + str(catbudget) + "\n")
    category2 = Budget("clothing",catbudget)
    budgetdict["clothing"] = catbudget

    try:
        catbudget = int(input("Please enter your budget for entertainment: "))
    except ValueError:
        print("Error: Please enter a number")
    budgetfile.write("entertainment " + str(catbudget) + "\n")
    category3 = Budget("entertainment",catbudget)
    #budgetdict["entertainment"] = catbudget # is a dictionary even needed here if the object is already created???
    
    #Do you want to add new categories? FEATURE COMING SOON

    budgetfile.close()


else:
    print("A budget file has already been created.")
    budgetfile = open("budgetfile.txt","r")

    budgetdict = {}
    for line in budgetfile:
        category, catbudget = line.split()
        catbudget = int(catbudget)
        #create object
        #catobj = budget(category,catbudget)
        #create dictionary
        
        budgetdict[category] = catbudget

    allcats = list(budgetdict.keys())
    print(allcats)
    #makeobjects
    category1 = Budget("food",budgetdict["food"])
    category2 = Budget("clothing",budgetdict["clothing"])
    category3 = Budget("entertainment",budgetdict["entertainment"])

    budgetfile.close()

#BUDGET FILE NOW CREATED.
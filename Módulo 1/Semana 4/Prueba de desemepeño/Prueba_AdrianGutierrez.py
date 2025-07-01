import time
import os
from pprint import PrettyPrinter
from datetime import datetime

# List of variables used in this code.
inventory = {"Moby Dick" : {"author" : "Adrian", "category" : "Fiction", "price" : 18900, "quantity" : 100},
             "Hunger Games" : {"author" : "Lesly", "category" : "Fiction", "price" : 35000, "quantity" : 50},
             "Romeo And Juliet" : {"author" : "Laura", "category" : "Romance", "price" : 20800, "quantity" : 60},
             "Cristiano Ronaldo" : {"author" : "Israel", "category" : "Biography", "price" : 45000, "quantity" : 45},
             "One Hundred Years Of Solitude" : {"author" : "Alejandro", "category" : "Novel", "price" : 39900, "quantity" : 55}}

sales = [{"bookName" : "Moby Dick", "client" : "Lionel Messi", "author" : "Adrian", "category" : "Fiction", "numOfSales" : 2, "date" : "2025-06-02", "saleValue" : 250000},
         {"bookName" : "Hunger Games", "client" : "Edison Toloza", "author" : "Lesly", "category" : "Fiction", "numOfSales" : 18, "date" : "2024-06-25", "saleValue" : 190000},
         {"bookName" : "Moby Dick", "client" : "Radamel Falcao", "author" : "Adrian", "category" : "Fiction", "numOfSales" : 5, "date" : "2025-06-02", "saleValue" : 250000},
         {"bookName" : "Romeo And Juliet", "client" : "Luis Diaz", "author" : "Laura", "category" : "Romance", "numOfSales" : 10, "date" : "2025-06-08", "saleValue" : 250000},
         {"bookName" : "Cristiano Ronaldo", "client" : "Cristiano Ronaldo", "author" : "Israel", "category" : "Biography", "numOfSales" : 17, "date" : "2025-07-02", "saleValue" : 250000}]

# Wipe the console when user choose an option from a menu.
def wipeConsole():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

# Add products to the inventory.
def addProducts():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        try:
            # User inputs book's name, author's name and category's name.
            bookName = input("Input the book's name/title: ").title().strip()
            author = input("Input the author's name: ").title().strip()
            category = input("Input the category's name: ").title().strip()
            # Condition to raise an error if user inputs an empty space or format the text if not.
            if not bookName or not author or not category:
                raise ValueError
            # User inputs price and quantity of books.
            price = float(input("Input the book's price: "))
            quantity = int(input("Input the quantity of books to add to the inventory: "))
            # Condition to raise an error if user inputs a negative value.
            if price <= 0 or quantity <= 0:
                raise ValueError
            else:
                inventory[bookName] = dict({"author" : author, "category" : category, "price": price, "quantity": quantity})
                print(f"\n{bookName} has been added to the inventory.")
        except ValueError:
            # Printed message when the function sends a raised error.
            print("You must input a valid option. \nYou can't input words or special characters like @, _, #, etc.")
            wipeConsole()
        else:
            # Add another book to the inventory.
            wipeConsole()
            if not askContinue("Do you want to add another product? (y/n) "):
                continueLoop = False
            
# Find products function.
def findProducts():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        # User inputs the book's name to find.
        bookName = input("Input the book's name you want to find: ").title().strip()
        if bookName in inventory:
            # if book is in inventory show the name and the information about it.
            result = (f"{bookName} is in the inventory \nThe info about the book is: {inventory[bookName]} \n")
            print(result)
        else:
            # Show a message to let the user knows that the book is not in the inventory.
            result = (f"{bookName} is not in the inventory. \n")
            print(result)
            wipeConsole()
        # Add another book to the inventory.
        if not askContinue("Do you want to find another product? (y/n) "):
                continueLoop = False
        
# Update prices function.
def updatePrice():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        try:
            # User inputs the book's name to update its price.
            bookName = input("Input the book's name you want to update its price: ").title().strip()
            if bookName in inventory:
                # If the book is in the inventory, we let the user input the new price.
                price = float(input("Input the new price: "))
                if price <= 0:
                    # Raise an error when the user inputs a negative value.
                    raise ValueError
                else:
                    # If the price is bigger than 0, update the price.
                    inventory[bookName].update({"price" : price})
                    result = (f"The {bookName}'s price has been updated")
                    print(result)
            else:
                # Show a message to let the user knows that the book is not in the inventory.
                resultado = (f"{bookName} is not in the inventory")
                print(resultado)
        except ValueError:
            # Printed message when the function sends a raised error.
            print("You must input a valid option. \nYou can't input words or special characters like @, _, #, etc.")
            wipeConsole()
            continueLoop
        else:
            # Realize another operation with a book of the inventory.
            wipeConsole()
            if not askContinue("Do you want to update another product's price? (y/n) "):
                continueLoop = False

# Delete products function
def deleteProducts():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        # User inputs the book's name to update its price.
        bookName = input("Input the book's name you want to update its price: ").title().strip()
        if bookName in inventory:
            # if the book is in the inventory, the system will delete it.
            inventory.pop(bookName)
            result = (f"{bookName} se ha eliminado del inventario")
            print(result)
        else:
            # Show a message to let the user knows that the book is not in the inventory.
            result = (f"{bookName} no se encuentra en el inventario")
            print(result)
        # Realize another operation with a book of the inventory.
        wipeConsole()
        if not askContinue("Do you want to delete another product? (y/n) "):
            continueLoop = False

# Inventory's total value calc function.
def calculateTotalValue():
    # map() goes through the dictionary and the values of each key, the lambda function performs the operation of calculating the total value of each product,
    # and sum performs the sum of the total values of all the products in the dictionary.
    totalValue = sum(map(lambda bookName: bookName["price"] * bookName["quantity"], inventory.values()))
    print(f"The total value of the invetory is: {totalValue:.2f}")
            
# Format the inventory in the console.
def showInventory():
    formatInventory = PrettyPrinter(indent = 4, width = 60, sort_dicts = True)
    formatInventory.pprint(inventory)

# Ask the users if they want to do another operation.
def askContinue(prompt = "Do you want to perform another operation? (y/n) "):
    while True:
        answer = input(prompt).lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        print("Please, input 'y' or 'n'.")

# Function for inventory managment.
def inventoryManagment():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        try:
            print("1. Add products \n2. Search product \n3. Update product's price \n4. Delete products \n5. Inventory's total value \n6. Show inventory \n7. Go back to main menu \n")    
            menuOption = int(input("Choose an option: "))
            match menuOption:
                    case 1:
                        # Add products function.
                        addProducts()
                        wipeConsole()
                    case 2:
                        # Find products function.
                        findProducts()
                        wipeConsole()
                    case 3:
                        # Update product's price function.
                        updatePrice()
                        wipeConsole()
                    case 4:
                        # Delete products function.
                        deleteProducts()
                        wipeConsole()
                    case 5:
                        # Calculate the total value of the inventory function.
                        calculateTotalValue()
                        wipeConsole()
                    case 6:
                        # Display all the inventory.
                        showInventory()
                    case 7:
                        # Back to main menu.
                        wipeConsole()
                        continueLoop = False
                    case _:
                        print("Input a valid option please.")
                        wipeConsole()
                        continueLoop
        except ValueError:
            print("You must input a valid option. \nYou can't input words or special characters like @, _, #, etc.")
            wipeConsole()

# Making sales function.
def salesRegistration():
    continueLoop = True
    while continueLoop:
        try:
            bookName = input("Input the book's name: ").title().strip()
            client = input("Input the client's name: ").title().strip()
            author = input("Input the author's name: ").title().strip()
            category = input("Input the category of the book: ").title().strip()
            if not bookName or not client or not category:
                raise ValueError
            elif bookName in inventory:
                numOfSales = int(input("Quantity of book to be sold: "))
                date = input("Input the date (YYYY-MM-DD): ")
                discount = int(input("Input discount's percentage: "))
                if numOfSales > inventory[bookName]["quantity"]:
                    print("The sale can't be done because there's no stock. \nVerify the book stock in the inventory.")
                else:
                    totalNoDiscount = inventory[bookName]["price"] * numOfSales
                    discountPrice = (totalNoDiscount) * (discount / 100)
                    saleValue = totalNoDiscount - discountPrice
                    sale = dict({"Name" : bookName, "client" : client, "author" : author, "category" : category, "quantity" : int(numOfSales), "date" : date, "Sale Value" : saleValue})
                    sales.append(sale)

                inventory[bookName]["quantity"] -= numOfSales
                print(f"\nThe sale of {bookName} has been done")
                print(f"The {bookName}'s stock is {inventory[bookName]["quantity"]} copys")
            else:
                print("The book is not in the inventory.")
        except:
            print("You must input a valid option. \nYou can't input words or special characters like @, _, #, etc.")
            wipeConsole()
            continueLoop
        else:
            wipeConsole()
            if not askContinue("Do you want to sell another product? (y/n) "):
                continueLoop = False

# Sales main function.
def salesManagment():
    continueLoop = True
    while continueLoop:
        try:
            print("1. Sales Registration \n2. Sales History \n3. Go back to main menu \n")    
            opcionMenu = int(input("Choose an option: "))
            match opcionMenu:
                case 1:
                    salesRegistration()
                    wipeConsole()
                case 2:
                    formatSales = PrettyPrinter(indent=4, width=60, sort_dicts=False)
                    formatSales.pprint(sales)
                    wipeConsole()
                case 3:
                    wipeConsole()
                    continueLoop = False
                case _:
                    print("\nPlease, input a valid option\n")
                    wipeConsole()
                    continueLoop
        except ValueError:
            print("\nYou must input a valid option. \nYou can't input words or special characters like @, _, #, etc.\n")
            wipeConsole()
            continueLoop

# Display best three selling books function.
def bestSellingBooks():
    salesBook = {}

    for sale in sales:
        bookName = sale["bookName"]
        numOfSales = sale["numOfSales"]
        if bookName in salesBook:
            salesBook[bookName] += numOfSales 
        else:
            salesBook[bookName] = numOfSales
    sortedSales = sorted(salesBook.items(), key=lambda item: item[1], reverse=True)
    bestSellers = sortedSales[:3]
    for bookName, numOfSales in bestSellers:
        print(f"{bookName}: {numOfSales} copys")

# Sales by author function.
def authorSales():
    salesByAuthor = {}

    for sale in sales:
        author = sale["author"]
        numOfSales = sale["numOfSales"]
        if author in salesByAuthor:
            salesByAuthor[author] += numOfSales 
        else:
            salesByAuthor[author] = numOfSales
    sortedAuthorSales = sorted(salesByAuthor.items(), key=lambda item: item[1], reverse=True)
    for author, numOfSales in sortedAuthorSales:
        print(f"{author}: {numOfSales} copys")        

# Gross and net incomes function.
def incomes():
    sumSales = 0
    inventoryTotalValue = sum(map(lambda bookName: bookName["price"] * bookName["quantity"], inventory.values()))
    for sale in sales:
        sumSales += sale["saleValue"]
    grossIncome = sumSales
    netIncome = sumSales - inventoryTotalValue
    print(f"The gross incomes are {grossIncome:.2f}")
    print(f"The net incomes are {netIncome:.2f}")
    

# Reports main function.
def reportsManagment():
    continueLoop = True
    while continueLoop:
        try:
            print("1. Best Selling Books \n2. Total sales by author \n3. Net and Gross Income \n4. Go back to main menu \n")    
            opcionMenu = int(input("Choose an option: "))
            match opcionMenu:
                case 1:
                    bestSellingBooks()
                    wipeConsole()
                case 2:
                    authorSales()
                    wipeConsole()
                case 3:
                    incomes()
                    wipeConsole()
                case 4:
                    wipeConsole()
                    continueLoop = False
                case _:
                    print("\nPlease, input a valid option\n")
                    wipeConsole()
                    continueLoop
        except ValueError:
            print("\nYou must input a valid option. \nYou can't input words or special characters like @, _, #, etc.\n")
            wipeConsole()
            continueLoop

# Main function.
def main():
    # Variable used for the loop's condition.
    continueLoop = True
    while continueLoop:
        try:
            #Main menu printed in console.
            print("-"*35)
            print("       Adri's Library - IMS        ")
            print("-"*35)
            print("1. Inventory Management \n2. Make or consult sales \n3. Reports \n4. Exit \n")
            # Choose an option from the main menu.
            menuOption = int(input("Choose an option: "))
            match menuOption:
                case 1:
                    # Inventory managment function.
                    wipeConsole()
                    inventoryManagment()
                case 2:
                    # Sales function.
                    wipeConsole()
                    salesManagment()
                case 3:
                    # Reports function.
                    wipeConsole()
                    reportsManagment()
                case 4:
                    # Exit the program.
                    print("\nCome back soon!\n") 
                    continueLoop = False
                case _:
                    print("Input a valid choice please.")
                    wipeConsole()
                    continueLoop
        except ValueError:
            print("You must input a valid option. \nYou can't input words or special characters like @, _, #, etc.")
            wipeConsole()

if __name__ == "__main__":
    main()

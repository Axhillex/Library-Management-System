import read as r1
import write_borrow as wb
import write_return as wr
import name_check as nc

#function to call other functions from read module to display the text file
def book_list(n):
    r1.print_2d_file(r1.store_file())
    next_menu(n)

#function to input the customer name and call function from write_borrow module
def borrow_func(n):
    quantity=1
    customer_name=input("Name of the customer:")
    wb.lend_book(quantity,customer_name,n)
    next_menu(n)

#function to input the customer name and call function from write_return module   
def return_func(n):
    quantity=1
    customer_name=input("Name of the customer:")
    val_chk=nc.chk_name(customer_name,quantity,n)
    if val_chk==True:
        wr.return_book(customer_name,quantity)
        next_menu(n)
    else:
        return_func(n)

'''function to prompt the user if they want to go back to menu or not to make
    the program run in a loop untill the user says no.''' 
def next_menu(n):
    try:
        z=input("Do you want to go back to menu?(y/n):")
    except:
        print("Incorrect Input!!Try again..")
    else:
        if z=="y":
            display(n)
        else:
            print("Thank you for you service!")

#function to display the details 
def display(name):  
    print("\t\t Welcome "+name+" to the L.M.S of Midnight Library.")
    print("\t[Note: Only three  books per customer can be borrowed.]")
    print("\tWhat would you like to do? (Follow the instruction given below):")
    print("\tEnter 1. To check the list of the books available.")
    print("\tEnter 2. To lend a book to the customer.")
    print("\tEnter 3. To return a book from the customer.")
    print("\tEnter 4. Exit")
    try:
        num=int(input())
    except:
        print("\t\t Please try again!!")
        display(name)
    else:
        if num==1:
            book_list(name)
        elif num==2:
            borrow_func(name)
        elif num==3:
            return_func(name)
        elif num==4:
            print("Thank you for your service!")
        else:
            print("\t\t Please try again!!")
            display(name)
            
#Function for the user to login to the program
def login():
    print("\t\t\t\t\t Welcome to Midnight Library.")
    print("\t\t\t\t\t   Kamalpokhari,Kathmandu")
    print("\t\t\t\t\t  Ph:01-5555555,9807654321")
    try:
        user_name=input("Enter your username in the library:")
    except:
        print("Incorrect Input!!Try again..")
        login()
    else:
        display(user_name)

#The program starts from here  
login()

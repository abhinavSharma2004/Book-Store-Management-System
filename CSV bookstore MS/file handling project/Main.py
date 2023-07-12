from Animations import Animations
import time
import sys
import os
import getpass
from Database import Database

class Main:
    def __init__(self):
        self.clear()
        self.animate = Animations()
        self.animate.dots(4)
        print("Getting you online")
        self.animate.dots(3)
        self.DB = Database()

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    obj=Main()
    print("Starting the Software")
    obj.animate.dots(4)
    obj.clear()
    print("Enter your choice")
    print("1.Login")
    print("2.Register")
    choice = input()    
    obj.clear()
    if(choice=="1"):
        print("Enter User ID:")
        userID = input()
        obj.clear()
        print("Enter Password:")
        password = input()
        obj.clear()
        checked = obj.DB.Login(userID, password)
        if(checked):
            obj.animate.dots(4)
            print("Logging you in please wait")
            obj.animate.dots(8)
            obj.clear()
            selectInput = 0
            while selectInput != "8":
                print("\n------------------WELCOME TO THE BOOK MANAGEMT------------------ \n")
                print("    1. Search Book")
                print("    2. Search Author")
                print("    3. Show Book List")  
                print("    4. Add item")
                print("    5. Delete item")             
                print("    6. Make bill")
                print("    7. Update details")
                print("    8. Exit \n ")
                print("----------------------------------------------------------------\n")
                selectInput = input("Enter your choice:\n")
                obj.clear()
                if(selectInput=="3"):
                    obj.DB.showBookList()
                elif(selectInput=="4"):
                    obj.DB.add_rec()
                elif(selectInput=="1"):
                    obj.DB.search_ID()
                elif(selectInput=="2"):
                    obj.DB.search_author()
                elif(selectInput=="5"):
                    itemd = input("Enter the ID of the item that is to be deleted: ")
                    obj.DB.deletebook(itemd)
                elif(selectInput=="6"):
                    obj.DB.bill()
                elif(selectInput=="7"):
                    ch = 0
                    while (ch != '3'):
                        ch = input("Enter what to update: \n1. Price \n2. Quantity \n3. Exit \n")
                        if (ch == '1'):
                            obj.DB.update_price()
                        elif (ch == '2'):
                            obj.DB.update_quan()
        else:
            print("Access Denied")
    elif(choice=="2"):
        print("Create ID:")
        userName=input()
        print("Create Password")
        userPass = input()
        obj.DB.Register(userName, userPass)
        print ("You have been registered")
        obj.animate.dots(4)
        print ("restart to continue")


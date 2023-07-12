import mysql.connector as sql
from Animations import Animations
import sys
import os
from mysql_bookmanagement import bookdb

class Main:
    def __init__(self):
        self.clear()
        self.animate = Animations()
        self.animate.dots(4)
        print("Getting you online")
        self.animate.dots(3)
        self.DB = bookdb()

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    obj=Main()
    print("Starting the Software")
    obj.animate.dots(4)
    conec = sql.connect(host="localhost",user="root",password="Lalu@2004",database="milkyday")
    if conec.is_connected():
        print("connection certified")
    else:
        print("Connection Failed Try later.......")
    obj.clear()
    print("")
    print("Enter your choice")
    print("1.Login")
    print("2.Register")
    print("3.Remove User")
    choice = input()    
    obj.clear()
    if(choice=="1"):
        log = obj.DB.login()
        if log == True:
            print("")
            print ("      **User confirmed**")
            print("")
            print("Logging you in please wait")
            obj.animate.dots(7)
            selectInput = 0
            while selectInput != "12":
                print("\n------------------WELCOME TO THE BOOK MANAGEMT------------------ \n")
                print("----------------------------MENU-------------------------------- \n")
                print("    1. Search by Book ID")
                print("    2. Search by Author")
                print("    3. Search by Price range")
                print("    4. Show Book List")  
                print("    5. Add item")
                print("    6. Delete by Book")  
                print("    7. Delete by Author")              
                print("    8. Make bill")
                print("    9. Update Book ID")
                print("   10. Update Price")
                print("   11. Update Quantity")
                print("                        Issued Books")
                print("       a. Show issued book list")
                print("       b. Issue books")
                print("       c. Delete issue records")
                print("   12. Exit")
                print("")
                print("----------------------------------------------------------------")
                print("")
                selectInput = input("Enter your choice:\n")
                if(selectInput=="1"):
                    obj.DB.searchbook()
                elif(selectInput=="2"):
                    obj.DB.search_author()
                elif(selectInput=="3"):
                    obj.DB.search_price()
                elif(selectInput=="4"):
                    obj.DB.showtable()
                elif(selectInput=="5"):
                    obj.DB.addtable()
                elif(selectInput=="6"):
                    obj.DB.deletebook()
                elif(selectInput=="7"):
                    obj.DB.deleteauthor()
                elif(selectInput=="8"):
                    obj.DB.makebill()
                elif(selectInput=="9"):
                    obj.DB.updateID()
                elif(selectInput=="10"):
                    obj.DB.updatePri()
                elif(selectInput=="11"):
                    obj.DB.updateQuan()
                elif(selectInput=="a"):
                    obj.DB.showissue()
                elif(selectInput=="b"):
                    obj.DB.issuebook()
                elif(selectInput=="c"):
                    obj.DB.deleteissue()
                elif(selectInput=="12"):
                    obj.animate.dots(4)
                    print("logging you out")
                    obj.animate.dots(3)
                else:
                    print("Choose between 1 to 12 or a,b,c")
                    break
        else:
            print("")
            print("      **Access Denied**")
    
    elif(choice=="2"):
        access = input("Enter the Admin Password to create a new Account: ")
        if access == "1111":
            obj.DB.register()
            print("")
            print ("restart to continue")
        else:
            print("")
            print("**Not Authorised for such actions**")
    
    elif(choice=="3"):
        obj.DB.deleteuser()










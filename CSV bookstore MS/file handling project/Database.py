
from Animations import Animations
import csv
import pickle

class Database:
    global animate
    global ID_list
    global price_list
    global author_list  
     

    def bill(self):
        with open("bookexampl.csv", 'r') as file:
            csv_reader = csv.reader(file)
            ID_list = list()
            price_list = list()
            for row in csv_reader:
                ID_list.append(row[0])
                price_list.append(row[3]) 
            quan = int(input("Enter the number of unique books to be bought: "))
            sum=0
            list_length = len(ID_list)
            for i in range (1,quan+1):
                name = input("Enter the ID of book: ") 
                quan2 = int(input("Enter quantity: "))
                for j in range (0,list_length):
                    if name == ID_list[j] :
                        rate = int(price_list[j])
                        price1 = rate*quan2
                        sum += price1
                        print("Price for ", i ," is", price1)
            print("Total bill is ",sum)
    

    def search_ID(self):
        with open("bookexampl.csv", 'r') as file:
            csv_reader = csv.reader(file)
            ID_input = input("Enter ID of the book: ")
            for row in csv_reader:
                if (ID_input == row[0]) :
                    print("[ID,Author,Title,Price,Quantity]")
                    print (row)
                    linput = input("\nPress 'c' to continue.\n")
                    if (linput == 'c'):
                        break


    def search_author(self):
        with open("bookexampl.csv", 'r') as file:
            csv_reader = csv.reader(file)
            author_books = list()
            author_input = input("Enter Author's full name: ")
            for row in csv_reader:
                if (author_input == row[2]):
                    author_books.append(row[1])
            lang = len(author_books)
            if (lang >= 1):
                print ("All available books by the author are: ")
                print (author_books)
                rinput = input("\nEnter 'c' to continue.\n")
            else:
                print ("Author's books are not available")
                linput = input("\nEnter 'c' to continue.\n")
            

    def append_File(self,filename, listItem):
        with open(filename , 'a+' , newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(listItem)


    def showBookList(self):
        with open("bookexampl.csv") as  file:
            csv_reader = csv.reader(file)
            print("ID             Author                                               Title                                          Price        Quantity")
            for row in csv_reader:
                bookID = "{:<15}".format(row[0])
                bookTitle = "{:<50}".format(row[1])
                bookAuthor = "{:<50}".format(row[2])
                bookPrice = "{:<12}".format(row[3])
                bookQuantity = row[4]
                result = bookID + bookAuthor + bookTitle + bookPrice + bookQuantity
                print(result)


    def deletebook(self, bookID):
        tempFile = list()
        with open("bookexampl.csv") as file:
            bookreader = csv.reader(file)
            for row in bookreader:
                if(row[0] != bookID):
                    tempFile.append(row)
        with open("bookexampl.csv" ,"w",newline="") as wfile:
            writer = csv.writer(wfile)
            writer.writerows(tempFile)
            print ("\n**Item has been deleted**")


    def Login(self,userID, Password):
        with open("Users.csv") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if(row[0] == userID and row[1] == Password):
                    return True
            return False   


    def Register(self, name, password):
        dummy =  [name, password]
        self.append_File("Users.csv", dummy)
        return True


    def add_rec(self):
        tempFile = list()
        with open("bookexampl.csv" ,"r") as rfile:
            rec_input = int(input ("Enter number of records to be saved: "))
            bookreader = csv.reader(rfile)
            for row in bookreader:
                tempFile.append(row)
            rec = list()
            for i in range (1,rec_input+1):
                ID_input = input("Enter ID: ")
                title_input = input("Enter Title name: ")
                author_input = input("Enter Author: ")
                price_input = input("Enter Price: ")
                quantity_input = input("Enter Quantity: ")
                new_rec = [ID_input,title_input,author_input,price_input,quantity_input]
                tempFile.append(new_rec) 
            with open("bookexampl.csv" ,"w",newline="") as wfile:
                writer = csv.writer(wfile)
                writer.writerows(tempFile)  
                print ("**Record saved**")
    

    def update_price(self):
        with open("bookexampl.csv" ,"r") as rfile:
            tempfile = list()
            bookreader = csv.reader(rfile)
            upd_input = (input ("Enter ID of the item to be updated: "))
            for row in bookreader:
                if (upd_input == row[0]):
                    change = input("Enter the new price: ")
                    row[3] = change
                tempfile.append(row)
            with open("bookexampl.csv" ,"w",newline="") as wfile:
                writer = csv.writer(wfile)
                writer.writerows(tempfile)
                print ("\n**Price has been successfully updated**\n")
               
        
    def update_quan (self):
        with open("bookexampl.csv" ,"r") as rfile:
            tempfile1 = list()
            bookreader = csv.reader(rfile)
            upd_input1 = (input ("Enter ID of the item to be updated: "))
            for row in bookreader:
                if (upd_input1 == row[0]):
                    change1 = input("Enter the new Quantity: ")
                    row[4] = change1
                tempfile1.append(row)
            with open("bookexampl.csv" ,"w",newline="") as wfile1:
                writer1 = csv.writer(wfile1)
                writer1.writerows(tempfile1)
                print ("\n**Quantity has been successfully updated**\n\n")


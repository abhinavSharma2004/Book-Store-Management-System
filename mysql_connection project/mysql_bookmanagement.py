import mysql.connector as sql
from Animations import Animations as animate


class bookdb:
    conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
    if conec.is_connected():
        print("connection certified")
      

    def showtable(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        print("showing data in the system")
        animate.dots(self,5)
        cur.execute("select * from books")
        show=cur.fetchall()


        print ("+" ,"-"*120,"+")
        print ("| Book ID          ","| Book Name                              ","| Author                    ","| Quantity     ","| Price         |")
        for row in show:
            bookID = "{:<16}".format(row[0])
            bookName = "{:<38}".format(row[1])
            bookAuthor = "{:<25}".format(row[2])
            bookPrice = "{:<12}".format(row[3])   
            bookQuantity = row[4]
            bookID = str(bookID)
            bookPrice = str(bookPrice)
            bookQuantity = str(bookQuantity)
            print ("|" ,"-"*17, "+","-"*39,"+","-"*26,"+","-"*13,"+","-"*13,"|")
            print ("|",bookID,' '*(15-len(bookID)) , "|",bookName,' '*(37-len(bookName)) , "|",bookAuthor,' '*(24-len(bookAuthor)) , "|",bookPrice,' '*(11-len(bookPrice)) , '|',bookQuantity, ' '*(12-len(bookQuantity)),"|")
        print ("+" ,"-"*120,"+")
        go = input("PRESS ENTER TO GO BACK")
     
    def addtable(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            ID_input = int(input("Enter ID: "))
            title_input = input("Enter Title name: ")
            author_input = input("Enter Author: ")
            price_input = int(input("Enter Price: "))
            quantity_input = int(input("Enter Quantity: "))
            rec = [ID_input,title_input,author_input,price_input,quantity_input]
            query = "INSERT INTO books VALUES (%s,%s,%s,%s,%s)"
            cur.execute(query,rec)
            conec.commit()
            print ("")
            print("     **New data added**")
            print ("")
            print("Add more? (y/n) ")
            reply = (input())

    def searchbook(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = input("Enter the BookID you need to find: ")
            cur.execute("select * from books where BookID = '%s'" %(cond))
            show=cur.fetchall()
        
            print ("+" ,"-"*120,"+")
            print ("| Book ID          ","| Book Name                              ","| Author                    ","| Quantity     ","| Price         |")
            for row in show:
                bookID = "{:<16}".format(row[0])
                bookName = "{:<38}".format(row[1])
                bookAuthor = "{:<25}".format(row[2])
                bookPrice = "{:<12}".format(row[3])   
                bookQuantity = row[4]
                bookID = str(bookID)
                bookPrice = str(bookPrice)
                bookQuantity = str(bookQuantity)
                print ("|" ,"-"*17, "+","-"*39,"+","-"*26,"+","-"*13,"+","-"*13,"|")
                print ("|",bookID,' '*(15-len(bookID)) , "|",bookName,' '*(37-len(bookName)) , "|",bookAuthor,' '*(24-len(bookAuthor)) , "|",bookPrice,' '*(11-len(bookPrice)) , '|',bookQuantity, ' '*(12-len(bookQuantity)),"|")
                print ("+" ,"-"*120,"+")
            print("Search more? (y/n) ")
            reply = (input())

    def search_author(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = input("Enter the Author you need to find: ")
            cur.execute("select * from books where Author = '%s'" %(cond))
            show=cur.fetchall()
            
            print ("+" ,"-"*120,"+")
            print ("| Book ID          ","| Book Name                              ","| Author                    ","| Quantity     ","| Price         |")
            for row in show:
                bookID = "{:<16}".format(row[0])
                bookName = "{:<38}".format(row[1])
                bookAuthor = "{:<25}".format(row[2])
                bookPrice = "{:<12}".format(row[3])   
                bookQuantity = row[4]
                bookID = str(bookID)
                bookPrice = str(bookPrice)
                bookQuantity = str(bookQuantity)
                print ("|" ,"-"*17, "+","-"*39,"+","-"*26,"+","-"*13,"+","-"*13,"|")
                print ("|",bookID,' '*(15-len(bookID)) , "|",bookName,' '*(37-len(bookName)) , "|",bookAuthor,' '*(24-len(bookAuthor)) , "|",bookPrice,' '*(11-len(bookPrice)) , '|',bookQuantity, ' '*(12-len(bookQuantity)),"|")
            print ("+" ,"-"*120,"+")
            print("search more? (y/n) ")
            reply = (input())

    def search_price(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = input("Enter the mininum price: ")
            cond1 = input("Enter the maximum price: ")
            inp = [cond,cond1]
            query ="select * from books where Price between %s and %s"
            cur.execute(query,inp)
            show=cur.fetchall()
            print ("+" ,"-"*120,"+")
            print ("| Book ID          ","| Book Name                              ","| Author                    ","| Quantity     ","| Price         |")
            for row in show:
                bookID = "{:<16}".format(row[0])
                bookName = "{:<38}".format(row[1])
                bookAuthor = "{:<25}".format(row[2])
                bookPrice = "{:<12}".format(row[3])   
                bookQuantity = row[4]
                bookID = str(bookID)
                bookPrice = str(bookPrice)
                bookQuantity = str(bookQuantity)
                print ("|" ,"-"*17, "+","-"*39,"+","-"*26,"+","-"*13,"+","-"*13,"|")
                print ("|",bookID,' '*(15-len(bookID)) , "|",bookName,' '*(37-len(bookName)) , "|",bookAuthor,' '*(24-len(bookAuthor)) , "|",bookPrice,' '*(11-len(bookPrice)) , '|',bookQuantity, ' '*(12-len(bookQuantity)),"|")
            print ("+" ,"-"*120,"+")
            print("search more? (y/n) ")
            reply = (input())

    def deletebook(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = int(input("Enter the BookID you need to delete: "))
            cur.execute("DELETE FROM books WHERE BookID = '%s'" %(cond))
            conec.commit()
            print("")
            print("     **Author deleted successfully**")
            print("")
            print("Delete more records? (y/n) ")
            reply = (input())

    def deleteauthor(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = (input("Enter the Author whose books you want to delete: "))
            cur.execute("DELETE FROM books WHERE Author = '%s'" %(cond))
            conec.commit()
            print("")
            print("     **Author deleted successfully**")
            print("")
            print("Delete more records? (y/n) ")
            reply = (input())
    
    def makebill(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        bill = 0
        reply = "y"
        while reply == "y":
            cond = int(input("Enter the BookID : "))
            quan = int(input("Enter the number of books to be bought: "))
            cur.execute("select Quantity from books where BookID = '%s'" %(cond))
            change = cur.fetchone()
            for j in change:
                change2 = int(j)
            change2 = change2-quan
            print (change2)
            cond1 = [change2,cond]
            query = "update books set Quantity = '%s' where BookID = '%s'"
            cur.execute(query,cond1)
            conec.commit()
            cur.execute("select Price from books where BookID = '%s'" %(cond))
            show = cur.fetchone()
            for i in show:
                pri = int(i)
            amount = pri*quan
            bill += amount
            print ("Amount is ",amount)
            print("add more items to the bill? (y/n) ")
            reply = (input())
        print ("The Total bill is ",bill)
        go = input("PRESS ENTER TO GO BACK")

    def login(self):
        user = input("Enter Username: ")
        password = input("Enter Password: ")
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        cur.execute("select Password from admin where Username = '%s'" %(user))
        show = cur.fetchone()
        if show is not None:
            for i in show:
                if i == password:
                    return True  

    def register(self):
        reply = "y"
        while reply == "y":
            print("Create ID:")
            userName=input()
            print("Create Password")
            userPass = input()
            conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
            cur=conec.cursor()
            inp = [userName,userPass]
            query = "insert into admin values(%s,%s)"
            cur.execute(query,inp)
            conec.commit()
            animate.dots(self,4)
            print ("     **You have been added to the system**")
            print("Add more Users? (y/n) ")
            reply = (input())

    def deleteuser(self):
        access = input("Enter Admin password: ")
        print("")
        if access == "1111" : 
            reply = "y"
            while reply == "y":
                cond = (input("Enter the Username : "))
                print("")
                conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
                cur = conec.cursor()
                cur.execute("DELETE FROM admin WHERE Username = '%s'" %(cond))
                conec.commit()
                print ("     ***USER REMOVED*** ")
                print("")
                print("Delete more Users? (y/n) ")
                conec.commit()
                reply = (input())
        else:
            print("")
            print("**Not Authorised for such actions**")
        
    def updatePri(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = int(input("Enter the BookID you want to updated: "))
            cond1 = int(input("Set Price to: "))
            condition = [cond1,cond]
            query = "update books set Price = '%s' where BookID = '%s'"
            cur.execute(query,condition)
            conec.commit()
            print("")
            print("     **Price updated successfully**")
            print("")
            print("Update more Prices? (y/n) ")
            reply = (input())

    def updateQuan(self):
            conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
            cur=conec.cursor()
            reply = "y"
            while reply == "y":
                cond = int(input("Enter the Book ID of book you want to update: "))
                cond1 = int(input("Set Quantity to: "))
                condition = [cond1,cond]
                query = "update books set Quantity = '%s' where BookID = '%s'"
                cur.execute(query,condition)
                conec.commit()
                print("")
                print("     **Quantity updated successfully**")
                print("")
                print("Update more Quantities? (y/n) ")
                reply = (input())
        
    def updateID(self):
            conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
            cur=conec.cursor()
            reply = "y"
            count = 0
            result = False
            while reply == "y":
                cur.execute("select BookID from books")
                show = cur.fetchall()
                print ("Already entered IDs:")
                for i in show:
                    i = str(i)
                    print (i)
                cond = int(input("Enter the Book ID you want to update: "))
                cond1 = int(input("Change ID to: "))
                condition = [cond1,cond]
                query = "update books set BookID = %s where BookID = %s"
                cur.execute(query,condition)
                conec.commit()
                print("")
                print("     **ID updated successfully**")
                print("")
                print("Update more IDs? (y/n) ")
                reply = (input())

    def showissue(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        print("showing data in the system")
        animate.dots(self,5)
        cur.execute("select * from issue")
        show=cur.fetchall()

        print ("+" ,"-"*101,"+")
        print ("| Member ID    ","| Name                            ","| Date of Issue   ","| Date of Return  ","| Book ID      |")
        for row in show:
            memberID = row[0]
            Name = row[1]
            doi = row[2]
            dor = row[3]   
            bookID = row[4]
            bookID = str(bookID)
            memberID = str(memberID)
            print ("|" ,"-"*13, "+","-"*32,"+","-"*16,"+","-"*16,"+","-"*12,"|")
            print ("|",memberID,' '*(12-len(memberID)) , "|",Name,' '*(31-len(Name)) , "|",doi,' '*5, "|",dor,' '*5, '|',bookID, ' '*(11-len(bookID)),"|")
        print ("+","-"*101,"+")
        go = input("PRESS ENTER TO GO BACK ")
    
    def deleteissue(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            cond = int(input("Enter the Memeber ID of issued book: "))
            cur.execute("DELETE FROM issue WHERE MemberID = '%s'" %(cond))
            conec.commit()
            print("")
            print("     ** BOOK ISSUE RECORD DELETED**")
            cur.execute("select Quantity from books B , issue I where B.BookID=I.BookID and MemberID = '%s'" %(cond))
            change = cur.fetchone()
            for j in change:
                change2 = int(j)
            change2 = change2+1
            cond1 = [change2,cond]
            print (change2)
            query = "update books set Quantity = '%s' where BookID = '%s'"
            cur.execute(query,cond1)
            conec.commit()
            print("")
            print("Delete more records? (y/n) ")
            reply = (input())

    def issuebook(self):
        conec = sql.connect(host="localhost",user="root",password="",database="bookstore")
        cur=conec.cursor()
        reply = "y"
        while reply == "y":
            ID_input = int(input("Enter Member ID: "))
            title_input = input("Enter member's Name: ")
            author_input = input("Enter Date of issue (YYYY-MM-DD) : ")
            price_input =  input("Enter Date of return (YYYY-MM-DD) : ")
            quantity_input = int(input("Enter Book ID: "))
            rec = [ID_input,title_input,author_input,price_input,quantity_input]
            query = "INSERT INTO issue VALUES (%s,%s,%s,%s,%s)"
            cur.execute(query,rec)
            conec.commit()
            cur.execute("select Quantity from books where BookID = '%s'" %(quantity_input))
            change = cur.fetchone()
            for j in change:
                change2 = int(j)
            change2 = change2-1
            cond1 = [change2,quantity_input]
            query = "update books set Quantity = '%s' where BookID = '%s'"
            cur.execute(query,cond1)
            conec.commit()
            print ("")
            print("     **BOOK ISSUED**")
            print ("")
            print("Issue more? (y/n) ")
            reply = (input())

        
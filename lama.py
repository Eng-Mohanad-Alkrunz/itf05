#!/usr/bin/env python
# coding: utf-8

# # lama
# 
# Use the "Run" button to execute the code.

# In[5]:


def Menu():
    print("Library Management System")
    print("=" * 30)
    print('''    1.Print books info
    2. Search a book
    3. Add new book
    4. Remove a book
    5. Borrow a book
    6. Return a book
    7. Exit
    ''')
    print("=" * 30)
    choice = input("Enter your choice: ")
    return choice


def LoadBooksData():
    file = open("booksinfo.txt", "r")
    lines = file.read().strip().split("\n")
    books = []
    for line in lines:
        m_book = {}
        if len(line) != 0:
            book_details = line.split(",")
            if len(book_details) != 0:
                m_book['serial_number'] = book_details[0]
                m_book['title'] = book_details[1]
                m_book['author'] = book_details[2]
                m_book['price'] = book_details[3]
                m_book['copies'] = book_details[4]
                try:
                    m_book['borrowed'] = book_details[5]
                except:
                    m_book['borrowed'] = 0
                try:
                    m_book['returned'] = book_details[6]
                except:
                    m_book['returned'] = 0
                books.append(m_book)
    return books


def PrintBooksInfo():
    books = LoadBooksData()
    for book in books:
        print("S.No:", book.get('serial_number'))
        print("Title:", book.get('title'))
        print("Number of authors:", len(book.get('author').split('-')))
        print("Price:", book.get('price'))
        print("Total number of copies:", int(book.get('copies')) + int(book.get('borrowed')))
        print("*****************------------**********")
    return


def SearchBook(search):
    books = LoadBooksData()
    for book in books:
        if search.lower() in book.get('title').lower() :
            print("S.No:", book.get('serial_number'))
            print("Title:", book.get('title'))
            print("Number of authors:", len(book.get('author')))
            print("Price:", book.get('price'))
            print("Total number of copies:", int(book.get('copies')) + int(book.get('borrowed')))
            print("*****************------------**********")
        else:
            for author in book.get('author').split("-"):
                if search.lower() in author.lower():
                    print("S.No:", book.get('serial_number'))
                    print("Title:", book.get('title'))
                    print("Number of authors:", len(book.get('author')))
                    print("Price:", book.get('price'))
                    print("Total number of copies:", int(book.get('copies')) + int(book.get('borrowed')))
                    print("*****************------------**********")
    return


def GetSerialNumber(Serial):
    books = LoadBooksData()
    for book in books:
        if book.get('serial_number') == str(Serial):
            return False
    return True


def AddNewBook(NewBook):
    print(NewBook)
    data = "\n"
    file = open("booksinfo.txt", "a+")
    for i in range(len(NewBook)):
        data += NewBook[i] + ","
    data = data[0:-1]
    data += "\n"
    file.write(data)
    file.close()
    return NewBook[1] + " has been added Successfully"


def DisplayBook(SerialNumber):
    books = LoadBooksData()
    for book in books:
        if book['serial_number'].lower() == SerialNumber.lower():
            print("S.No:", book['serial_number'])
            print("Title:", book['title'])
            print("Author:", book.get('author'))
            print("Price:", book.get('price'))
            print("Total number of copies:", int(book['copies']) + int(book['borrowed']))
            print()
    return


def RemoveBook(SerialNumber):
    file = open("booksinfo.txt", "r")
    context = file.read().strip().split("\n")
    file.close()
    books = []
    for each in context:
        m_book = {}
        if len(each) != 0:
            book_details = each.split(",")
            if len(book_details) != 0:
                m_book['serial_number'] = book_details[0]
                m_book['title'] = book_details[1]
                m_book['author'] = book_details[2]
                m_book['price'] = book_details[3]
                m_book['copies'] = book_details[4]
                m_book['borrowed'] = book_details[5]
                m_book['returned'] = book_details[6]
                books.append(m_book)
    new_data = "\n"
    for book in books:
        if str(book.get('serial_number')) == str(SerialNumber):
            continue
        new_data += book['serial_number'] + "," + book['title'] + "," + \
                    book['author'] + "," + book['price'] + "," + book['copies'] \
                    + "," + book['borrowed'] + "," + book['returned'] + \
                    "\n"
    file = open('booksinfo.txt', 'w')
    file.write(new_data)
    file.close()


def update_book(serial, m_type):
    file = open("booksinfo.txt", "r")
    context = file.read().strip().split("\n")
    file.close()
    books = []
    books_data = ""
    for each in context:
        m_book = {}
        if len(each) != 0:
            book_details = each.split(",")
            if len(book_details) != 0:
                m_book['serial_number'] = book_details[0]
                m_book['title'] = book_details[1]
                m_book['author'] = book_details[2]
                m_book['price'] = book_details[3]
                m_book['copies'] = int(book_details[4])
                m_book['borrowed'] = int(book_details[5])
                m_book['returned'] = int(book_details[6])
                if book_details[0] == str(serial):
                    if m_type == "borrow":
                        m_book['copies'] = int(book_details[4]) - 1
                        m_book['borrowed'] = int(book_details[5]) + 1
                    else:
                        m_book['copies'] = int(book_details[4]) + 1
                        m_book['borrowed'] = int(book_details[5]) - 1
                        m_book['returned'] = int(book_details[6]) + 1
            books_data += m_book['serial_number'] + "," + m_book['title'] + "," + \
                          m_book['author'] + "," + m_book['price'] + "," + str(m_book['copies']) \
                          + "," + str(m_book['borrowed']) +  "," + str(m_book['returned']) +"\n"
            books.append(m_book)
    file = open('booksinfo.txt', 'w')
    file.write(books_data)
    file.close()
    return books


def BorrowBook(UID, SerialNumber):
    file = open("borrowedinfo.txt", "r+")
    context = file.read().strip().split("\n")
    file.close()
    total_borrow = 0
    for record in context:
        record = record.split(",")
        if UID in record and SerialNumber in record:
            return "You cannot borrow the same book again"
        if UID in record:
            total_borrow += 1
    if total_borrow >= 3:
        return "You cannot borrow more then 3 books"

    if checkAvailableBooks(SerialNumber):
        file.writelines([SerialNumber + "," + UID + "\n"])
        update_book(serial=SerialNumber, m_type = "borrow")
        return "Book has been borrowed successfully"
    else:
        return "Book is not borrowed successfully"


def checkAvailableBooks(SerialNumber):
    books = LoadBooksData()
    for book in books:
        if book.get('serial_number') == str(SerialNumber):
            return True
    return False

choice = ""


def update_borrowed(serial, user):
    file = open("borrowedinfo.txt", "r")
    context = file.read().strip().split("\n")
    file.close()
    new_data = ""
    for record in context:
        record = record.split(",")
        if user == record[1] and SerialNumber == record[0]:
            continue
        new_data += record[0] + ","+ record[1] +"\n"
    file = open("borrowedinfo.txt", "w")
    file.write(new_data)
    file.close()



while choice != "7":
    choice = Menu()
    if choice == "1":
        PrintBooksInfo()
    elif choice == "2":
        search = input("Enter Title or Author Name: ")
        SearchBook(search)
    elif choice == "3":
        SerialNumber = input("Enter a 5 digit S.No: ")
        Title = input("Enter the title of book: ")
        author = input("Enter authors name (Separate multiple names using comma)").split(",")
        while True:
            try:
                price = float(input("Enter the price: "))
                break
            except:
                print("Invalid Price format, it should be in float value")
        while True:
            try:
                Copies = int(input("Enter number of copies"))
                break
            except:
                print("Enter only integer value")

        if len(SerialNumber) != 5 and GetSerialNumber(SerialNumber):
            print("Invalid Serial Number")
        if len(Title) < 1:
            print("Invalid Title")
        if len(author) < 1:
            print("Enter atleast one author name")
        if Copies < 1:
            print("Atleast one copy should be added")
        else:
            NewBook = [SerialNumber, Title, ':'.join(author), str(price), str(Copies), "0","0"]
            message = AddNewBook(NewBook)
            print(message)
    elif choice == "4":
        SerialNumber = input("Enter an valid Serial Number: ")
        if len(SerialNumber) != 5 and not GetSerialNumber(SerialNumber):
            DisplayBook(SerialNumber)
        while (True):
            remove = input("Are you Sure you want to remove: Y/N")
            if remove == "Y" or remove == "N":
                break
        if remove == "Y":
            RemoveBook(SerialNumber)
        else:
            print("Such Book does not exist in system")
    elif choice == "5":
        SerialNumber = input("Enter the Serial Number: ")
        if not GetSerialNumber(SerialNumber):
            UID = input("Enter your User ID: ")
            print(BorrowBook(UID, SerialNumber))
        else:
            print("There is no such book in out records")
    elif choice == "6":
        SerialNumber = input("Enter Serial Number : ")
        UID = input("Enter your User ID")
        file = open("borrowedinfo.txt", "r")
        context = file.read().strip().split("\n")
        file.close()
        is_exist = False
        for record in context:
            record = record.split(",")
            if UID in record and SerialNumber in record:
                is_exist = True
                break
        if is_exist:
            update_book(serial=SerialNumber,m_type="return")
            update_borrowed(serial = SerialNumber,user=UID)
            print("Book Returned Successfully")
        else:
            print("You have not borrowed such an book")
    elif choice == "7":
        break
    else:
        print("Invalid Menu Option")

# In[ ]:

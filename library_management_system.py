print("="*25)
print("LIBRARY_MANAGEMENT_SYSTEM")
print("="*25)
books=[]
while True:
    print("\n1. add book:")
    print("2.view book:")
    print("3.search book:")
    print("4.issue book:")
    print("5.return book:")
    print("6.delete book:")
    print("7.exit:")

    choice=input("enter choice:")
    if choice=="1":
        book_id=int(input("enter book id:"))
        book_name=input("enter book name:")
        book_author=input("enter author of the book:")
        book_status="available"
        book={
            "id":book_id,
            "name":book_name,
            "author":book_author,
            "status":book_status
        }
        books.append(book)
        print("book added successfully!")
    elif choice=="2":
        if len(books)==0:
            print("no books available")
        else:
            for book in books:
                print("---------------")
                print("Book ID:",book["id"])
                print("Book Name:",book["name"])
                print("Author:",book["author"])
                print("status:",book["status"])
    elif choice=="3":
        search =input("enter book name to search:")
        found=False
        for book in books:
            if book["name"]==search:
                found=True
                print("Book name:",book["name"])
                print("Book id:",book["id"])
                print("author:",book["author"])
                print("status:",book["status"])
        if found==False:
            print("book not found")
    elif choice=="4":
        search=input("enter book name to issue:")
        found=False
        for book in books:
            if book["name"]==search:
                found=True
                print("status:",book["status"])
                if book["status"]=="issued":
                    print("book is already issued")
                else:
                    book["status"]="issued"
                    print("book issued successfully!")
        if found==False:
                print("book not found")
    elif choice=="5":
        search=input("enter book name to return:")
        found=False
        for book in books:
            if book["name"]==search:
                found=True
                print("status:",book["status"])
                if book["status"]=="available":
                    print("book is already available")
                else:
                    book["status"]="available"
                    print("book returned successfully!")
        if found==False:
            print("book not found")
    elif choice=="6":
        search=input("enter book name to delete:")
        found=False
        for book in books:
            if book["name"]==search:
                found=True
                books.remove(book)
                print("book deleted successfully")
        if found==False:
            print("Book not found")
    elif choice=="7":
        print("thank u for using Library Management System.")
        break
    else:
        print("Invalid choice please enter 1 to 7.")






        




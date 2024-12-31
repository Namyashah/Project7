class JournalManager:
    def setting(self):
        print("Enter your Journal entry:")
        self.file = open("journal.txt","a")
        self.a = int(input("Enter the range = "))
        for i in range(1,self.a):
            self.file.write(input(""))
            print()
        print("Entry Added Successfully!")
        self.file.close()
    def setting2(self):
        pass
    def setting3(self):
        self.keyword = input("Enter a keyword or date to search = ")
        self.file = open("journal.txt","r")
        number = 1
        lst = []
        
        for i in self.file:
            if i in self.file :
                lst.append(number)
            number += 1
            
        if lst :
            print(f"Matching Entries:")
            print("-----------------------------")
            print(self.keyword)
        else :
            print(f"No entries were found for the keyword: {self.keyword}")
    def setting4(self):
        self.num = input("Are you sure you want to delete all entries? (yes/no) = ")
        if self.num=="yes":
            import os
            self.fol = imput("Enter the file you want to delete = ")
            if self.fol=="journal.txt":
                os.remove("journal.txt")
                print("All journal entries have been deleted.")
            else :
                raise FileNotFoundError("No Journal Entries to delete!!")
        else :
            self.num=="no"
            print("Sure")

print("Welcome to Personal Journal Manager!")
while True :
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    
    choice = int(input("Enter your chocie = "))
    if choice==1 :
        j1 = JournalManager()
        j1.setting()
    elif choice==2 :
        pass
    elif choice==3 :
        j3 = JournalManager()
        j3.setting3()
    elif choice==4 :
        j2 = JournalManager()
        try:
            j2.setting4()
        except FileNotFoundError as e:
            print(f"Not Possible Because of {e}")
        except:
            print("General Exception Block!!")
    elif choice==5 :
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    else :
        print("Invalid option. Please select a valid option from the menu.")
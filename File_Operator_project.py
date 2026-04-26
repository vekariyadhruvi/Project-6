import os
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.file="journal.txt"

    def add(self):
        entry=input("Enter your new journal entry: \n")
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file,"a") as f:
            f.write(f"[{time}]\n{entry}\n")
            
        print("\nEntry added successfully!")

    def view(self):
        try:
            with open(self.file,"r") as f:
                data=f.read()

                if data.strip()=="":
                    print("\nNo journal entries found.")
                else:
                    print("\nYour Journal Entries:\n")
                    print(data)

        except FileNotFoundError:
            print("\nNo journal entries found.")

    def search(self):
        key=input("\nEnter a keyword or date to search: ")

        try:
            with open(self.file, "r") as f:
                entries=f.read().split("\n[")

            found=False
            print("\nMatching Entries:\n")

            for e in entries:
                if key.lower() in e.lower():
                    if not e.startswith("["):
                        e="[" + e
                    print(e.strip())
                    print()
                    found=True

            if not found:
                print(f"No entries were found.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")

    def delete(self):
        confirm=input("\nAre you sure you want to delete all entries? (yes/no): ")

        if confirm.lower()=="yes":
            try:
                os.remove(self.file)
                print("\nAll journal entries have been deleted.")
            except FileNotFoundError:
                print("\nNo journal entries to delete.")
        else:
            print("\nDeletion cancelled.")

jm=JournalManager()
print("\nWelcome to Personal Journal Manager!")

while True:
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice=int(input("User Input: "))

    if choice==1:
        jm.add()
    elif choice==2:
        jm.view()
    elif choice==3:
        jm.search()
    elif choice==4:
        jm.delete()
    elif choice==5:
        print("Exiting the program!")
        break
    else:
        print("\nInvalid choice. Please choose again.")
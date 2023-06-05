from Database import Database
from OTP import OTP
from Entry import Entry

class Authenticator:

    def __init__(self):
        self.headline()
        self.run_app = True
        self.DB = Database()
        self.otp = OTP()

    """The greeting headline"""
    def headline(self):
        print("Welcome to Python Terminal Authenticator\n")

    """The menu options"""
    def show_menu(self):
        print("\nEnd Program (0)")
        print("Show All Entries (1)")
        print("Show Auth-Code (2)")
        print("Add Entry (3)")
        print("Delete Entry (4)")
        print("Edit Entry (5)")

    """Lists all entries available"""
    def get_all_entries(self):
        all_entries = self.DB.get_entries()
        self.print_all(all_entries)

    """Prints all entries"""
    def print_all(self, all_entries):
        print("ID | Website | Account")
        for entry in all_entries:
            for info in entry:
                print(f"{info}", end=" ")
            print()

    """Adds a new entry"""
    def add_entry(self):
        repeat = True
        print("Type the new entry:\n")
        while repeat:
            website = input("Website: ")
            account = input("Account: ")
            b32s = input("Base32Secret: ")
            correct = input("\nIs this correct? (y) Yes , (n) No , (x) End : ")
            if correct == "y":
                repeat = False
                print("End Entry\n")
                return [website, account, b32s]
            if correct == "n":
                repeat = True
            if correct == "x":
                repeat = False
                print("")
                self.application()

    """Asks User for Entry ID"""
    def get_entry_id(self):
        e_id = input("\nSelect ID: ")
        return int(e_id)

    """Deletes an entry"""
    def del_entry(self):
        repeat = True
        e_id = input("\nSelect the ID of entry to delete: ")
        check_ex = self.check_entry_existence(e_id)
        if not check_ex:
            print("The ID is not available")
        else:
            while repeat:
                correct = input("\nIs this correct? (y) Yes , (n) No , (x) End : ")
                if correct == "y":
                    repeat = False
                    self.DB.del_entry(int(e_id))
                    print("Deleted Entry\n")
                if correct == "n":
                    repeat = True
                if correct == "x":
                    repeat = False
                    print("")
                    self.application()

    """Editing an Entry"""
    def edit_entry(self):
        e_id = self.get_entry_id()
        check_ex = self.check_entry_existence(e_id)
        if not check_ex:
            print("The ID is not available")
        else:
            Entry(e_id)

    """Checks if an entry exists in table"""
    def check_entry_existence(self, id):
        return self.DB.get_entry(id)

    """Generates and prints a new OTP"""
    def getAuthCode(self):
        try:
            e_id = self.get_entry_id()
            b32s = self.DB.get_b32s(e_id)
            print("Current TOTP: " + self.otp.get_TOTP(b32s) + "\n")
        except:
            return

    """Handles the user input """
    def handle_input(self):
        self.decision = input("Input: ")
        match int(self.decision):
            case 0:
                self.run_app = False
                print("\nEnding Program\n")
            case 1:
                print("")
                self.get_all_entries()
                print("")
            case 2:
                self.getAuthCode()
            case 3:
                entry = self.add_entry()
                self.DB.add_entry(entry[0], entry[1], entry[2])
            case 4:
                self.del_entry()
            case 5:
                self.edit_entry()

    """Starts the application"""
    def application(self):
        while self.run_app:
            self.show_menu()
            self.handle_input()

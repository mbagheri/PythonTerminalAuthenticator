from Database import Database

"""
Entry class which offers the methods
to edit the name of the service and the
account linked to the service for 2FA
"""

class Entry:

    def __init__(self, id):
        self.DB = Database()
        self.show_options(id)

    """Offers the user the options to choose which information to edit"""
    def show_options(self, id):
        decision = input("\n(1) Update Account Name, (2) Update Website Name, (3) Menu\nInput: ")
        match int(decision):
            case 1:
                self.update_acc(id)
            case 2:
                self.update_website(id)
            case 3:
                return

    """Updates the account information linked to the service"""
    def update_acc(self, id):
        new_acc = input("\nNew Account Name or exit with 'n': ")
        if new_acc == 'n':
            print("\nExiting Update")
            return
        else:
            self.DB.update_acc(id, new_acc)

    """Updates the service information"""
    def update_website(self, id):
        new_site = input("\nNew Website Name or exit with 'n': ")
        if new_site == 'n':
            print("\nExiting Update")
            return
        else:
            self.DB.update_site(id, new_site)

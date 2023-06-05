import sqlite3

"""
The class which is responsible for maintaining 
all the information in a database file
"""
class Database:

    def __init__(self):
        self.con = sqlite3.connect("authenticator.db")
        self.cur = self.con.cursor()
        self.create_table()

    """Creates the necessary table if it doesn't exist"""
    def create_table(self):
        self.con.execute("CREATE TABLE if NOT EXISTS authenticator(id INTEGER PRIMARY KEY AUTOINCREMENT, website VARCHAR(50), account VARCHAR(100), b32s VARCHAR(100))")

    """Takes the necessary information to create a new entry"""
    def add_entry(self, website, account, b32s):
        try:
            self.con.execute(f"""INSERT INTO authenticator(website, account, b32s) VALUES('{website}', '{account}', '{b32s}')""")
            self.con.commit()
            print("Successfully entered: " + website + " ," + account + " , " + b32s + " into database\n")
        except:
            self.con.rollback()
            print("Entry into database was not possible")

    """Deletes an entry after receiving its ID"""
    def del_entry(self, id):
        try:
            self.con.execute(f"""DELETE FROM authenticator WHERE id = '{id}'""")
            self.con.commit()
        except:
            return False

    """Searches for and returns all the entries in the Table"""
    def get_entries(self):
        query = self.con.execute(f"""SELECT id, website, account FROM authenticator""").fetchall()
        return query

    """Returns the entry from a given ID if found"""
    def get_entry(self, id):
        try:
            (account, b32s) = self.con.execute(f"""SELECT account, b32s FROM authenticator WHERE id = '{id}'""").fetchone()
            return account, b32s
        except:
            return False

    """Returns the base32secret from a corresponding ID"""
    def get_b32s(self, id):
        try:
            query = self.con.execute(f"""SELECT b32s FROM authenticator WHERE id = '{id}'""").fetchone()
            return query[0]
        except:
            print("An issue occured while trying to get the TOTP\nCheck if the ID is really available")

    """Updates the account information"""
    def update_acc(self, id, account):
        try:
            self.con.execute(f"""UPDATE authenticator SET account='{account}' WHERE id='{id}'""")
            self.con.commit()
            print("Update Successful")
        except:
            print("Updating Account not possible")

    """Updates the service information"""
    def update_site(self, id, website):
        try:
            self.con.execute(f"""UPDATE authenticator SET website = '{website}' WHERE id='{id}'""")
            self.con.commit()
        except:
            print("Updating Account not possible")


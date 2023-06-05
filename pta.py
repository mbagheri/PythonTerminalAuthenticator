from Authenticator import Authenticator

authenticator = Authenticator() # Creates an Object of the Authentication Class
try:
    authenticator.application() # Starts the application by calling the method
except:
    print("\nThe Program was quit unexpectedly")

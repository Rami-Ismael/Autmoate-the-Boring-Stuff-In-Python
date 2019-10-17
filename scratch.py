#this method will call the PreInstall webscraping libarary in python
#the sys method will for sending the potential command line arguments
import webbrowser,sys
#this method will open a url on the web
#webbrowser.open('http://inventwithpython.com/')
#goal
    #1. get sa street fromt he command line argumnets or clipboard.
        #1. read the comman lin arguments from or the lcipboard

    #2. Opens the web browest to the Google Maps page fro the address.
        #1. call the web browser .open function to open the browser
#Step 1:
    #1.  figure out what URL to use
        #1.https://www.google.com/maps/place/your_address_string
# the greater than 1 then this is a command line argument
if(len(sys.argv))>1:
    #Get address fro command line.
    #this will get every element of the string into an array
    address = " ".join(sys.argv[1:])
    print(address)
import webbrowser as wb
from gui import optionMenu
from gui import completeMenu
from getMentions import *

archive = getArchive()

def FindByUser(archive, threshold = 0):
    '''This application takes a twitter archive object, opens an user input display in order to select
    a particular user mentioned in their tweets (with over 10 mentions) and open these tweets in a browser'''

    #unpack a tuple of a [0] dictionary of the users mentioned and their respective mention count
    #and a [1] sorting order to display these users
    mentioned,sortOrder = getMentions(archive,sort=True)

    #create a list of only the mentioned users display name sorted by the sorting order.
    userList = [(mentioned[k][0]) for k in sortOrder if mentioned[k][1] > threshold]

    #select an user from the userList with a GUI
    user = completeMenu(userList)
    #if user is selected, this loops through the archive collecting tweets from them.
    if user > 0:
        tweetsCollected = [archive[tweet] for tweet in archive if archive[tweet].getmentions() != None and archive[tweet].getmentions()[0][0] == sortOrder[user]]
        #opens the tweets collected in web browser tabs if they are less than 25 (to not exceed Twitter's rate limit)
        for tweet in tweetsCollected:
            print(tweet)
            if len(tweetsCollected) < 45:
                wb.open_new_tab(tweet.url())
            else:
                print("_________________")
                pass
    else: pass

FindByUser(archive)

from getArchive import *

def getMentions(archive, sort=False, USERNAME=True):

    if USERNAME: y = 0
    else: y = 1

    mentioned = {}
    #Create a list that collects all user mentions per tweet by looping through the archive
    mentions = [archive[tweet].getmentions()[0] for tweet in archive if archive[tweet].getmentions() != None]

    #Create a dictionary that stores each user mentioned and how many times they are mentioned
    #by looping through the previous list
    for mention in mentions:
        if mention[0] not in mentioned:
            mentioned[mention[0]] = [mention[1+y],0]
        mentioned[mention[0]][1] += 1

    #Create a sorted order, either by mention count, alphabetical or twitter ID.
    if sort == True:
        sortOrder = sorted(mentioned.keys(), key= lambda k : mentioned[k][1], reverse = True)
    elif sort == False:
        sortOrder = mentioned
    elif sort == ID:
        sortOrder = sorted(mentioned.keys(), key = lambda k : (len(k),k))

    return mentioned,sortOrder

from timezone import *

class Tweet:
    '''Class containing all the information associated with an individual tweet'''

    def __init__(self, id, text, time, favs, mentions = None):
        self.id = id
        self.text = text
        self.time = time
        self.favs = favs
        self.mentions = mentions

    def __str__(self):
        return '''{}\n{}'''.format(self.text,self.getdate())

    def url(self):
        return '''https://twitter.com/adrianleon/status/{}'''.format(self.id)

    def getdate(self):
        date = self.time.split()
        weekday = date[0]
        month = date[1]
        day = int(date[2])
        hour = [int(x) for x in date[3].split(':')]
        year = int(date[5])
        return '''{} {} {} – {}:{}'''.format(year,month,day,timezone(hour[0],6),hour[1])

    def getmentions(self):
        if len(self.mentions) > 0:
            return self.mentions
        else:
            return None

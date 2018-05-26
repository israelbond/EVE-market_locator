import json
import urllib.request
import requests
import time
#Still need to use time to sort through zkill data. There is more of an hour range in return kill mails. 
#create object to store zkill data in.
class Zkill:
    def __init__(self, time, location):
        self.time = time
        self.location = location

#Print killmails to screen with time, system, and character id. Some kills mails don't have a character_id and I'm unsure of why. Will loop until redisq sever sends a "null package" 
while True:
    webUrl = urllib.request.urlopen('https://redisq.zkillboard.com/listen.php') 
    data = webUrl.read()
    jData = json.loads(data.decode('utf-8'))
    #print(jData)
    if jData['package'] is None:
        print('null hit!')
        break
    zTime = jData['package']['killmail']['killmail_time']
    parts = zTime.split('T')
    time = parts[1]
    time = time[:-1]
    Zkill.time = time
    Zkill.location = jData['package']['killmail']['solar_system_id']
    try:
        print(zTime, Zkill.location, jData['package']['killmail']['victim']['character_id'] )
    except:
        print(zTime, Zkill.location )

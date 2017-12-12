#import libraries
from bs4 import BeautifulSoup #pip install bs4
import keyboard #pip install keyboard
import urllib2 
import threading
from datetime import date
from twilio.rest import Client # pip install twilio

# Your Account SID & Auth Token from twilio.com/console
account_sid = "XXX"
auth_token  = "XXX"

client = Client(account_sid, auth_token)

def track():
 if minutes > 0:
  clock = threading.Timer(minutes, track)
  clock.start()
 webPage = urllib2.urlopen(url)
# print str(webPage.getcode())
 soup = BeautifulSoup(webPage, 'html.parser')
 status_box = soup.find('div', {'class' : 'keel-grid statusSubHeadline'})
 status = status_box.text.strip()
 flight_box = soup.find('div', {'class' : 'col col-6-12'})
 flight = flight_box.text.strip()
 
 message = client.messages.create(
    to="#", 
    from_="#",
    body=flight + ' ' + status)
 
 print flight + ' ' + status
 print(message.sid)
 if minutes > 0:
  while True:
    if keyboard.is_pressed('escape'):
     clock.cancel()
     break

def var():
 today = date.today()
 flightnum = raw_input('Enter airline ICAO code - flight number: ')
 global minutes 
 minutes = input('How often do you want to check? (minutes): ') * 60
 global url 
 url = 'https://www.kayak.com/tracker/' + flightnum + '/' + str(today)
 print 'Checking for flight ' + flightnum + ' every ' + str(minutes / 60)+ ' minutes'
 print url
# print today
# print flightnum
# print minutes
 track()

var()

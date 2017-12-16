from bs4 import BeautifulSoup
from twilio.rest import Client
import keyboard, urllib2, time, sys, threading
from datetime import date

account_sid = 'AC509d5fba13bf7e990d5d7925d4639a39'
auth_token  = '7151508e9bf41aeb23c4d3c610a1d586'

client = Client(account_sid, auth_token)

class Tracker():
  """Class which scrapes data on air flights."""
  
  def __init__(self, minutes, flightnum, url):
    self.sloppy = True
    self.url = url
    self.flightnum = flightnum
    self.minutes = float(minutes)
    self.track()

  def ok(self):
    self.sloppy = True

  def track(self):
    """Tracks flight"""
    while keyboard.is_pressed('escape') != True:
      if self.sloppy == True:
        webPage = urllib2.urlopen(self.url)
        soup = BeautifulSoup(webPage, 'html.parser')
        status_box = soup.find('div', {'class' : 'keel-grid statusSubHeadline'})
        status = status_box.text.strip()
        flight_box = soup.find('div', {'class' : 'col col-6-12'})
        flight = flight_box.text.strip()
        message = client.messages.create(
         to='9712011367', 
         from_='5312016897',
         body=flight + ' ' + status)
        print flight + ' ' + status
        print(message.sid)
        self.sloppy = False
        Go = threading.Timer(self.minutes * 60, self.ok)
        Go.start()
    Go.cancel()
    sys.exit()

def main():
  """
  Defines variables for the tracking 
  Example usage: flighttracker.py [code] [minutes]
  """
  today = date.today()
  if len(sys.argv) > 1:
    flightnum = sys.argv[1]
    if len(sys.argv) > 2:
      minutes = sys.argv[2]
    else:
      minutes = input("How often do you want to check? (minutes): ")
  else:
    flightnum = raw_input('Enter airline ICAO code - flight number: ')
    minutes = input('How often do you want to check? (minutes): ')
  url = 'https://www.kayak.com/tracker/' + flightnum + '/' + str(today)
  print 'Checking for flight ' + flightnum + ' every ' + str(minutes) + ' minutes. press ESC to exit.'
  Thing = Tracker(minutes, flightnum, url)

if __name__ == "__main__":
  main()

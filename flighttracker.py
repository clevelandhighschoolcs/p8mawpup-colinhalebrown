from bs4 import BeautifulSoup
import keyboard, urllib2, time, sys, threading
from datetime import date


class Tracker():
  
  def __init__(self, seconds, flightnum, url):
    self.sloppy = True
    self.url = url
    self.flightnum = flightnum
    self.seconds = float(seconds)
    print self.seconds
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
        print flight + ' ' + status
        self.sloppy = False
        Go = threading.Timer(self.seconds, self.ok)
        Go.start()
    Go.cancel()
    sys.exit()



def main():
  """
  Defines variables for the tracking 
  Example usage: flighttracker.py [code] [seconds]
  """
  today = date.today()
  if len(sys.argv) > 1:
    flightnum = sys.argv[1]
    if len(sys.argv) > 2:
      seconds = sys.argv[2]
    else:
      seconds = input("How often do you want to check? (seconds): ")
  else:
    flightnum = raw_input('Enter airline ICAO code - flight number: ')
    seconds = input('How often do you want to check? (seconds): ')
  url = 'https://www.kayak.com/tracker/' + flightnum + '/' + str(today)
  print 'Checking for flight ' + flightnum + ' every ' + str(seconds) + ' seconds'
  Thing = Tracker(seconds, flightnum, url)

if __name__ == "__main__":
  main()

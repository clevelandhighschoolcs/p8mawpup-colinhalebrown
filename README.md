# Flight Tracker
This tool will tell you how soon a flight is supposed to land. It will also tell you the status of the flight whether it is on time, delayed, or if it has landed. When the propt appears to input a ICAO Airline code then the flight number seperated by a hiphen. 

ICAO Airline Code - Flight Number
> Example:
> ASA-11,
> Alaska Airlines flight 11

Common Airlines

| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska Airline | ASA |
| American Airline | AAL |
| Delta Airlines | DAL |
| Hawaiian Airlines | HAL |
| JetBlue Airway | JBU |
| Southwest Airlines | SWA |
| Spirit Airlines | NKS |
| United Airlines | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

![Flow Chart](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/flowchart.png)

# Installation Tutorial
This tool is made for python 2.7.14, mileage may vary. 

## Install Needed Liberaries
Open your virtual enviroment or what ever instance of python you intend on using and install the two liberaries BeautifulSoup4 and Keyboard.  
```python
pip install bs4
pip install keyboard
```
## [Download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) the Code
In whatever instane of python you have installed the liberaries in [download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) or [clone](https://github.com/colinhalebrown/Flight-Tracker.git) and move the flighttracker.py to that destination.

![Folder example](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/folder.PNG)

## Run flighttracker.py
In your virtual enviroment run flighttracker.py.

![console](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/run.gif)

```console
python flighttracker.py
```

## Input your flight & check time
First it will ask for your flight code. This code is in ICAO format, two parts the airlines and the flight number seperated by a hyphen. 

Here is an example using flight asa-123 (Alaska Airline flight 123)

![example flight ASA-123](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/asa-123.gif)

| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska Airline | ASA |
| American Airline | AAL |
| Delta Airlines | DAL |
| Hawaiian Airlines | HAL |
| JetBlue Airway | JBU |
| Southwest Airlines | SWA |
| Spirit Airlines | NKS |
| United Airlines | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

After You have put in your airline code input how often you want it to check the status of the flight in seconds. If you want it to only check once input 0. If you input a number greater than 0 to stop it hit enter and it will end the program. 

![examaple flight ASA-123 comleted](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/asa-123(2).PNG)

# Common Errors
If the flight ICAO code or flight number are noT accociated with an actual flight it will check and give a large error code every few seconds. 

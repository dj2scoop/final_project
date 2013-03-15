final_project
=============

Final project for Internet Programming with Python

I call it ViewTube. Not very original, but that is because my initial project idea fell through.


Original Project Goals:
----------------------
* Login system.
* Create User system.
* User can enter Favorite Band names to search for upcoming concerts.
* Use API or scrape Ticketmaster or some other Concert Venue ticketing agency.
* Return list of dates and places to the user.
* Keep a history of User's previous searches.

Problems: Ticketmaster does not have an API and their html would not be scrapable(sic?)
Live Nation had an API that I found using Programmable Web, but it was discontinued 2 years ago.
Stub Hub does have an API: http://stubhubapi.nobisi.com/index.php?title=PHP_Code_Samples but I was losing interest.

New Project Goals:
-----------------
* Login system.
* Create User system.
* User can Enter keywords to search YouTube.
* Use Google's YouTube API to return videos related to keyword search.
* Allow User to select a video and watch it on embedded player.
* Keep a history of User's previous searches.


Final Project Outcome:
----------------------
* Login system.
* Create User system.
* User can Enter keywords in Search field.
* Search is not actually performed.
* Result is error.
* Was not able to get YouTube API working.
* User cannot watch a video.
* History page does show search history.
* Sites appearance does not look much different than djangor assignment (Meaning it does not look nice).

Small things: 
* Created all the HTML files for views. Not sure if they all work ( You can view the history page, it works-ish).
* Created all URLs for the site.
* There is code for CredentialsModel and FieldFlow that was to be used with YouTube API, but never got it working.
* Built some forms, views, and models, but they are incomplete.
* Need more familiarity with Django and YouTube API.

Instructions:
-------------
* Sign-up for Google API account
* Create Virtual Environment
* Database: sqlite3
* Install django
* Install django-registration
* Install google API package
* Clone GIT repository
* Update the settings.py file with a relevent database path
* Update search.py with your API key

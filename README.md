# Text Match

Text Match is a web application for mathcing two text blobs.
This application accepts two text strings and matches them based on the match option chosen
A success / failure code is shown based on the test results

# What is included
* app.py : contains the Flask framework
* index.html : UI
* Docker files for creating a docker image
  * docker-compose.yml : configuration file defining services, volume, environment
  * Dockerfile : commands to create an image
  * requiremnts.txt : dependencies (in this case Flask)

# How to setup
* Run webserver from local machine
  * Open command line interface (Terminal or cmd on windows)
  * Change directory to project directory (cd directoryname)
  * Run "python app.py". This will start the local web service and return an IP address
  * Open the IP address in your browser
  
# The Application
* Enter two blobs of text in the two text boxes
* Select how you want to match
  * Case sensitive exact match
  * Case insensitive exact match
  * Match words only i.e. ignore punctuations
* Hit Submit. If the match is successful, a 1 is returned in match score and 0 is reutrned if match is unsuccessful

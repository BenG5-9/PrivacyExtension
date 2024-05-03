# Privacy Companion (Chrome Extension)
CMSC 491 Data Privacy

## Required python libraries
1. `pip install -v flask`
2. `pip install -v flask_cors`
3. `pip install -v bs4`
4. 'pip install --upgrade openai'
5. `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
6. pip install brotli

## HOW TO RUN
 - Download the all of the files and place into a folder
 - In Chrome, click on the extensions button to the right of the URL field
 - Click manage extensions, load unpacked, and select the `extension/` folder with the `*.js` files in it
 - Open up your console from the `backend/` folder, and run `app.py` with python
 - Navigate to a website

## THINGS TO DO
 - Privacy parser - 2 people?
 - UI for pop-up
 - Opt-out script

## OPT-OUT SCRIPT
- Must be a tester for the gmail api for the project
- must run `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
- Currently only Ben's account is connected to the script

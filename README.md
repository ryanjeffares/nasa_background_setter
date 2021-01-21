# nasa_background_setter

This Python script will send a request to NASA's Astronomy Photo of the Day API when you run the file, and then every day (I have made mine run whenever I start my PC), downloads the file and sets it to be your desktop background on Windows 10. It will also save the description of the image with its date to a text file. 

This script requires the <a href="https://github.com/nasa/apod-api"> NASA APOD API </a> - pull their repo, follow instructions to set up as standard environment, then pull this repo in the root directory of the NASA repo, run ```pip install -r requirements.txt``` for schedule and urllib3 and it should run.
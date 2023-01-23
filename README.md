# AI Fake Face Telegram Bot

Downloads & Sends AI generated photos of non existing humans via Telegram Bot.

Just for fun!

## Content:

- /AI: Contains the classification of age & gender (detect.py) with AI model files, can be used standalone
- create_db.py is a one time run helper script to create the database for generate_faces.py
- data.py is used as helper functions to connect the bot to a sqlite database for usermanagement
- generate_faces.py is used to download and classify the faces of [thispersondoesnotexist](https://thispersondoesnotexit.com)
- main.py is the telegram bot itsself
- requirements.txt need to be installed with pip
- token.config.example is a config file example where you can put your telegram bot token

## Usage:

1) Install requirements.txt with pip
2) Run python create_db.py once
3) Run python generate_faces.py once, this will take a while!
4) Now you can start the telegram bot with python main.py

## Attention:

Bot and helper scripts are running, but bot delivers at the moment no pictures. Integration with DB is not yet finished.

All images are from [thispersondoesnotexist](https://thispersondoesnotexit.com).
Thanks to [smahesh29](https://github.com/smahesh29/Gender-and-Age-Detection) and [hankhank10](https://github.com/hankhank10/fakeface)!
"""
    Downloads & Classifies the Images from Thispersondoesnotexist.
    With times_to_run you can set the amount of downloaded images.
    
    :return: Images with Faces that does not exist
    :rtype: img
    
"""

import requests, shutil, secrets, time
from datetime import datetime
from active_alchemy import ActiveAlchemy

from AI import detect

db = ActiveAlchemy("sqlite:///db.sqlite")

url = "https://thispersondoesnotexist.com/image"
temp_file = "temp_img.jpg"
times_to_run = 500
seconds_to_sleep = 1


class ImageRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    filename = db.Column(db.String(100))
    hosting = db.Column(db.String(100))
    date_added = db.Column(db.DateTime)
    source = db.Column(db.String(100))
    last_served = db.Column(db.DateTime)


def download_face():
    response = requests.get(url, stream=True)
    with open(temp_file, "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return


def move_file(gender, age):
    filename = gender + "_" + str(age) + "_" + secrets.token_hex(20) + ".jpg"
    location_to_move_to = "images/" + filename
    shutil.move(temp_file, location_to_move_to)
    return filename


def write_db(gender, age, filename):
    image_record = ImageRecord(
        gender=gender,
        age=age,
        filename=filename,
        date_added=datetime.utcnow(),
        source="thispersondoesnotexist",
        hosting="local",
        last_served=datetime.utcnow(),
    )

    db.session.add(image_record)
    db.session.commit()
    return


if __name__ == "__main__":

    for a in range(0, times_to_run):
        download_face()
        gender, age = detect.AI_detect(temp_file)
        if gender != "unclear":
            filename = move_file(gender, age)
            write_db(gender, age, filename)
        else:
            print("skipping")
        time.sleep(seconds_to_sleep)

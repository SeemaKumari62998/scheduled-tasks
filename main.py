import smtplib
import random
import datetime as dt
import pandas
import os

MY_EMAIL= os.environ.get("MY_EMAIL")
PASSWORD=os.environ.get("PASSWORD")

now= dt.datetime.now()
today=(now.month,now.day)

data=pandas.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for(index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person=birthday_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!!\n\n {contents}")



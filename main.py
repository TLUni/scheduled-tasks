import datetime as dt
import random
import os
import pandas
import smtplib

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pandas.read_csv("birthdays.csv")

print(birthdays)

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}
print(birthdays_dict)

for i in birthdays_dict:
    if today == i:
        print("Yes")
        letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter}.txt", "r") as letter_file:
            mail_string = letter_file.read()
            mail_string = mail_string.replace("[NAME]",birthdays_dict[i]["name"])
        print(mail_string)

        to_email = birthdays_dict[i]["email"]

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Happy Birthday\n\n{mail_string}")

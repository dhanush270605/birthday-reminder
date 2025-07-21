import pandas as pd
from datetime import datetime, timedelta
from twilio.rest import Client

account_sid = 'AC75bbfc03424d2fea9aa3a9cd62215c4a'
auth_token = '7de0a4f34817cf9bab83e1400319864e'
client = Client(account_sid, auth_token)

my_number = 'whatsapp:+918778198552'  # Your verified number
twilio_number = 'whatsapp:+14155238886'  # Twilio sandbox number

df = pd.read_csv('birthday_new.csv')
today = datetime.now().date()

for _, row in df.iterrows():
    name = row['name']
    dob = datetime.strptime(row['dob'], "%d-%m-%Y").date()
    dob_this_year = dob.replace(year=today.year)

    if dob_this_year == today:
        msg = f"🎉 Today is {name}'s birthday!"
        client.messages.create(from_=twilio_number, body=msg, to=my_number)

    elif dob_this_year == today + timedelta(days=10):
        msg = f"📅 Reminder: {name}'s birthday is in 10 days on {dob_this_year.strftime('%d %b')}!"
        client.messages.create(from_=twilio_number, body=msg, to=my_number)

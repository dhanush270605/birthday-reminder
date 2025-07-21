import pandas as pd
from datetime import datetime, timedelta
from twilio.rest import Client

account_sid = 'AC75bbfc03424d2fea9aa3a9cd62215c4a'
auth_token = '7de0a4f34817cf9bab83e1400319864e'  # Replace with your real token
client = Client(account_sid, auth_token)

my_number = 'whatsapp:+918778198552'  # YOUR WhatsApp number
twilio_number = 'whatsapp:+14155238886'  # Twilio sandbox

df = pd.read_csv('birthday_new.csv')
now = datetime.now()
today = now.date()

for _, row in df.iterrows():
    name = row['name']
    dob = datetime.strptime(row['dob'], "%d-%m-%Y").date()
    dob_this_year = dob.replace(year=today.year)

    if dob_this_year == today and now.hour == 0:
        msg = f"🎉 Today is {name}'s birthday!"
        client.messages.create(from_=twilio_number, body=msg, to=my_number)

    elif dob_this_year == today + timedelta(days=10) and now.hour == 9:
        msg = f"📅 Reminder: {name}'s birthday is in 10 days on {dob_this_year.strftime('%d %b')}!"
        client.messages.create(from_=twilio_number, body=msg, to=my_number)

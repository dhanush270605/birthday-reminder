import pandas as pd
from datetime import datetime, timedelta
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC75bbfc03424d2fea9aa3a9cd62215c4a'
auth_token = '7de0a4f34817cf9bab83e1400319864e'
client = Client(account_sid, auth_token)

# WhatsApp numbers
my_number = 'whatsapp:+918778198552'
twilio_number = 'whatsapp:+14155238886'

# Load the CSV
try:
    df = pd.read_csv('birthday_new.csv')
except Exception as e:
    print("❌ Error reading CSV file:", e)
    exit(1)

today = datetime.now().date()
ten_days_later = today + timedelta(days=10)

# Loop through each row
for _, row in df.iterrows():
    try:
        name = row['name']
        dob = datetime.strptime(row['dob'], "%d-%m-%Y").date()
        dob_this_year = dob.replace(year=today.year)

        if dob_this_year == today:
            msg = f"🎉 Today is {name}'s birthday!"
            print("✅", msg)
            client.messages.create(from_=twilio_number, body=msg, to=my_number)

        elif dob_this_year == ten_days_later:
            msg = f"📅 Reminder: {name}'s birthday is in 10 days on {dob_this_year.strftime('%d %b')}!"
            print("✅", msg)
            client.messages.create(from_=twilio_number, body=msg, to=my_number)

    except Exception as e:
        print(f"❌ Error processing row {row}:", e)

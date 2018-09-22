
# Download the helper library from eas
from twilio.rest import Client

import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=os.getenv('TWILIO_PHONE'),
                     to='+18178995567'
                 )

print(message.sid)


# prompt the user the phone number
# validated the phone number
# propmt user to send message
# add the variables to request object


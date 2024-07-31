# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from dotenv import load_dotenv
load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


response = VoiceResponse()
response.say("Hello Officer, enjoy exclusive banking benefits tailored for you, including low-interest loans and financial planning support", language="hi-IN", voice="Polly.Aditi")

call = client.calls.create(
    from_=os.getenv("TWILIO_NUMBER"),
    to="+919987483893",
    twiml=str(response)
)

print(call.sid)
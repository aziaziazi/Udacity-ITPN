# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC938d13653230c8696fb61e2b8e575e20"
auth_token  = "1c48b5939a6ff77b564fdb0b77de60af"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Camille",
    to="+33652098020",    # Replace with your phone number
    from_="+33977556798") # Replace with your Twilio number
print message.sid

# Your code here.
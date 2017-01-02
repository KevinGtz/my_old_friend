from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACbdd0bd654cd0b836b67b341065d72cbd"
AUTH_TOKEN = "3b3a5a56aece7ba086c81a23e832c894"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello Monkey!",  # Message body, if any
    to="+5255642333773",
    from_="+525549998702",
)
print message.sid
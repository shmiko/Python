from twilio.rest import TwilioRestClient

account_sid = "ACfeb5d4b7577e9ad69cc8aab37f9d11c4"
auth_token = "f977244a9bad4b1142095ca8d422cdff"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="How are those travel plans going, ready to book flights for departure 11th December 2016 returning January 23rd 2017?"
    ,to="+610432753310"
    ,from_="+12093543738")
print message.sid

from twilio.rest import Client 
 
account_sid = '' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='XXXXXXXX',  
                              body='Hello, this is sent from a python script.',      
                              to='XXXXXXXX' 
                          ) 

print(message.sid)
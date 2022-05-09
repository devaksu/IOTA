import iota_client
from datetime import datetime
import random

INDEX = 'index'

"""Create a timestamp with a random number 
and save it to Tangle"""

client = iota_client.Client()
time = datetime.now().strftime('%H-%M-%S')
data = f'{time} ; random number: {str(random.randint(0,10))}'
message = client.message(index=INDEX, data=data.encode('utf8'))
print(f'Message ID: {message["message_id"]}')


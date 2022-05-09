import iota_client

"""This app retrieves indexed data from the Tangle 
and translates it to readable form""" 

INDEX = 'index'

client = iota_client.Client()
message = client.find_messages(indexation_keys=[INDEX])

def decoder(data):
    string = ""
    for i in data:
        s = str(chr(i))
        string = string + s
        i =+ 1

    print(string)

for i in range(len(message)):
    value = message[i]['payload']['indexation'][0]['data']
    i =+ 1
    decoder(value)



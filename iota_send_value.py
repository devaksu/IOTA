import iota_client
import secret

"""Send value to other address using IOTA Network"""

SEED = secret.Seed
DEST_ADDRESS = 'Destination address'

client = iota_client.Client()
transaction = client.message(
    seed = SEED,
    outputs = [
        {
            'address' : DEST_ADDRESS,
            'amount' : 1_000_000,
        }
    ]
)
print(f'Message ID: {transaction["message_id"]}')
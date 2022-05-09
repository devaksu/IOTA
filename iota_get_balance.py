import iota_client
import secret

"""Get balance of certain Seed or address"""

NODE_URL = 'https://api.lb-0.h.chrysalis-devnet.iota.cafe:443'
SEED = secret.SEED
ADDRESS = 'f7d21d7c1e38ddd60aa64bb957c0ccf6fc1bc1691b5fad3e918e8b7ad01625bc'

client = iota_client.Client(
    nodes_name_password=[[NODE_URL]], 
    node_sync_disabled=True
    )

# Get balance of entire Seed
balance = client.get_balance(seed=SEED)
print(f'balance of SEED: {balance}')

# Get balance of a single address
print(client.get_address_balance(ADDRESS))
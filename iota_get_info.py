import iota_client

### Status of the network ###

NODE_URL = "https://chrysalis-nodes.iota.org:443"

client = iota_client.Client(
    nodes_name_password=[[NODE_URL]], 
    node_sync_disabled=True
    )

print(f'node_info: {client.get_info()}')
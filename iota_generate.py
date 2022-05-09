import os
import hashlib
import iota_client

""" Generate proper Seed and Addresses to work with IOTA Tangle"""

SEED = hashlib.sha256(os.urandom(256)).hexdigest()

client = iota_client.Client()
address = client.get_addresses(
    seed=SEED,
    account_index=0,
    input_range_begin=0,
    input_range_end=10,
    get_all=False
)

bech_address = address[0][0]
hex_address = client.bech32_to_hex(bech_address)

with open('secret.py', 'w') as f:
    f.write(f"SEED: '{SEED}' \n")
    f.write(f"Bech32: '{bech_address}' \n")
    f.write(f"Hex_64: '{hex_address}' \n")
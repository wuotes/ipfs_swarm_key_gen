import secrets

with open(r'./swarm.key', r'w') as key_file:
    key_file.write(f'/key/swarm/psk/1.0.0/\n/base16/\n{secrets.token_bytes(32).hex()}')
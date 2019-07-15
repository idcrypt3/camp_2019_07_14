def new_hash(message):
    digest = 0
    for c in message:
        digest += ord(c)
        digest = digest % 256
        return digest

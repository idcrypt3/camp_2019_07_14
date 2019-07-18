def new_hash(message):
    digest = 1
    for c in message:
        digest += ord(c)
        digest = digest % 256
        print(digest)
    return digest

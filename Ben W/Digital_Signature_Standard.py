def new_hash (message):
    digest = 0
    for c in message:
        digest += ord(c)
        digest = digest % 256
    return digest
def mod_inv(n, modulus):
    q = [0, 0]
    r = [modulus, n]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2]// r[index - 1]
        q.append(quotient)
        




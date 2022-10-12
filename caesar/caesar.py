key = input ("Key: ")

try:
    int(key)
    while key <= '0':
        key = input("Invalid key format \nTry again: ")
except ValueError:
    while key != int():
        key = input("Invalid key format \nTry again: ")

plaintext = input("plaintext: ")

ciphertext = 'inicial'

i = 0
letters = len(plaintext)
while i < letters:
    if (plaintext[i] != ' ') and (plaintext[i] != ',') and (plaintext[i] != "'") and (plaintext[i] != '.') and (plaintext[i] != '!'):
        ciphertext[i] = ord (plaintext[i]) + key

print(ciphertext)


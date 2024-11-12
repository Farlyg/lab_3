import math

def encrypt_message(message, cols):
    message = message.replace(" ", "").upper()

    rows = math.ceil(len(message) / cols)

    table = [[''] * cols for _ in range(rows)]
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(message):
                table[row][col] = message[index]
                index += 1
            else:
                table[row][col] = ''

    encrypted_message = ""
    for row in table:
        encrypted_message += ''.join(row) + " "

    return encrypted_message.strip()


def decrypt_message(encrypted_message, cols):
    encrypted_message = encrypted_message.replace(" ", "").upper()

    rows = math.ceil(len(encrypted_message) / cols)

    table = [[''] * cols for _ in range(rows)]
    index = 0
    for row in range(rows):
        for col in range(cols):
            if index < len(encrypted_message):
                table[row][col] = encrypted_message[index]
                index += 1

    decrypted_message = ""
    for col in range(cols):
        for row in range(rows):
            if table[row][col] != '':
                decrypted_message += table[row][col]

    return decrypted_message



message = "НЕЯСНОЕ СТАНОВИТСЯ ЕЩЕ БОЛЕЕ НЕПОНЯТНЫМ"
cols = 7

encrypted = encrypt_message(message, cols)
print("Зашифрованное сообщение:", encrypted)

decrypted = decrypt_message(encrypted, cols)
print("Дешифрованное сообщение:", decrypted)
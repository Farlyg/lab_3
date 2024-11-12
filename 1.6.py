def create_cipher_table(key, alphabet):
    unique_key = ''.join(sorted(set(key), key=key.index))
    remaining_letters = ''.join([ch for ch in alphabet if ch not in unique_key])
    table = list(unique_key + remaining_letters)
    return [table[i:i+6] for i in range(0, len(table), 6)]

def find_position(table, char):
    for i, row in enumerate(table):
        if char in row:
            return i, row.index(char)
    return None

def encrypt(text, table):
    encrypted_text = ""
    rows = len(table)
    for char in text:
        position = find_position(table, char)
        if position is None:
            encrypted_text += char
            continue
        row, col = position
        next_row = (row + 1) % rows
        if col >= len(table[next_row]):
            encrypted_char = table[next_row][0]
        else:
            encrypted_char = table[next_row][col]
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, table):
    decrypted_text = ""
    rows = len(table)
    for char in text:
        position = find_position(table, char)
        if position is None:
            decrypted_text += char
            continue
        row, col = position
        prev_row = (row - 1) % rows
        if col >= len(table[prev_row]):
            decrypted_char = table[prev_row][0]
        else:
            decrypted_char = table[prev_row][col]
        decrypted_text += decrypted_char
    return decrypted_text

key = "РЕСПУБЛИКА"
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
table = create_cipher_table(key, alphabet)

message = "БЕГОМ"
encrypted_message = encrypt(message, table)
decrypted_message = decrypt(encrypted_message, table)

print("Таблица шифрования:")
for row in table:
    print(" ".join(row))
print("\nСообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
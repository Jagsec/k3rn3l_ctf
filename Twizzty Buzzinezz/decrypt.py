hex_value = '632a0c6d68a7e5683601394c4be457190f7f7e4ca3343205323e4ca072773c177e6e'
flag_fragment = b'flag{'
value_in_bytes = bytes.fromhex(hex_value)
decimal_values = []
for byte in value_in_bytes:
    decimal_values.append(byte)

key_fragment = [flag_fragment[i] ^ decimal_values[i] for i in range(len(flag_fragment))]

key_fragment.append(0)
key = []
while len(key) < len(decimal_values):
    key += key_fragment
    key_fragment = [key_fragment[-1]] + key_fragment[:-1]

for j in range(256):
    key[5] = j
    key[6] = j
    key[13] = j
    key[20] = j
    key[27] = j
    flag = [key[i] ^ decimal_values[i] for i in range(len(decimal_values))]
    plain_text_flag = ''
    for char in flag:
        plain_text_flag += chr(char)
    if plain_text_flag.endswith("Tw1zzt}") or plain_text_flag.endswith("tw1zzt}"):
        print(plain_text_flag)
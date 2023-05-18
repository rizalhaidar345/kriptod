def string_to_binary(string):
    binary = ''.join(format(ord(i)-97, 'b').zfill(8) for i in string)
    return binary

def binary_to_string(binary):
    string = ""
    for i in range(0, len(binary), 8):
        binary_char = binary[i:i+8]
        decimal = int(binary_char, 2)
        string += chr(decimal%97+97)
    return string


def encrypt_decrypt(text, key):
    resultXOR = ""
    bin_text = string_to_binary(text)
    bin_key = string_to_binary(key)
    for i in range(len(bin_text)):
        resultXOR += str(int(bin_text[i]) ^ int(bin_key[i % len(bin_key)]))
    return binary_to_string(resultXOR)

print((encrypt_decrypt("ana", "tes")))

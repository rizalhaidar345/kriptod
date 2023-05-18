def string_to_binary(string):
    binary = ""
    for char in string:
        if 'a' <= char <= 'z':
            binary += format(ord(char) - ord('a'), '05b')
    return binary

def binary_to_string(binary):
    string = ""
    for i in range(0, len(binary), 5):
        binary_char = binary[i:i+5]
        decimal = int(binary_char, 2)
        char = chr(decimal + ord('a'))
        string += char
    return string

def encrypt_decrypt(text, key):
    resultXOR = ""
    bin_text = string_to_binary(text)
    bin_key = string_to_binary(key)
    for i in range(len(bin_text)):
        resultXOR += str(int(bin_text[i]) ^ int(bin_key[i % len(key)]))
    return binary_to_string(resultXOR)

print(encrypt_decrypt("ana", "tes")) 
# Program : Stream Cipher
# Nama    : Rifkhi Akbar
# NIM     : 2007397


import os

# Baca File
nama_file_input = "input.txt"
nama_file_ouput = "output.txt"

path = os.path.dirname(__file__)
full_path_input = os.path.join(path, "input.txt")
full_path_output = os.path.join(path, "output.txt")

# Buat file jika belum ada
if os.path.exists(full_path_input)==False:
    with open(full_path_input, "w") as file:
        file.write("Masukkan input teks di sini, input.txt")

if os.path.exists(full_path_input)==False:
    with open(full_path_output, "w") as file:
        file.write("Ini adalah file untuk output teks")

with open(full_path_input, "r") as file:
    input_teks = file.read()

# Konversi string ke bit
def str_to_bin(string, len_bit):
    string_bit = ""
    for i in range(len(string)):
        string_ord = ord(string[i]) - 97
        string_bit += bin(string_ord)[2:].zfill(len_bit)
    return string_bit

# Konversi bit ke string
def bin_to_str(bit, len_bit):
    string_arr = [bit[i:i+8] for i in range(0,len(bit),len_bit)]
    string_char = [chr(int(string_arr[i],2) + 97) for i in range(len(string_arr))]
    string = "".join(string_char)
    return string

# Buat stream key
def generate_keystream(key_word, string):
    key_bit = str_to_bin(key_word,8)
    len_string_bit = len(str_to_bin(string,8))
    len_key_bit = len(key_bit)
    
    i = 0
    while len(key_bit) < len_string_bit:
        tmp = key_bit[i:i+len_key_bit]
        key_new = str(int(tmp[0]) ^ int(tmp[-1]))
        key_bit += key_new
        i += 1
    return key_bit

# Enkripsi Shift Cipher
def enc_shift(string, key_word):
    string_bit = str_to_bin(string,8)
    key_word_bit = generate_keystream(key_word,string)
    
    enc_result_bit = ""
    for i in range(len(string_bit)):
        enc_result_bit += str(int(string_bit[i]) ^ int(key_word_bit[i]))
    
    enc_result = bin_to_str(enc_result_bit,8)
    
    return enc_result

# Dekripsi Shift Cipher
def dec_shift(string, key_word):
    string_bit = str_to_bin(string,8)
    print(string_bit)
    key_word_bit = generate_keystream(key_word,string)
    
    dec_result_bin = ""
    for i in range(len(string_bit)):
        dec_result_bin += str(int(string_bit[i]) ^ int(key_word_bit[i]))
    
    dec_result = bin_to_str(dec_result_bin,8)
    
    return dec_result

# PROGRAM UTAMA
# Print judul dan kode
def print_judul():
    print("STREAM CIPHER")
    print("[1] Enkripsi Stream Cipher")
    print("[2] Dekripsi Stream Cipher")

# Teks pada input
pesan = "Masukkan pilihan (1/2): "
pesan_peringatan = "Pilihan yang anda masukkan salah. Coba lagi!"

print_judul()

pilihan = input(pesan)

match pilihan:
    case "1":
        # [1] Enkripsi Stream Cipher
        print("\n###### ENKRIPSI STREAM CIPHER ######")
        print("Teks dibaca dari:", full_path_input)
        print("Isi teks:", input_teks)
        print("Masukkan kunci berupa teks tanpa spasi!")
        key = input("Kunci = ")
        enc_result = enc_shift(input_teks, key)

        print("\nHasil Enkripsi:", enc_result)
            
        string = "ENKRIPSI:\n" + "# Plainteks:\n" + input_teks + "\n\n" + "# Hasil Enkripsi:\n" + "{} -> {}".format(key, enc_result)
        with open(full_path_output, "w") as file:
            file.write(string)
        print("Hasil enkripsi telah disimpan di:", full_path_output)
        input()

    case "2":
        # [2] Dekripsi Stream Cipher
        print("\n###### DEKRIPSI STREAM CIPHER ######")
        print("Teks dibaca dari:", full_path_input)
        print("Isi teks:", input_teks)
        print("Masukkan kunci berupa teks tanpa spasi!")
        key = input("Kunci = ")
        dec_result = dec_shift(input_teks, key)

        print("\nHasil Dekripsi:", dec_result)
            
        string = "DEKRIPSI:\n" + "# Cipherteks:\n" + input_teks + "\n\n" + "# Hasil Dekripsi:\n" + "{} -> {}".format(key, dec_result)
        with open(full_path_output, "w") as file:
            file.write(string)
        print("Hasil dekripsi telah disimpan di:", full_path_output)
    case _:
        print("\n"+pesan_peringatan)
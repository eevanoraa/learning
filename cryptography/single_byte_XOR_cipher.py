import string
from langdetect import detect

def bytes_xor(input_string: bytes, xor_key: bytes) -> bytes:
    result = []
    for byte in input_string:
        result.append(byte ^ xor_key[0])
    return bytes(result)

def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False

letters = string.printable
hexstring = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

for letter in letters:
    xor_key = letter.encode()
    decoded_bytes = bytes_xor(hexstring, xor_key)
    try:
        decoded_text = decoded_bytes.decode("ascii")
        if is_english(decoded_text):
            print(decoded_text)
    except UnicodeDecodeError:
            continue
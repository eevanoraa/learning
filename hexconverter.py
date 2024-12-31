import base64

def hexconvert(hex_string):

    plain_text = base64.b16decode(hex_string, casefold=True)
    b64_string = base64.b64encode(plain_text)

    return plain_text, b64_string

if __name__ == "__main__":
    hexconvert(b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
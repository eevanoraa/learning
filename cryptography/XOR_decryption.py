def _bytes_xor(input_string: bytes, xor_key: bytes, quiet=True, check_lens=True) -> bytes:
    if not quiet:
        print(input_string, "XOR", xor_key)
    if check_lens and len(input_string) != len(xor_key):
        raise ValueError("bytestring lengths aren't equal")
    
    result = []
    for byte_1, byte_2 in zip(input_string, xor_key):
        result.append(byte_1 ^ byte_2)
    return bytes(result)

def bytes_xor(*args: bytes, quiet=True, check_lens=False):
    assert len(args) > 0
    result = args[0]
    for arg in args[1:]:
        result = _bytes_xor(result, arg, quiet=quiet, check_lens=check_lens)
    return result


if __name__ == "__main__":
    input_string = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    xor_key = bytes.fromhex("686974207468652062756c6c277320657965")
    result = bytes_xor(input_string, xor_key, quiet=False)

    print(f"{result=}")
    print(f"{result.hex()}")

    if result == bytes.fromhex("746865206b696420646f6e277420706c6179"):
        print("It's correct!")
    else:
        exit("xor didn't work")
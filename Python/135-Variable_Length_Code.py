# Python 2.7

def compress_string(string):
    answer = []
    value_dict = {
        ' ': '11',             'e': '101',
        't': '1001',           'o': '10001',
        'n': '10000',          'a': '011',
        's': '0101',           'i': '01001',
        'r': '01000',          'h': '0011',
        'd': '00101',          'l': '001001',
        '!': '001000',         'u': '00011',
        'c': '000101',         'f': '000100',
        'm': '000011',         'p': '0000101',
        'g': '0000100',        'w': '0000011',
        'b': '0000010',        'y': '0000001',
        'v': '00000001',       'j': '000000001',
        'k': '0000000001',     'x': '00000000001',
        'q': '000000000001',   'z': '000000000000',
        }
    
    string = string[::].lower()

    # Convert to assigned values.
    eight_bit = []
    for char in string[::]:
        bits = ("%s") % (value_dict[char])
        eight_bit.append(bits)
    eight_bit = (''.join(eight_bit))

    # Split into chunks of 8
    chunks = []
    for byte in range(len(eight_bit)):
        if len(eight_bit) > 0 and len(eight_bit) < 8:
            while len(eight_bit) < 8:
                eight_bit += '0'
        while len(eight_bit) > 7:
            byte = eight_bit[:8]
            chunks.append(byte)
            eight_bit = eight_bit[8:]
            #eight_bit = eight_bit[:-8]

    # Convert into hex and print answer.
    for chunk in chunks:
        chunk = int(chunk, 2)
        encoded_value = hex(chunk)[2:].upper() #[2:] to remove the '0x'
        if len(encoded_value) == 1:
            encoded_value = '0' + encoded_value
        answer.append(encoded_value)
    print(' '.join(answer))
    
compress_string(raw_input())

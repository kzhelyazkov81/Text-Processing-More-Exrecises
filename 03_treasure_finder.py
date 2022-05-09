def decrypt(data):
    result = ''
    for i in range(len(data)):
        ascii_ch = ord(data[i])
        key_index = i % len(key)
        ascii_key = key[key_index]
        new_ch = chr(ascii_ch - ascii_key)
        result += new_ch
    return result


def extract(result):
    type = ''
    coordinates = ''
    i = 0
    while i < len(result):
        if result[i] == '&':
            i += 1
            while result[i] != '&':
                type += result[i]
                i += 1
            i += 1
        if result[i] == '<':
            i += 1
            while result[i] != '>':
                coordinates += result[i]
                i += 1
            i += 1
        i += 1
    print(f'Found {type} at {coordinates}')


key = list(map(int, input().split(' ')))
while True:
    data = input()
    if data == 'find':
        break
    result = decrypt(data)
    extract(result)

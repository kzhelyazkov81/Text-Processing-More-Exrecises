def extract(characters, first, last):
    first = ord(first)
    last = ord(last)
    result = 0
    for ch in characters:
        ch_ascii = ord(ch)
        if first < ch_ascii < last:
            result += ch_ascii
    print(result)


first_ch = input()
last_ch = input()
text = input()
extract(text, first_ch, last_ch)

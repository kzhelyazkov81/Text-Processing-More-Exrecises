def extract(name_age):
    name = ''
    age = ''
    i = 0
    while i < len(name_age):
        if name_age[i] == '@':
            i += 1
            while name_age[i] != '|':
                name += name_age[i]
                i += 1
        if name_age[i] == '#':
            i += 1
            while name_age[i] != '*':
                age += name_age[i]
                i += 1
        i += 1
    print(f"{name} is {age} years old.")


rows = int(input())
for i in range(rows):
    data = input()
    extract(data)

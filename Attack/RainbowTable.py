read_path = '../Defend/Output/hashed_sha1.txt'
table = '../Resource/raw_passwords.txt'

rainbow = []


def read_passwords(hashcode):
    global rainbow

    with open(table, 'r') as f:
        rainbow = [x.strip() for x in f]

    with open(read_path, 'r') as f:
        lines = [x.strip() for x in f]
    lookup(lines, hashcode)


def lookup(dictionary, hashcode):
    i = 0

    for line in dictionary:
        if hashcode == line:
            print('SHA1: Result')
            print(rainbow[i])
        else:
            i += 1


read_passwords('bd5e5eb049f3907175f54f5a571ba6b9fdea36ab')

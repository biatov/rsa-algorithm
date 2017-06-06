def divisor(number, mod=0):
    if not mod:
        return list(filter(None, map(lambda i: i if not number % i else '', range(2, number-1))))
    else:
        return list(filter(None, map(lambda i: i if (k * i) % number == 1 else '', range(2, number-1))))[0]


def rsa(data):

    p, q = divisor(n)[0], divisor(n)[1]

    func_phi = (p - 1) * (q - 1)

    l = divisor(func_phi, mod=1)

    for each in data:
        yield (each ** l) % n


def decode(data):
    abc = list(map(lambda i: chr(i), range(97, 123)))
    print('Phrase - ', end='')
    for i in data:
        if i is 2:
            print(' ', end='')
        else:
            print(abc[i-3], end='')
    print()

n = 1739
k = 523

set_data = {
    1: [898, 1224, 426, 426, 619, 553, 682, 1228, 1209, 553, 619, 1228, 1224, 979],
    2: [1484, 1228, 1224, 1346, 718, 973, 1583, 1346, 874, 553, 170, 973, 682, 401],
    3: [973, 170, 973, 718, 1224, 718, 973, 131, 682, 553, 897, 1224, 170, 1228],
    4: [170, 1228, 979, 979, 619, 553, 1401, 898, 979, 973, 576, 718, 170, 1224, 576],
    5: [979, 1228, 874, 1224, 718, 973, 718, 619, 553, 718, 898, 1228, 131, 979, 619],
    6: [170, 131, 131, 682, 553, 897, 979, 1224, 346, 973, 718, 1224, 718, 973, 131, 682]
    }

for option in range(1, 7):
    print('Option %s' % option)
    print('Decrypted letter numbers:', list(rsa(set_data[option])))
    decode(list(rsa(set_data[option])))

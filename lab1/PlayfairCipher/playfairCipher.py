import re

LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


class PlayfairCipher:
    @staticmethod
    def check_input(arg):
        if not isinstance(arg, str):
            raise TypeError(
                'The argument of the function should be an instance of `str`')

        if not all(i.isascii() & i.isprintable() for i in arg):
            raise ValueError(
                'The argument of the function should be a `str` containing only printable ASCII characters')

    @staticmethod
    def prepare(msg):
        msg = msg.upper().replace('J', 'I')
        PlayfairCipher.check_input(msg)
        msg = ''.join([i for i in msg if i.isalpha()])
        while msg:
            s = msg[:2]
            if len(set(s)) == 2 and s[-1] != 'X':
                msg = msg[2:]
            else:
                s = s[0] + 'X'
                msg = msg[1:]
            yield s

    def __init__(self, key):
        key = key.upper().replace('J', 'I')
        PlayfairCipher.check_input(key)
        key = ''.join(i for i in key if i.isalpha())
        self.square = list(dict.fromkeys(key + LETTERS))

    def locate(self, letter):
        letter = letter.upper()
        return list(divmod(self.square.index(letter), 5))

    def get_letter(self, pos):
        index = pos[0] * 5 + pos[1]
        return self.square[index]

    def transform(self, pair, move):
        p0, p1 = map(self.locate, pair)
        def roll(x): return (x + move) % 5
        for i in range(3):
            if i < 2 and p0[i] == p1[i]:
                j = 1 - i
                p0[j], p1[j] = map(roll, (p0[j], p1[j]))
                break
            if i == 2:
                p0[1], p1[1] = p1[1], p0[1]
        return ''.join(map(self.get_letter, (p0, p1)))

    def encrypt(self, msg):
        pairs = PlayfairCipher.prepare(msg)
        return ' '.join(self.transform(pair, 1) for pair in pairs)

    def decrypt(self, msg):
        msg = msg.upper()
        PlayfairCipher.check_input(msg)
        if not re.match(r'^([A-Z]{2}(\s)?)+$', msg):
            raise ValueError(
                "The inputted message isn't a valid Playfair cipher message")
        msg = re.findall('[A-Z]{2}', msg)
        def rule1(x): return x if x[1] != 'X' else x[0]
        return ' '.join(rule1(self.transform(s, -1)) for s in msg)

class writeFile:
    def writeFile(self, fileName, content):
        f = open(fileName, 'w')
        f.write(content)
        f.close()


file = writeFile()
cipher = PlayfairCipher("secret message")
with open('lab1/PlayfairCipher/input.txt') as text:
    text = text.read()

istring = cipher.encrypt(text)

# writing output to a file
file.writeFile("outputFile.txt", istring)

# checking the decrypt function
dstring = cipher.decrypt(istring)
file.writeFile('checkDecrypt.txt', dstring)



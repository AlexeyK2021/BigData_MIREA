morze = {'a': '.-', 'b': '-…', 'c': '-.-.', 'd': '-..',
         'e': '.', 'f': '..-.', 'g': '--.', 'h': '….',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
         'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
         'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
         'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..'}


def encrypt(msg):
    new_msg = ""
    for i in msg:
        new_msg += morze[i]
    return new_msg


if __name__ == "__main__":
    text = input().lower().split(" ")
    for word in text:
        print(encrypt(word))

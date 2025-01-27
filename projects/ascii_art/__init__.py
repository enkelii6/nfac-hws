CHARS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


def get_chars(chars):
    chars_lows_array = []

    for char in chars:
        chars_lows_array.append(CHARS.index(char) * 9)

    with open('standard.txt', 'r') as f:
        data = f.readlines()
        data.remove('\n')

    for i in range(9):
        data_to_print = ''
        for char in chars_lows_array:
            print(data_to_print)
            data_to_print += data[char + i]


get_chars('Hello')

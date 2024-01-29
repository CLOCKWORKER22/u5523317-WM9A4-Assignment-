def morse_translator(text):
    global morse_code_dict
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morse_code_dict[letter] + ' '
        else:
            cipher += '/ '
    return cipher

def main():
    morse_translator("")  # 调用以初始化 morse_code_dict
    message = "..." #在这里输入
    result = encrypt(message.upper())
    print(result)

if __name__ == '__main__':
    main()

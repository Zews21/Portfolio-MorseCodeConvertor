morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}


def convert_to(text):
    """Converts from normal text to Morse code"""
    end_text = ""
    for letter in text:
        if letter in morse_code_dict:
            end_text += morse_code_dict[letter] + " "
        else:
            letter = '/'
            end_text += letter

    print(end_text.strip())


def convert_from(text):
    """Converts from Morse code to normal text"""
    end_text = ""
    words = text.split(' /')

    for word in words:
        word_result = ""
        letters = word.split(' ')

        for letter in letters:
            for key, value in morse_code_dict.items():
                if letter == value:
                    word_result += key
        end_text += word_result + " "

    print(end_text.strip())


running = True
while running:

    convert_direction = input("Would you like to convert TO or FROM Morse code? Type TO / FROM: \n").upper()
    input_text = input("What message would you like to convert?: ").upper()

    if convert_direction == "TO":
        convert_to(input_text)

    elif convert_direction == "FROM":
        convert_from(input_text)

    else:
        print("Invalid input.")

    decision = input("Do you want to restart the program? Type 'yes' or 'no': \n\n").lower()
    if decision == "no":
        running = False
        print("\nThank you for using this program!")

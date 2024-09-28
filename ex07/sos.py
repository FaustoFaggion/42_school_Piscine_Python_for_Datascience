import sys

def main(argv):
    
    morse_code_dict = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
        "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
        "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
        "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
        "Z": "--..",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
        " ": "/"
    }
    try:
        if len(argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")

        words_collection = argv[1].split()
        for word in words_collection:
             if not word.isalpha():
                raise AssertionError("AssertionError: the arguments are bad .")
        
        text: str = argv[1].upper()
        new_text = ""
        for char in text:
            new_text = new_text + morse_code_dict[char] + " "
        print(new_text)
    except Exception as e:
        print(e)
    
    return 0

if __name__ == "__main__":
    main(sys.argv)
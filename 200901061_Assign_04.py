import threading

def input_func():
    global input_string
    try:
        input_string = str(input("Enter a string: "))
        print("\t  ___________________________________\n")
    except ValueError:
        input_string = ""
        print("\tThe string is empty. Try again.")
        input_string = str(input("Enter a valid string: "))
    return input_string

def reverse_func():
    print("\t=> Reversed Input String: ", input_string[::-1])

def capitalize_func():
    print("\t=> Capitalized Input String: ", input_string.upper())
    
def shift_func():
    shifted_string = ""
    for letter in input_string:
        if letter == " ":
            shifted_string += " "
        elif ord(letter) + 2 > ord("9") and letter.isdigit():
            shifted_string += chr(ord(letter) + 2 - 10)
        elif ord(letter) + 2 > ord("z") and letter.islower():
            shifted_string += chr(ord(letter) + 2 - 26)
        elif ord(letter) + 2 > ord("Z"):
            shifted_string += chr(ord(letter) + 2 - 26)
    print("\t=> +2 Character Shifted Input String: ", shifted_string, )
    print("\t  ___________________________________\n")
if __name__ == "__main__":
    Input_Thread = threading.Thread(target=input_func)
    Reverse_Thread = threading.Thread(target=reverse_func)
    Capital_Thread = threading.Thread(target=capitalize_func)
    Shift_Thread = threading.Thread(target=shift_func)

    Input_Thread.start()
    Input_Thread.join()

    Reverse_Thread.start()
    Reverse_Thread.join()

    Capital_Thread.start()
    Capital_Thread.join()

    Shift_Thread.start()
    Shift_Thread.join()
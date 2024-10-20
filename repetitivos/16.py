import os
os.system("cls")

class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        reversed_text = ""  
        index = len(self.text) - 1  

        while index >= 0:  
            reversed_text += self.text[index] 
            index -= 1  

        return reversed_text 

if __name__ == "__main__":
    text = "Hola, mundo!"
    reverser = StringReverser(text)
    inverted_text = reverser.reverse()
    print(f"Texto original: {text}")
    print(f"Texto invertido: {inverted_text}")
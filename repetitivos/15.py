import os
os.system("cls")

class StringConverter:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        uppercase_text = ""
        index = 0

        while index < len(self.text):
            char = self.text[index]
            if 'a' <= char <= 'z':
                uppercase_text += chr(ord(char) - 32)  
            else:
                uppercase_text += char  
            index += 1 

        return uppercase_text

    def to_lowercase(self):
        lowercase_text = ""
        index = 0

        while index < len(self.text):
            char = self.text[index]
            if 'A' <= char <= 'Z':
                lowercase_text += chr(ord(char) + 32) 
            else:
                lowercase_text += char  
            index += 1  

        return lowercase_text

if __name__ == "__main__":
    text = "Hola, Mundo!"
    converter = StringConverter(text)
    
    upper_text = converter.to_uppercase()
    lower_text = converter.to_lowercase()
    
    print(f"Texto original: {text}")
    print(f"Texto en mayúsculas: {upper_text}")
    print(f"Texto en minúsculas: {lower_text}")
class StringConverter:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        """Convierte la cadena a mayúsculas usando un bucle while."""
        uppercase_text = ""
        index = 0

        while index < len(self.text):
            char = self.text[index]
            # Convierte a mayúscula si es una letra minúscula
            if 'a' <= char <= 'z':
                uppercase_text += chr(ord(char) - 32)  # Convertir a mayúscula
            else:
                uppercase_text += char  # Mantener el carácter original
            index += 1  # Incrementa el índice

        return uppercase_text

    def to_lowercase(self):
        """Convierte la cadena a minúsculas usando un bucle while."""
        lowercase_text = ""
        index = 0

        while index < len(self.text):
            char = self.text[index]
            # Convierte a minúscula si es una letra mayúscula
            if 'A' <= char <= 'Z':
                lowercase_text += chr(ord(char) + 32)  # Convertir a minúscula
            else:
                lowercase_text += char  # Mantener el carácter original
            index += 1  # Incrementa el índice

        return lowercase_text

# Ejemplo de uso
if __name__ == "__main__":
    text = "Hola, Mundo!"
    converter = StringConverter(text)
    
    upper_text = converter.to_uppercase()
    lower_text = converter.to_lowercase()
    
    print(f"Texto original: {text}")
    print(f"Texto en mayúsculas: {upper_text}")
    print(f"Texto en minúsculas: {lower_text}")
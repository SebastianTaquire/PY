class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        """Invierte la cadena de texto utilizando un bucle while."""
        reversed_text = ""  # Cadena vacía para almacenar el resultado
        index = len(self.text) - 1  # Inicia desde el último índice

        while index >= 0:  # Mientras haya caracteres en la cadena
            reversed_text += self.text[index]  # Agrega el carácter actual
            index -= 1  # Decrementa el índice

        return reversed_text  # Devuelve la cadena invertida

# Ejemplo de uso
if __name__ == "__main__":
    text = "Hola, mundo!"
    reverser = StringReverser(text)
    inverted_text = reverser.reverse()
    print(f"Texto original: {text}")
    print(f"Texto invertido: {inverted_text}")
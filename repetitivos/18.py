class StringTrimmer:
    def __init__(self, text):
        self.text = text

    def ltrim(self):
        """Elimina los espacios en blanco del inicio de la cadena."""
        # Inicializa un índice para recorrer la cadena
        i = 0
        # Aumenta el índice mientras haya espacios en blanco al inicio
        while i < len(self.text) and self.text[i] == ' ':
            i += 1
        # Retorna la subcadena desde el índice i hasta el final
        return self.text[i:]

    def rtrim(self):
        """Elimina los espacios en blanco del final de la cadena."""
        # Inicializa un índice al final de la cadena
        i = len(self.text) - 1
        # Disminuye el índice mientras haya espacios en blanco al final
        while i >= 0 and self.text[i] == ' ':
            i -= 1
        # Retorna la subcadena desde el inicio hasta el índice i + 1
        return self.text[:i + 1]

    def alltrim(self):
        """Elimina los espacios en blanco del inicio y del final de la cadena."""
        # Usa ltrim para eliminar espacios del inicio
        trimmed_start = self.ltrim()
        # Usa rtrim para eliminar espacios del final
        trimmed_end = StringTrimmer(trimmed_start).rtrim()
        return trimmed_end

# Ejemplo de uso
if __name__ == "__main__":
    text = "   Hola, mundo!   "
    trimmer = StringTrimmer(text)

    print(f"Original: '{text}'")
    print(f"Ltrim: '{trimmer.ltrim()}'")
    print(f"Rtrim: '{trimmer.rtrim()}'")
    print(f"Alltrim: '{trimmer.alltrim()}'")
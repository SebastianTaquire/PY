import os
os.system("cls")

class StringTrimmer:
    def __init__(self, text):
        self.text = text

    def ltrim(self):
        i = 0
        while i < len(self.text) and self.text[i] == ' ':
            i += 1
        return self.text[i:]

    def rtrim(self):
        i = len(self.text) - 1
        while i >= 0 and self.text[i] == ' ':
            i -= 1
        return self.text[:i + 1]

    def alltrim(self):
        trimmed_start = self.ltrim()
        trimmed_end = StringTrimmer(trimmed_start).rtrim()
        return trimmed_end

if __name__ == "__main__":
    text = "   Hola, mundo!   "
    trimmer = StringTrimmer(text)

    print(f"Original: '{text}'")
    print(f"Ltrim: '{trimmer.ltrim()}'")
    print(f"Rtrim: '{trimmer.rtrim()}'")
    print(f"Alltrim: '{trimmer.alltrim()}'")
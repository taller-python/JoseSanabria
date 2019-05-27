'''It reads a word and it validates if word is a palindrome

Args:
    PALABRA (string): word to validate

Returns (print):
    resultado (string): Result of validate word (False or True)
      + word validate
'''

print("Ingrese Palabra: ")
PALABRA = input()
PALABRA_MAYUSCULA = PALABRA.upper()
if PALABRA_MAYUSCULA != PALABRA_MAYUSCULA[::-1]:
    print("False " + PALABRA)
else:
    print("True " + PALABRA)

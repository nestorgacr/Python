def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('{} sí es un palíndromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word))

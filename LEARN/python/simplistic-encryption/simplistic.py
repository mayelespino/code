#!/usr/bin/python
import sys
import string

def replace_character(character, replacement_alphabet):
    if character == ' ':
        return(' ')

    offset = string.ascii_lowercase.find(character.lower())
    if offset == -1:
        return('?')
    replaced_character = replacement_alphabet[offset]

    return(replaced_character)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Must provide a word and a file name:")
        exit(-1)

    key_word = sys.argv[1]
    file_name = sys.argv[2]
    alphabet = string.ascii_lowercase

    for letter in key_word:
        alphabet = alphabet.replace(letter, '')

    alphabet = key_word + alphabet

    print("\n\ncode word: {} file name{} coded alphabet: {}\n\n".format(key_word, file_name, alphabet))

    with open(file_name, 'r') as f:
        entire_file = f.readlines()

    replaced_file_text = ''
    for line in entire_file:
        for letter in line:
            replaced_file_text += replace_character(letter, alphabet)

    print("\nOriginal content of file:\n")
    print(entire_file)
    print("\nEncrypted content of file:\n")
    print(replaced_file_text)
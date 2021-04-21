import string
def is_pangram(sentence):
    alphabet_list = [chr(i) for i in range(ord('a'),ord('z')+1)]

    # would the below be better for performance?
    # alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in alphabet_list:
      if letter not in sentence.lower():
        return False

    return True
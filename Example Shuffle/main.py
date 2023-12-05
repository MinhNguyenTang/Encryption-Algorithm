import random

word = "Python"
letters = list(word)
random.shuffle(letters)
mixed = ''.join(letters)

print("Original:", word)
print("Mixed:", mixed)
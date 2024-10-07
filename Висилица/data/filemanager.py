import codecs
import random
import sys
import time

with codecs.open("data\words.txt","r","utf-8") as file:
    words = file.readlines()
    words = [i[:-2] for i in words]
    words = [i for i in words if not i.startswith("#")]

word = random.choice(words)
word = word.lower()
attempts = len(set(word))

word = list(word)
player_word = ["_"] * len(word)


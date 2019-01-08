#!/usr/bin/env python3
# -*- coding: utf-8 -*-

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in alphabet:
    count = alphabet.index(letter) + 1
    if count % 3 == 0 and count % 4 == 0:
        print(str(count) + letter.lower())
    elif count % 3 == 0:
        print(letter.lower())
    elif count % 4 == 0:
        print(count)
    else:
        print(letter)        

    
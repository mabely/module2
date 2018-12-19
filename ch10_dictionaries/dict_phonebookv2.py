# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:15:47 2018

@author: Mabel
"""

def main(phonebook):
    for name in range(1, 5):
        createPhonebook()
        print('\n-----PERSON', name, '-----')
        entries(phonebook)
    
    return phonebook

def createPhonebook():
    phonebook = {}
    return phonebook

def entries(phonebook):
    name = input('Name: ')
    phoneNo = input('Phone number: ')
    phonebook[name] = phoneNo
    return phonebook

def writeFile(phonebook):
    f = open('phonebook.txt', 'w+')
    f.write(str(phonebook))
    f.close()
    
phonebook = {}





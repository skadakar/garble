import json
import os
import random
import sys

def split(word):
    return [char for char in word]

alphanum = (split(str("abcdefghijklmnopqrstuvwxyz0123456789,.-! ")))
print("Valid characters:")
print(alphanum)
validnumbers = list(range(10, 100))
alphanumlen = alphanum.__len__()


def getkeys():
    with open('config/psk_keynames.txt', 'r') as file:
        data = file.read().rstrip()
        return data
psklist=()
psklist = getkeys()


guidlist = psklist.split(",")


def recreatekeys():
    for pskid in guidlist:
        makekey(pskid)


def makekey(keyname):
    randlist = random.sample(validnumbers, alphanumlen)
    key = randlist[0:(alphanumlen)]
    encryption_dict = dict(zip(alphanum, key))
    decryption_dict = dict(zip(key, alphanum))
    with open('psk-dump/' + keyname + 'dict_encrypt.txt', 'w') as outfile:
        json.dump(encryption_dict, outfile)
    with open('psk-dump/' + keyname + 'dict_decrypt.txt', 'w') as outfile:
        json.dump(decryption_dict, outfile)
    #print(encryption_dict, decryption_dict)
    return encryption_dict, decryption_dict

print("Creating keys:")
print(psklist)

recreatekeys()

print("Keys created!")
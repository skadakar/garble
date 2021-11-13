import json
import os
import random
import sys
import re

def split(word):
    return [char for char in word]



def getkeys():
    with open('config/otp_keynames.txt', 'r') as file:
        data = file.read().rstrip()
        return data
otplist=()
otplist = getkeys()


otplist = otplist.split(",")


def recreatekeys():
    for otpname in otplist:
        makekey(otpname)

def makekey(keyname):
    digits="0123456789"
    otpcontent=''.join(random.SystemRandom().choice(digits) for _ in range(240))
    otpcontent= (' ').join(re.findall('.{1,5}', otpcontent))
    print(keyname)
    print(otpcontent)
    with open('otp-dump/' + keyname + '_otp.txt', 'w') as outfile:
        json.dump(otpcontent, outfile)
    return otpcontent



print("Creating keys:")
recreatekeys()

print("Keys created! 5*6*8 240 numbers, 120character messages before repeat. ")
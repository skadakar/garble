import json
import os
import sys
import time
from operator import add
import numpy as np
from audioplayer import AudioPlayer


def split(word):
    return [char for char in word]


def listToString(s):
    # initialize an empty string
    string = ""

    # traverse in the string
    for element in s:
        string += element

        # return string
    return string


alphanum = (split(str("abcdefghijklmnopqrstuvwxyz")))
validnumbers = list(range(0, 26))
alphanumlen = alphanum.__len__()
lettermapping = dict(zip(alphanum, validnumbers))
print(lettermapping)


otp = sys.argv[1]
otpkey = sys.argv[2]
os.environ[otp] = otpkey


prefix = sys.argv[3]
prefixcontent = sys.argv[4]
os.environ[prefix] = prefixcontent

msg = sys.argv[5]
msgcontent = sys.argv[6]
os.environ[msg] = msgcontent

def split(word):
    return [char for char in word]

# Encrypt message
def encryptmsg(otpkey, msgcontent):
    optraw = open('otp-dump/' + otpkey + '_otp.txt', "r")
    optraw = json.load(optraw)
    splitmessage = split(msgcontent.lower())
    # Create the list of encrypted values to use
    encryptedlist = []
    for i in splitmessage:
        encryptedlist.append(lettermapping[i])
    encryptedlisttostring = ''.join(str(("{:02d}".format(e))) for e in encryptedlist)
    #Make encrypted list to blocks of two
    msglength = encryptedlisttostring.__len__()

    otpneed = str(optraw.replace(" ", ""))
    otplengt = otpneed.__len__()
    otpneed = otpneed[0:msglength]

    #Check for too long message.
    if msglength > otplengt:
        print("OTP too short to cover message")
        exit(0)

    encrypted_msg_str = listToString(encryptedlisttostring)
    encrypted_otp_str = listToString(otpneed)

    n = 2
    encrypted_msg_duo = [encrypted_msg_str[index: index + n] for index in range(0, len(encrypted_msg_str), n)]
    encrypted_msg_duo = map(int, encrypted_msg_duo)
    encrypted_msg_duo = list(encrypted_msg_duo)
    #print(encrypted_msg_duo)

    encrypted_otp_duo = [encrypted_otp_str[index: index + n] for index in range(0, len(encrypted_otp_str), n)]
    encrypted_otp_duo = map(int, encrypted_otp_duo)
    encrypted_otp_duo = list(encrypted_otp_duo)
    #print(encrypted_otp_duo)

    otpencryptedlist=np.add(encrypted_msg_duo, encrypted_otp_duo)
    mod100otpencryptedlist=[]
    #Mod 100 for n
    for n in np.array(otpencryptedlist):
        mod100otpencryptedlist.append(n % 100)

    otpencryptedmod100=[]
    otpencryptedmod100 = str(''.join(str(e) for e in mod100otpencryptedlist))
    
    # Split the encrypted message into individual numbers for sounds/vo to deal with
    encryptedtovo = split(otpencryptedmod100)

    return encryptedtovo


def sendmessage(prefixcontent, otpkey, msgcontent):
    print(otpkey)
    print("MSGCONTENT" + msgcontent)
    encryptedtovo = encryptmsg(otpkey, msgcontent)
    print("Starting intro")
    introfullpath = os.path.abspath('audio/otpintro.mp3')
    AudioPlayer(introfullpath).play(block=True)
    print("Prefix transfer")
    prefixsplitmessage = split(prefixcontent.lower())
    print(prefixsplitmessage)
    for l in prefixsplitmessage:
        numfullpath = os.path.abspath('vo/' + l + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
    print("Prefix transfered")
    time.sleep(0.1)

    print("Encrypted key transfer")
    for i, symbol in enumerate(encryptedtovo):
        numfullpath = os.path.abspath('vo/' + symbol + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
        print(symbol)
        i= i+1
        if i % 5 == 0: print("Five break")
        if i % 5 == 0: time.sleep(1.25)

    # Distinct break before code runs again slower
    time.sleep(0.1)
    print("Break")
    midfullpath = os.path.abspath('audio/otpmid.mp3')
    AudioPlayer(midfullpath).play(block=True)

    print("Prefix slow transfer")
    prefixsplitmessage = split(prefixcontent.lower())
    print(prefixsplitmessage)
    for l in prefixsplitmessage:
        numfullpath = os.path.abspath('vo-slow/' + l + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
    print("Prefix slowly transfered")

    print("Encrypted key transfer 80% speed")
    for i, symbol in enumerate(encryptedtovo):
        numfullpath = os.path.abspath('vo-slow/' + symbol + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
        #This gives us a 0.75 second break every five character.
        i = i + 1
        if i % 5 == 0: print("Five break")
        if i % 5 == 0: time.sleep(1.25)

    time.sleep(0.1)

    print("Slow transfer complete")
    endfullpath = os.path.abspath('audio/otpend.mp3')
    AudioPlayer(endfullpath).play(block=True)

sendmessage(prefixcontent, otpkey, msgcontent)


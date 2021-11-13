import json
import os
import sys
import time
from audioplayer import AudioPlayer

psk = sys.argv[1]
pskkey = sys.argv[2]
os.environ[psk] = pskkey

msg = sys.argv[3]
msgcontent = sys.argv[4]
os.environ[msg] = msgcontent


def split(word):
    return [char for char in word]

# Encrypt message
def encryptmsg(pskkey, msgcontent):
    encryption_dict_data = open('psk-dump/' + pskkey + 'dict_encrypt.txt', "r")
    encryption_dict = json.load(encryption_dict_data)
    splitmessage = split(msgcontent.lower())

    # Create the list of encrypted values to use
    encryptedlist = []
    for i in splitmessage:
        encryptedlist.append(encryption_dict[i])

    encryptedlisttostring = ''.join(str(e) for e in encryptedlist)
    mergedencrytpedmessage = str(pskkey) + encryptedlisttostring

    # Split the encrypted message into individual numbers for sounds/vo to deal with
    encryptedtovo = split(mergedencrytpedmessage)
    return encryptedtovo


def sendmessage(pskkey, msgcontent):
    encryptedtovo = encryptmsg(pskkey, msgcontent)
    print(encryptedtovo)
    print("Starting intro")
    introfullpath = os.path.abspath('audio/pskintro.mp3')
    AudioPlayer(introfullpath).play(block=True)

    time.sleep(0.1)
    print("Encrypted key transfer")
    for i, symbol in enumerate(encryptedtovo):
        numfullpath = os.path.abspath('vo/' + symbol + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
        # This gives us a 0.75 second break every five character.
        i= i+1
        if i % 5 == 0: print("Five break")
        if i % 5 == 0: time.sleep(1.25)

    # Distinct break before code runs again slower
    time.sleep(0.1)
    print("Break")
    midfullpath = os.path.abspath('audio/pskmid.mp3')
    AudioPlayer(midfullpath).play(block=True)

    print("Encrypted key transfer 80% speed")
    for i, symbol in enumerate(encryptedtovo):
        numfullpath = os.path.abspath('vo-slow/' + symbol + '.mp3')
        AudioPlayer(numfullpath).play(block=True)
        #This gives us a 0.75 second break every five character.
        i = i + 1
        if i % 5 == 0: print("Five break")
        if i % 5 == 0: time.sleep(1.25)

    time.sleep(0.1)

    print("Transfer complete")
    endfullpath = os.path.abspath('audio/pskend.mp3')
    AudioPlayer(endfullpath).play(block=True)
sendmessage(pskkey, msgcontent)


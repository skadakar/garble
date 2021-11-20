import subprocess
import json
import os
import random
import re
import string
import sys
import time

import numpy as np
from audioplayer import AudioPlayer


def garble_help():
    print("See docs: https://github.com/skadakar/garble")
    print("Usage:")
    print("--send \"message here\"  --otp \"name of otp\" --prefix \"prefix numbers\"")
    print("--send \"message here\"  --psk \"name of otp\" --prefix \"prefix numbers\"")
    print("Example:")
    print("python garble.py --send \"This is my message\" --otp \"003\" --prefix \"1003\"")
    print("Note: Max 5 numbers in prefix")
    print("")
    print("To generate new keys use keygen, note that this will overwrite existing keys defined in the config folder.")
    print("--keygen --otp")
    print("--keygen --psk")
    print("")
    print("   _____ _   _ ______ _  ____          ________ _____  _  __ _____")
    print("  / ____| \ | |  ____| |/ /\ \        / /  ____|  __ \| |/ // ____|")
    print(" | (___ |  \| | |__  | ' /  \ \  /\  / /| |__  | |__) | ' /| (___")
    print("  \___ \| . ` |  __| |  <    \ \/  \/ / |  __| |  _  /|  <  \___ \\")
    print("  ____) | |\  | |____| . \    \  /\  /  | |____| | \ \| . \ ____) |")
    print(" |_____/|_| \_|______|_|\_\    \/  \/   |______|_|  \_\_|\_\_____/ ")
    print("")
    return


def wait():
    time.sleep(0.1)
    return


def list_to_duo_string(list: list[int]):
    duostring: str = ''.join(str(("{:02d}".format(e))) for e in list)
    return duostring


def otp_message_to_list(message: str):
    otp_message_list = []
    for i in message:
        otp_message_list.append(otplettermapping[i])
    return otp_message_list


def single_split(string: str):
    return [char for char in string]


def duo_split(inputstring: str):
    if len(inputstring) % 2 == 0:
        duo = [inputstring[index: index + 2] for index in range(0, len(inputstring), 2)]
        duo = map(int, duo)
        duo = list(duo)
        return duo
    else:
        print("Mod 2 failure, check your duo list")
        exit(0)


def mod100_list(inputlist: list[int]):
    mod100list = []
    for n in np.array(inputlist):
        mod100list.append(n % 100)
    return mod100list


def list_to_string(list: list):
    string: str = ""
    for element in list:
        string += element
    return string


def play(path: str, sound: str):
    soundfullpath = os.path.abspath(path + '/' + sound + '.mp3')
    AudioPlayer(soundfullpath).play(block=True)


def playstring(path: str, string: str):
    print("Playing sounds in increments of five.")
    print(string)
    for i, character in enumerate(string):
        play(path, character)
        i = i + 1
        if i % 5 == 0:
            print("Break five.")
            time.sleep(1.25)


def get_pskkeys():
    with open('config/psk_keynames.txt', 'r') as file:
        data = file.read().rstrip()
        return data


def get_otpkeys():
    with open('config/otp_keynames.txt', 'r') as file:
        data = file.read()
        data = data.split(",")
        return data


def remove_old_keys(type: str, name: str):
    if os.path.isfile("keys-" + type + "/" + name + ".key"):
        os.remove("keys-" + type + "/" + name + ".key")
    return


def generate_psk(keyname: str):
    remove_old_keys("psk", keyname)
    randlist = random.sample(pskvalidnumbers, pskalphanumlen)
    key = randlist[0:(pskalphanumlen)]
    encryption_dict = dict(zip(pskcharacterlist, key))
    decryption_dict = dict(zip(key, pskcharacterlist))
    with open('keys-psk/' + keyname + 'dict_encrypt.txt', 'w') as outfile:
        json.dump(encryption_dict, outfile)
    with open('keys-psk/' + keyname + 'dict_decrypt.txt', 'w') as outfile:
        json.dump(decryption_dict, outfile)
    return


def generate_otp(keyname: str):
    remove_old_keys("otp", keyname)
    otpcontent = ''.join(random.SystemRandom().choice(num) for _ in range(240))
    otpcontent = (' ').join(re.findall('.{1,5}', otpcontent))
    otpcontent = re.sub("(.{36})", "\\1\n", otpcontent, 0, re.DOTALL)
    file = open("keys-otp/" + keyname + ".key", "w")
    for line in otpcontent.splitlines():
        file.write(line + "\n")
    return


def ingest_playlist():
    my_file = open("config/playlist.txt", "r")
    content_list = my_file.readlines()
    return content_list


def ingest_psk(name):
    data = open('keys-psk/' + name + 'dict_encrypt.txt', "r")
    data = json.load(data)
    return data


def prefix_to_list(prefixtext: str):
    prefixtext = str.strip(prefixtext)
    prefixtextlist = single_split(prefixtext)

    return prefixtextlist


def encrypt_psk(key, message):
    encryptedlist = []
    for i in single_split(message.lower()):
        encryptedlist.append(ingest_psk(key)[i])
    encrypted_psk_string = single_split((''.join(str(e) for e in encryptedlist)))
    encrypted_psk_string = list_to_string(encrypted_psk_string)
    return encrypted_psk_string


def ingest_otpkeys(name):
    with open('keys-otp/' + name + '.key', 'r') as file:
        data = file.read()
        data = re.sub(r"[\n\t\s]*", "", data)
        return data


def encrypt_otp(otp: str, message: str):
    otp_len_need = message.__len__() * 2
    otpstring = ingest_otpkeys(otp)

    # Check to see if we have enough OTP to go around.
    if message < otpstring:
        print("OTP too short to cover message")
        exit(0)

    # Getting just the part of the OTP we need.
    otpstringcut = otpstring[0:otp_len_need]

    duo_msg_string = list_to_duo_string(otp_message_to_list(message))
    # Generate lists for encrypting
    duo_msg = duo_split(duo_msg_string)
    duo_otp = duo_split(otpstringcut)

    # Do the OTP encryption:
    otpencryptedlist = np.add(duo_msg, duo_otp)

    # Mod 100 the new list:
    otpencryptedlist = mod100_list(otpencryptedlist)

    # Create final string
    finalstring = ''.join(str(("{:02d}".format(e))) for e in otpencryptedlist)

    print(finalstring)
    return finalstring


def rotate_otp_keys():
    for name in list(get_otpkeys()):
        generate_otp(name)
    print("All OTP keys replaced")


def rotate_psk():
    for name in list(get_otpkeys()):
        generate_psk(name)
    print("All PSKs replaced")

def rotencodechar(char,rotlevel):

    #Flyttet inn i rot13encodechar siden det ikke trenger være global
    upper = [*string.ascii_uppercase]
    lower = [*string.ascii_lowercase]

    if char in upper:
        charshift =  ((upper.index(char)) + int(rotlevel)) % len(upper)
        newchar = upper[charshift]
        return newchar
    if char in lower:
        charshift =  ((lower.index(char)) + int(rotlevel)) % len(lower)
        newchar = lower[charshift]
        return newchar
    else:
        return char


def rot(rotlevel,string):
    finalstring =""
    for char in string:
        finalstring += (rotencodechar(char, rotlevel))
    return finalstring

# OTP EN Specific variables, RU might be something for the future.
otpcharacterlist = single_split(string.ascii_lowercase)
otpvalidnumbers = list(range(0, len(otpcharacterlist)))
otplettermapping = dict(zip(otpcharacterlist, otpvalidnumbers))
num: list = single_split("0123456789")

# PSK Specific variables.
pskcharacterlist = single_split(string.ascii_lowercase + "0123456789,.-! ")
pskvalidnumbers = list(range(10, 100))
pskalphanumlen = pskcharacterlist.__len__()

prefix=None
# rotate_psk()
# rotate_otp_keys
# send_otp_message
# send_psk_message

def send_otp_message(message, otp_key, prefix):
    # Play intro
    play("audio", "otpintro")
    wait()
    # Play prefix
    playstring("vo", prefix_to_list(prefix))
    wait()
    # Play message
    playstring("vo", encrypt_otp(otp_key, message))
    wait()
    # Play pause music
    play("audio", "otpmid")
    # Re-play prefix
    playstring("vo", prefix_to_list(prefix))
    wait()
    # Re-play message
    playstring("vo-slow", encrypt_otp(otp_key, message))
    # Play exit
    play("audio", "otpend")
    return


def send_psk_message(message,psk_key, prefix="_"):
    # Play intro
    play("audio", "pskintro")
    wait()
    # Play prefix
    playstring("vo", prefix_to_list(prefix))
    wait()
    # Play message
    playstring("vo", encrypt_psk(psk_key, message))
    wait()
    # Play pause music
    play("audio", "pskmid")
    # Re-play prefix
    playstring("vo", prefix_to_list(prefix))
    wait()
    # Re-play message
    playstring("vo-slow", encrypt_psk(psk_key, message))
    # Play exit
    play("audio", "pskend")
    return

def send_rot_message(message,rot_num, prefix="_"):
    # Play intro
    play("audio", "rotintro")
    wait()
    # Play prefix
    playstring("vaz09", prefix_to_list(prefix))
    wait()
    # Play message
    tmpstr = rot(rot_num,message)
    playstring("vaz09", tmpstr)
    wait()
    # Play pause music
    play("audio", "rotmid")
    # Re-play prefix
    playstring("vaz09", prefix_to_list(prefix))
    wait()
    # Re-play message
    playstring("vaz09", rot(rot_num, message))
    # Play exit
    play("audio", "rotend")
    return

def autoplaylist():
    waittime = list(range(3, 17 ))
    commands = ingest_playlist()
    options=list(range(0, commands.__len__()))
    on = True
    while on == True:
        thiswait = (random.sample(waittime, 1))
        nexttask = (random.sample(options, 1))
        commandcall = commands[nexttask[0]]
        print("Waiting for " + str(thiswait[0]) + " minutes before doing:")
        print(commandcall)
        time.sleep(thiswait[0] * 60)
        subprocess.call(commandcall)
        print("Done, starting over.")
#tmpstr = rot(13,"hei")
#playstring("vaz09", tmpstr)
#send_rot_message("hei",13)
sysarglength = len(sys.argv)



if sys.argv[1] == str("--send"):
    if sys.argv[3] == str("--rot"):
        if len(sys.argv) > 5:
            print(len(sys.argv))
            send_rot_message(sys.argv[2], sys.argv[4], sys.argv[6])
            exit(0)
        else:
            send_rot_message(sys.argv[2], sys.argv[4])
            exit(0)
    if sys.argv[3] == str("--psk"):
        if sys.argv[5] == str("--prefix"):
            send_psk_message(sys.argv[2], sys.argv[4], sys.argv[6])
            exit(0)
        else:
            send_psk_message(sys.argv[2], sys.argv[4])
            exit(0)
    if sys.argv[3] == str("--otp"):
        if sys.argv[5] == str("--prefix"):
            send_otp_message(sys.argv[2], sys.argv[4], sys.argv[6])
            exit(0)
        else:
            send_otp_message(sys.argv[2], sys.argv[4])
        exit(0)

if sys.argv[1] == str("--keygen"):
    if sys.argv[2] == str("--otp"):
        rotate_otp_keys()
        exit()
    if sys.argv[2] == str("--psk"):
        rotate_psk()
        exit()
    exit(0)

if sys.argv[1] == str("--keygen"):
    if sys.argv[2] == str("--otp"):
        rotate_otp_keys()
        exit(0)
    if sys.argv[2] == str("--psk"):
        rotate_psk()
        exit()
    exit(0)
if sys.argv[1] == str("--autoplaylist"):
    autoplaylist()

if sysarglength <= 2:
    garble_help()
    exit(0)

if sys.argv[1] == str("--help"):
    garble_help()
    exit(0)


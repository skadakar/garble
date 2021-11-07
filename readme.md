vo contains audiofiles to be used 

psk.txt - first five characters is the name of the PSK, the rest is the actual code. 
Five characters followed by 95 numbers

message.txt contains the message that will be sendt
Prefix message with PSK, max 35 characters including spaces. 100 characters max length on file.

encrypt.py takes message.txt and encrypts with the PSK above.

makemessage.py creates a new wav file based on the encrypted-message.txt and the adio files available

sendmessage.py sends the created message over 446 radio

decode.py to verify decoded messages. 

# GARBLE

Numberstation supporting Vigenere, PSK and OTP based data encryption over radio with speech synthesized audio.  
You have the option to add prefix to your encoded message, to let people know what PSK or OTP is being used by setting the --prefix variable.

### Autoplaylist:  
Will run a random command from /config/playlist.txt at a random interval between 3-21 minutes. 

### Encryptions:
OTP is limited to "abcdefghijklmnopqrstuvwxyz"  
PSK is limited to "abcdefghijklmnopqrstuvwxyz0123456789 ,.-!"  
ROT is limited to "abcdefghijklmnopqrstuvwxyz0123456789"  
VIG is limited to "abcdefghijklmnopqrstuvwxyz"  

Not true random, cannot be trusted for anything outside of fun and games. 
  

## Usage  
```
--send "thistext"  --otp "name of otp" --prefix "prefix numbers"  
```
```
--send "thistext"  --psk "name of psk" --prefix "prefix numbers"  
```
```
--send "thistext"  --vig "keyword" --prefix "_"  
```
```
--send "thistext"  --rot <number> --prefix "prefix numbers"  
```
```
--autoplaylist
```
  
## To generate new keys use keygen, note that this will overwrite existing keys defined in the config folder.  
```
--keygen --otp  
```
```
--keygen --psk  
```  

   
   
## OTP Examples:
   ``` 
   python garble.py --send "thisismymessage" --otp "003" --prefix "1003"  
   ```
   ```
   python garble.py --send "thisismymessage" --otp "003"
   ```
   Decoding guide:
   
   ![alt text](https://github.com/skadakar/garble/blob/main/otp-manual.png?raw=true)
   

   
## PSK Examples:
   ```
   python garble.py --send "this is my message!" --psk "003" --prefix "1003"  
   ```
   ```
   python garble.py --send "This is my message!" --psk "003"
   ```
## ROT Examples: 
  ``` 
   python garble.py --send "thisismymessage" --rot 13 --prefix "rot13"  
   ```
   ```
   python garble.py --send "thisismymessage" --rot 13
   ```   
## VIG Examples: 
  ``` 
   python garble.py --send "thisismymessage" --vig "januar" --prefix "vig"  
   ```
   ```
   python garble.py --send "thisismymessage" --vig "januar"
   ```   
  
## Video examples   
   
   OTP: https://www.youtube.com/watch?v=2DjWeM7rUh4
   
   PSK: https://www.youtube.com/watch?v=z63h6zclol0
   
   
   
   
   
   
   
   
   

```
   _____ _   _ ______ _  ____          ________ _____  _  __ _____ 
  / ____| \ | |  ____| |/ /\ \        / /  ____|  __ \| |/ // ____|
 | (___ |  \| | |__  | ' /  \ \  /\  / /| |__  | |__) | ' /| (___  
  \___ \| . ` |  __| |  <    \ \/  \/ / |  __| |  _  /|  <  \___ \ 
  ____) | |\  | |____| . \    \  /\  /  | |____| | \ \| . \ ____) |
 |_____/|_| \_|______|_|\_\    \/  \/   |______|_|  \_\_|\_\_____/ 
```

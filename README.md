# GARBLE

Numberstation supporting PSK and OTP based data encryption over radio.

| Script | Function | Variables
|---|---|---|
|psk_sendmsg.py|Sends a message with the selected key| --psk <your selected key> --msg <"Your text here">|
|psk_keygen.py|Creates new keys and dictionaries based on the /config/psk_keynames.txt |
|otp_keygen.py|Creates new OTPs based on the /config/otp_keynames.txt| 
|otp_sendmsg.py| Sends a message encrypted with selected OTP| --prefix <if you want to prefix your message with something, replace with "_" to not have one> --otp <otp to be used for encryption>  --msg <The message you want to send, a-z>
   
   
# OTP Examples:
   ``` 
   python .\otp_sendmsg.py --otp 123456  --prefix "_" --msg "asd"
   ```
   ```
   python .\otp_sendmsg.py --otp 123456  --prefix "12345" --msg "asd"
   ```
   ![alt text](https://github.com/skadakar/garble/blob/main/otp-manual.png?raw=true)
   

   
# PSK Examples:
   ```
   python .\psk_sendmsg.py --psk 30848 --msg "This is a test string"
   ```
   
# Video examples   
   
   PSK: https://www.youtube.com/watch?v=z63h6zclol0
   
   OTP: https://www.youtube.com/watch?v=2DjWeM7rUh4
   
   
   
   
   
   
   

```
   _____ _   _ ______ _  ____          ________ _____  _  __ _____ 
  / ____| \ | |  ____| |/ /\ \        / /  ____|  __ \| |/ // ____|
 | (___ |  \| | |__  | ' /  \ \  /\  / /| |__  | |__) | ' /| (___  
  \___ \| . ` |  __| |  <    \ \/  \/ / |  __| |  _  /|  <  \___ \ 
  ____) | |\  | |____| . \    \  /\  /  | |____| | \ \| . \ ____) |
 |_____/|_| \_|______|_|\_\    \/  \/   |______|_|  \_\_|\_\_____/ 
```

# GARBLE

Numberstation supporting PSK and OTP based data encryption over radio.

| Script | Function | Variables
|---|---|---|
|psk_sendmsg.py|Sends a message with the selected key| --psk <your selected key> --msg <"Your text here">|
|psk_keygen.py|Creates new keys and dictionaries based on the /config/psk_keynames.txt |
|otp_keygen.py|Creates new OTPs based on the /config/otp_keynames.txt| 
|otp_sendmsg.py| Sends a message encrypted with selected OTP| --prefix <if you want to prefix your message with something> --otp <otp to be used for encryption>  --msg <The message you want to send, a-z>
   
   
   
   
   
   

```
   _____ _   _ ______ _  ____          ________ _____  _  __ _____ 
  / ____| \ | |  ____| |/ /\ \        / /  ____|  __ \| |/ // ____|
 | (___ |  \| | |__  | ' /  \ \  /\  / /| |__  | |__) | ' /| (___  
  \___ \| . ` |  __| |  <    \ \/  \/ / |  __| |  _  /|  <  \___ \ 
  ____) | |\  | |____| . \    \  /\  /  | |____| | \ \| . \ ____) |
 |_____/|_| \_|______|_|\_\    \/  \/   |______|_|  \_\_|\_\_____/ 
```

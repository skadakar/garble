# GARBLE

Numberstation supporting PSK and OTP based data encryption over radio with speech synthesized audio.  
Not true random, cannot be trusted for anything outside of fun and games. 


## Usage  
```
--send "message here"  --otp " --OTP "name of otp" --prefix "prefix numbers"  
```
```
--send "message here"  --psk " --psk "name of otp" --prefix "prefix numbers"  
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
   python garble.py --send "This is my message" --otp "003" --prefix "1003"  
   ```
   ```
   python garble.py --send "This is my message" --otp "003"
   ```
   Decoding guide:
   
   ![alt text](https://github.com/skadakar/garble/blob/main/otp-manual.png?raw=true)
   

   
## PSK Examples:
   ```
   python garble.py --send "This is my message" --psk "003" --prefix "1003"  
   ```
   ```
   python garble.py --send "This is my message" --psk "003"
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

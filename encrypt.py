import cv2
import os
import string
import numpy as np
import hashlib

def encrypt_message():
    image_path = input("Enter the image path (jpg/png): ")
    img = cv2.imread(image_path)
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    password_hash = hashlib.md5(password.encode()).digest()[:8]

    d = {chr(i): i for i in range(255)}
    msg_length = len(msg)

    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    for i in range(8):
        img[n, m, z] = password_hash[i]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    height = img.shape[0] - 1
    img[height, 0, 0] = msg_length
    
    output_path = "encrypted_image.png"
    cv2.imwrite(output_path, img)
    print(f"Encrypted image saved as: {output_path}")
    print(f"Password for decryption: {password}")
    print("Note: Encrypted image is saved as PNG to preserve data integrity.")

    os.startfill(output_path)

if __name__ == "__main__":
    encrypt_message()

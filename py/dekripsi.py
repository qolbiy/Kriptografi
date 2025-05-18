# decrypt_from_qr.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import cv2

def decrypt_text(encrypted_text, key):
    try:
        raw = base64.b64decode(encrypted_text)
        iv = raw[:16]
        ct = raw[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return pt
    except Exception as e:
        return f"[!] Dekripsi gagal: {str(e)}"

def read_qr_code_image(filename):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return data

def main():
    key = b'ThisIsASecretKey'  # 16-byte key
    filename = input("Masukkan nama file QR Code (misal: encrypted_qr.png): ")
    encrypted_text = read_qr_code_image(filename)
    print(f"[i] Data terenkripsi dari QR:\n{encrypted_text}")
    decrypted = decrypt_text(encrypted_text, key)
    print(f"[✔] Teks setelah dekripsi:\n{decrypted}")

if __name__ == "__main__":
    main()

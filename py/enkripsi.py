# encrypt_to_qr.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64
import qrcode

def encrypt_text(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = cipher.iv
    encrypted = base64.b64encode(iv + ct_bytes).decode('utf-8')
    return encrypted

def generate_qr_code(data, filename="encrypted_qr.png"):
    qr = qrcode.QRCode(
        version=1, box_size=10, border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"[✔] QR Code disimpan sebagai '{filename}'")

def main():
    key = b'ThisIsASecretKey'  # 16-byte key
    text = input("Masukkan teks yang ingin dienkripsi: ")
    encrypted_text = encrypt_text(text, key)
    print(f"[i] Teks terenkripsi:\n{encrypted_text}")
    generate_qr_code(encrypted_text)

if __name__ == "__main__":
    main()

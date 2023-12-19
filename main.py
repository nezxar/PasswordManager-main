import base64
import hashlib
import tkinter as tk
from tkinter import ttk
import tkinter
import tkinter.messagebox as tkm
import tkinter.font as tkFont
import sqlite3
from view_table import View
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES3, AES

LOGIN_PASS = "123" # User password
DEF_BG = "#363636" # Defualt Backgroud color

def create_database():
    conn = sqlite3.connect("nizar_database.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT,
            email TEXT,
            site_name TEXT,
            encryption_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user_data(password, email, site_name, encryption_type):
    conn = sqlite3.connect("nizar_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO user_info (password, email, site_name, encryption_type) VALUES (?, ?, ?, ?)",
              (password, email, site_name, encryption_type))
    conn.commit()
    conn.close()

def aes_encrypt(data, key):
    key_hash = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key_hash, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

def encrypt_data(data, encryption_type, shift=3):
    if encryption_type == "RSA":
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(data.encode())
        encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
        return encrypted_data
    elif encryption_type == "Caesar":
        return caesar_encrypt(data, shift)
    elif encryption_type == "DES":
        key = b'mysecretpassword'
        cipher = DES3.new(key, DES3.MODE_ECB)
        padded_data = data.encode().ljust(8)
        ciphertext = cipher.encrypt(padded_data)
        return base64.b64encode(ciphertext).decode('utf-8')
    elif encryption_type == "AES":
        return aes_encrypt(data, "770079778")  # قم بتغيير "your_aes_key" إلى المفتاح الخاص بك
    elif encryption_type == "3DES":  # تمت إضافة هذا الجزء لدعم 3DES
        key = b'mysecretpassword'
        cipher = DES3.new(key, DES3.MODE_ECB)
        padded_data = data.encode().ljust(8)
        ciphertext = cipher.encrypt(padded_data)
        return base64.b64encode(ciphertext).decode('utf-8')
    else:
        return "Unsupported Encryption Type"

def caesar_encrypt(data:str, shift:int):
    result = ""
    for char in data:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def show_first_interface():
    login_frame.pack_forget()
    first_frame.pack()

def show_second_interface():
    first_frame.pack_forget()
    second_frame.pack()

def show_third_interface():
    second_frame.pack_forget()
    third_frame.pack()

def show_fourth_interface():
    third_frame.pack_forget()
    fourth_frame.pack()
    fetch_user_data()

def encrypt_and_show_third_interface():
    password = password_entry_second.get()
    email = email_entry_second.get()
    site_name = site_name_entry_second.get()
    encryption_type = encryption_type_combobox_second.get()

    encrypted_password = encrypt_data(password, encryption_type)
    encrypted_email = encrypt_data(email, encryption_type)
    encrypted_site_name = encrypt_data(site_name, encryption_type)

    insert_user_data(encrypted_password, encrypted_email, encrypted_site_name, encryption_type)

    show_third_interface()

def validate_password():
    entered_password = password_entry_third.get()
    if entered_password == "":
        tkm.showwarning("تحذير","يرجى إدخال كلمة المرور")
    elif entered_password == "123":
        show_fourth_interface()
    else:
        tkm.showerror("خطأ", "كلمة المرور غير صحيحة")
        # status_label_third.config(text="كلمة المرور غير صحيحة")

def validate_login_password():
    if pin_login.get() == "":
        tkm.showwarning("تحذير","يرجى إدخال كلمة المرور")
    elif pin_login.get() == LOGIN_PASS:
        show_first_interface()
    else:
        tkm.showerror("خطأ","كلمة المرور غير صحيحة")

def fetch_user_data():
    conn = sqlite3.connect("nizar_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user_info")
    data = c.fetchall()
    View(table_frame)

root = tk.Tk()
root.title("تطبيق نزار لإدارة كلمات المرور")

create_database()

arabic_font = tkFont.Font(family="Times New Roman", size=14)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

root.configure(bg=DEF_BG)

first_frame = tk.Frame(root, bg=DEF_BG)

welcome_text = "مرحبًا بك في تطبيق نزار\n" \
               "للبدء في تخزين وإدارة كلمات المرور الخاصة بك بشكل آمن\n اضغط 'بدء' أدناه."

login_frame = tk.Frame(root, bg=DEF_BG)
login_mess = "مرحبًا بك في تطبيق نزار\nيرجى تسجيل الدخول"
login_lable = tk.Label(login_frame, text=login_mess
                       ,font=(arabic_font.actual("family"), "17"), bg=DEF_BG, fg="white", padx=20, pady=20, anchor='e')
pin_lable = tk.Label(login_frame,text="ادخل كلمة المرور", bg=DEF_BG, fg="white", font=("Arial", 14))
pin_login = tk.Entry(login_frame, show="*", font=("Arial", 14))
submit_login = tk.Button(login_frame, text="دخول", font=("Arial", 14), bg=DEF_BG, fg="white", padx=20, pady=20, command=validate_login_password)

welcome_label = tk.Label(first_frame, text=welcome_text,
                         font=(arabic_font.actual("family"), "17"), bg=DEF_BG, fg="white", padx=20, pady=20, anchor='e')

start_button = tk.Button(first_frame, text="بدء", command=show_second_interface, font=("Arial", 16), bg="#404040", fg="white")

welcome_label.pack(pady=50)
start_button.pack(pady=20)

second_frame = tk.Frame(root, bg=DEF_BG)

info_label_second = tk.Label(second_frame, text="ادخل الإيميل وكلمة المرور واسم الموقع للتشفير",
                             font=("Arial", 16), bg=DEF_BG, fg="white")
info_label_second.pack(pady=10)

password_label_second = tk.Label(second_frame, text="كلمة المرور:", font=("Arial", 16), bg=DEF_BG, fg="white")
password_entry_second = tk.Entry(second_frame, show="*", font=("Arial", 14))
email_label_second = tk.Label(second_frame, text="البريد الإلكتروني:", font=("Arial", 16), bg=DEF_BG, fg="white")
email_entry_second = tk.Entry(second_frame, font=("Arial", 14))
site_name_label_second = tk.Label(second_frame, text="اسم الموقع أو التطبيق:", font=("Arial", 16), bg=DEF_BG, fg="white")
site_name_entry_second = tk.Entry(second_frame, font=("Arial", 14))
encryption_type_label_second = tk.Label(second_frame, text="نوع التشفير المستخدم", font=("Arial", 16), bg=DEF_BG, fg="white")
encryption_types = ["RSA", "Caesar", "DES", "AES", "3DES"]
encryption_type_combobox_second = ttk.Combobox(second_frame, values=encryption_types, font=("Arial", 14))

encrypt_button_second = tk.Button(second_frame, text="تشفير والانتقال", command=encrypt_and_show_third_interface,
                                  font=("Arial", 16), bg="#404040", fg="white")

info_label_second.pack(pady=10)
password_label_second.pack(pady=10)
password_entry_second.pack(pady=10)
email_label_second.pack(pady=10)
email_entry_second.pack(pady=10)
site_name_label_second.pack(pady=10)
site_name_entry_second.pack(pady=10)
encryption_type_label_second.pack(pady=10)
encryption_type_combobox_second.pack(pady=10)
encrypt_button_second.pack(pady=20)
login_lable.pack(pady=20)
pin_lable.pack(pady=10)
pin_login.pack(pady=10)
submit_login.pack(pady=20)

third_frame = tk.Frame(root, bg=DEF_BG)

info_label_third = tk.Label(third_frame, text="لعرض الإيميلات وكلمات المرور المخزنة أدخل كلمة المرور الرئيسية للتطبيق",
                            font=("Arial", 16), bg=DEF_BG, fg="white")
info_label_third.pack(pady=10)

password_label_third = tk.Label(third_frame, text="كلمة المرور:", font=("Arial", 16), bg=DEF_BG, fg="white")
password_entry_third = tk.Entry(third_frame, show="*", font=("Arial", 14))
validate_button_third = tk.Button(third_frame, text="التحقق والانتقال", command=validate_password,
                                  font=("Arial", 16), bg="#404040", fg="white")
# status_label_third = tk.Label(third_frame, text="", font=("Arial", 12), bg=DEF_BG, fg="red")

password_label_third.pack(pady=10)
password_entry_third.pack(pady=10)
validate_button_third.pack(pady=20)
# status_label_third.pack(pady=10)

fourth_frame = tk.Frame(root, bg=DEF_BG, width=200, height=300)

info_label_fourth = tk.Label(fourth_frame, text="مخزن البيانات وكلمات المرور", font=("Arial", 18), bg=DEF_BG, fg="white")
info_label_fourth.pack(pady=10)

table_frame = tk.Frame(fourth_frame, height=150, width=200, bg=DEF_BG)
# fetch_button_fourth = tk.Button(fourth_frame, text="احضار البيانات", command=fetch_user_data,
#                                 font=("Arial", 16), bg="#404040", fg="white")


table_frame.pack(pady=20)
# fetch_button_fourth.pack(pady=20)

login_frame.pack()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

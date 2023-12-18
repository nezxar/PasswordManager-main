import tkinter as tk
from tkinter import ttk

# class GUI:
#     APP_NAME = "Nezar App for Password Managing"
#     def __init__(self) -> None:
#         self.main_window = tkinter.Tk()
#         self.main_window.title(GUI.APP_NAME)

#         self.frame = tkinter.Frame(self.main_window)
#         self.frame.pack()

#         self.lable = tkinter.Label(self.frame,text="Hello world", font="Times 16")
#         self.lable.pack()

#         self.inputAppName = tkinter.Text(self.frame,font="Times 14", relief="raised", borderwidth=2, width=80)
#         self.inputAppName.pack()

#         self.main_window.mainloop()

class Second_Interface:
    def __init__(self) -> None:
        
        self.second_frame = tk.Frame(root, bg="#363636")
        self.info_label_second = tk.Label(self.second_frame, text="ادخل الإيميل وكلمة المرور واسم الموقع للتشفير",
                                    font=("Arial", 16), bg="#363636", fg="white")
        self.info_label_second.pack(pady=10)
        self.password_label_second = tk.Label(self.second_frame, text="كلمة المرور:", font=("Arial", 16), bg="#363636", fg="white")
        self.password_entry_second = tk.Entry(self.second_frame, show="*", font=("Arial", 14))
        self.email_label_second = tk.Label(self.second_frame, text="البريد الإلكتروني:", font=("Arial", 16), bg="#363636", fg="white")
        self.email_entry_second = tk.Entry(self.second_frame, font=("Arial", 14))
        self.site_name_label_second = tk.Label(self.second_frame, text="اسم الموقع أو التطبيق:", font=("Arial", 16), bg="#363636", fg="white")
        self.site_name_entry_second = tk.Entry(self.second_frame, font=("Arial", 14))
        self.encryption_type_label_second = tk.Label(self.second_frame, text="نوع التشفير المستخدم", font=("Arial", 16), bg="#363636", fg="white")
        self.encryption_types = ["RSA", "Caesar", "DES", "AES", "3DES"]
        self.encryption_type_combobox_second = ttk.Combobox(self.second_frame, values=self.encryption_types, font=("Arial", 14))
        self.encrypt_button_second = tk.Button(self.second_frame, text="تشفير والانتقال", command=encrypt_and_show_third_interface,
                                        font=("Arial", 16), bg="#404040", fg="white")

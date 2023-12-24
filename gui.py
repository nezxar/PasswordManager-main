import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkm
from view_table import View

class GUI:
    def __init__(self) -> None:
        # Initial a variable for the application title
        self.__APP_TITLE = "تطبيق نزار لإدارة كلمات المرور"
        # Initial a startup welcome message
        self.__WELCOME_MSG = """
مرحبًا بك في تطبيق نزار
للبدء في تخزين وإدارة كلمات المرور الخاصة بك بشكل آمن
يرجى تسجيل الدخول
"""
        self.FONT_SIZE = 14
        self.FONT_FAMILY = "Times New Romain"
        # Create the main window object
        self.main_window = tk.Tk()
        # Resize the window to fit screen
        self.__resize_window()
        # Set up the title of the application
        self.main_window.title(self.__APP_TITLE)
        # Create sub-frames to organize widgets on the main window
        self.login_frame = ttk.Frame(self.main_window)
        self.password_manager_frame = ttk.Frame(self.main_window)
        self.data_frame = ttk.Frame(self.main_window)
        # Initial variables to store inserted info
        self.site_name = None
        self.email = None
        self.password = None
        # Call methods to display the login frame and hide password manager frame
        self.show_login_frame()
        # Create all widgets
        self.create_password_manager_widgets()
        self.create_login_widgets()
        self.create_show_data_widgets()

    def __resize_window(self):
            """Resize the window to fit screen"""
            scrn_width = self.main_window.winfo_screenwidth()
            scrn_height = self.main_window.winfo_screenheight()
            # Calculate the dimensions of the window (80% of screen width, 60% of screen height)
            win_width = int((scrn_width * 60)/100)
            win_height = int((scrn_height * 60)/100)
            # Set the size of the window
            self.main_window.geometry(f'{win_width}x{win_height}+{int((scrn_width - win_width)/2)}+{int((scrn_height - win_height)/2)}')

    def show_welcome_message(self):
        '''Display the welcome message'''
        lbl = ttk.Label(self.login_frame, text=self.__WELCOME_MSG, justify=tk.CENTER,
                        font=(self.FONT_FAMILY, 17))
        lbl.pack(pady=10)
    
    def create_login_widgets(self):
        '''Create username and password entry fields along with submit button'''
        self.show_welcome_message()
        # Username label and entry field
        user_label = ttk.Label(self.login_frame, text="اسم المستخدم", font=(self.FONT_FAMILY, self.FONT_SIZE))
        user_entry = ttk.Entry(self.login_frame, font=(self.FONT_FAMILY, self.FONT_SIZE))
        user_entry.focus()
        # Password label and entry field
        passwd_label = ttk.Label(self.login_frame, text="كلمة المرور", font=(self.FONT_FAMILY, self.FONT_SIZE))
        passwd_entry = ttk.Entry(self.login_frame, show='*', font=(self.FONT_FAMILY, self.FONT_SIZE))
        # Submit button
        submit_btn = tk.Button(self.login_frame, text="دخول", font=(self.FONT_FAMILY, self.FONT_SIZE),
                                command=lambda : self.check_login(user_entry, passwd_entry))
        
        # Pack the label and entry of username
        user_label.pack(pady=1)
        user_entry.pack(pady=10)
        # Pack the label and entry of password
        passwd_label.pack(pady=1)
        passwd_entry.pack(pady=10)
        # Pack the label and entry of submit button
        submit_btn.pack(ipadx=10, ipady=4)

    def create_password_manager_widgets(self):
        '''Create fields to enter info'''
        site_name_label = ttk.Label(self.password_manager_frame, text='اسم الموقع', font=(self.FONT_FAMILY, self.FONT_SIZE))
        site_name_entry = ttk.Entry(self.password_manager_frame, font=(self.FONT_FAMILY, self.FONT_SIZE))
        site_name_entry.focus()

        email_label = ttk.Label(self.password_manager_frame, text='البريد الإلكتروني', font=(self.FONT_FAMILY, self.FONT_SIZE))
        email_entry = ttk.Entry(self.password_manager_frame, font=(self.FONT_FAMILY, self.FONT_SIZE))

        passwd_label = ttk.Label(self.password_manager_frame, text='كلمة المرور', font=(self.FONT_FAMILY, self.FONT_SIZE))
        passwd_entry = ttk.Entry(self.password_manager_frame, font=(self.FONT_FAMILY, self.FONT_SIZE))

        save_btn = tk.Button(self.password_manager_frame, text='حفظ', font=(self.FONT_FAMILY, self.FONT_SIZE),
                             command=lambda: self.save_info(site_name_entry.get(),
                                                            email_entry.get(),
                                                            passwd_entry.get())
                            )
        
        show_data = tk.Button(self.password_manager_frame, text='عرض السجلات', font=(self.FONT_FAMILY, self.FONT_SIZE),
                              command=lambda: self.show_frame(self.password_manager_frame, self.data_frame)) # type: ignore

        # Pack the logout and close buttons
        self.nav_btns(self.password_manager_frame)
        # Pack the label and entry of site name
        site_name_label.pack()
        site_name_entry.pack(pady=10)
        # Pack the label and entry of email
        email_label.pack()
        email_entry.pack(pady=10)
        # Pack the label and entry of password
        passwd_label.pack()
        passwd_entry.pack(pady=10)
        # Pack the save button
        save_btn.pack(ipadx=10, ipady=4)
        # Pack the show data button
        show_data.pack(ipadx=10, ipady=4)

    def create_show_data_widgets(self):
        '''Create a frame that shows saved information'''
        frame_label = ttk.Label(self.data_frame, text="السجلات المحفوظة", font=(self.FONT_FAMILY, self.FONT_SIZE))
        table_frame = ttk.Frame(self.data_frame)
        View(table_frame)
        frame_label.pack(padx=5, pady=5)
        table_frame.pack()
        self.nav_btns(self.data_frame, True)

    def save_info(self, site_name, email, password):
        '''Get info form fields and save'''
        self.site_name = site_name
        self.email = email
        self.password = password

    def check_login(self, uname: ttk.Entry, upassword: ttk.Entry):
        if uname.get() == 'admin' and upassword.get() == 'admin':
            print("Login Successful!")
            uname.selection_clear()
            upassword.selection_clear()
            self.show_frame(self.login_frame, self.password_manager_frame)
        elif uname == '' or upassword == '':
            tkm.showwarning('تحذير','يجب ادخال اسم المستخدم وكلمة المرور')
            print('Username of Password is Empty')
        else:
            tkm.showerror('خطأ', 'اسم المستخدم أو كلمة المرور غير صحيحة')
            print('Failed Login Attempt')

    def logout(self, frame: ttk.Frame):
        frame.pack_forget()
        self.show_login_frame()

    def close_window(self):
        self.main_window.destroy()

    def nav_btns(self, frame: ttk.Frame, back_btn=False):
        in_frame = ttk.Frame(frame)
        logout_btn = tk.Button(in_frame, text='تسجيل الخروج', font=(self.FONT_FAMILY, self.FONT_SIZE),
                               command=lambda: self.logout(self.password_manager_frame))
        close_btn = tk.Button(in_frame, text='اغلاق', font=(self.FONT_FAMILY, self.FONT_SIZE),
                              command=lambda: self.close_window())
        logout_btn.pack(padx=5, pady=5, side=tk.LEFT)
        close_btn.pack(padx=5, pady=5, side=tk.RIGHT)
        in_frame.pack(padx=10, pady=20, side=tk.BOTTOM)
        if back_btn:
            back_btn = tk.Button(in_frame, text='رجوع', font=(self.FONT_FAMILY, self.FONT_SIZE),
                             command=lambda: self.show_frame(self.data_frame, self.password_manager_frame))
            back_btn.pack(padx=5,pady=5, side=tk.RIGHT)

    # def show_password_manager_frame(self):
    #     '''Hide the login frame and show the password manager frame'''
    #     self.login_frame.pack_forget()
    #     self.password_manager_frame.pack()
    
    # def show_data_frame(self):
    #     self.password_manager_frame.pack_forget()
    #     self.data_frame.pack()

    def show_frame(self, hide_frame: ttk.Frame, show_frame: ttk.Frame):
        '''Show a specific frame while hiding another one'''
        hide_frame.pack_forget()
        show_frame.pack()

    def show_login_frame(self):
        '''Show the login frame'''
        self.login_frame.pack()

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode('white')
ctk.set_default_color_theme('blue')


def signup_page():
    global firstname_entry, lastname_entry, email_entry, phonenumber_entry, password_entry, confirm_password_entry
    login_frames.grid_remove()
    signup_frames.grid(row= 0, column= 1)
    # Signup details
    title_label = ctk.CTkLabel(signup_frames, text= 'Register', fg_color= 'blue')
    title_label.grid(row= 0, column= 0, pady= 20, ipadx= 10)

    firstname_label = ctk.CTkLabel(signup_frames, text= 'First Name')
    firstname_label.grid(row = 1, column = 0)

    firstname_entry = ctk.CTkEntry(signup_frames, width= 200, placeholder_text= 'Enter your first name')
    firstname_entry.grid(row=2, column= 0, padx= 50)

    lastname_label = ctk.CTkLabel(signup_frames, text= 'Last Name')
    lastname_label.grid(row= 3, column= 0)

    lastname_entry = ctk.CTkEntry(signup_frames, width= 200,placeholder_text= 'Enter your last name' )
    lastname_entry.grid(row=4, column = 0, padx = 50)

    email_label = ctk.CTkLabel(signup_frames, text= 'Email')
    email_label.grid(row= 5, column= 0)

    email_entry = ctk.CTkEntry(signup_frames, width = 200, placeholder_text= 'Enter your email')
    email_entry.grid(row=6, column= 0, padx= 50)

    phonenumber_label = ctk.CTkLabel(signup_frames, text = 'Phone Number')
    phonenumber_label.grid(row = 7, column = 0)

    phonenumber_entry = ctk.CTkEntry(signup_frames, width= 200, placeholder_text= 'Enter your phone number')
    phonenumber_entry.grid(row=8, column= 0, padx= 50)

    password_label = ctk.CTkLabel(signup_frames, text = 'Password')
    password_label.grid(row = 9, column = 0)

    password_entry = ctk.CTkEntry(signup_frames, width= 200, show= '*')
    password_entry.grid(row=10, column= 0, padx= 50)

    confirm_password_label = ctk.CTkLabel(signup_frames, text= 'Confirm password')
    confirm_password_label.grid(row = 11, column = 0)

    confirm_password_entry= ctk.CTkEntry(signup_frames, width= 200, show= '*')
    confirm_password_entry.grid(row=12, column= 0, padx= 50)

    register_button = ctk.CTkEntry(signup_frames, text='register', command= get_info )
    register_button.grid(row= 13, column= 0, pady= (10, 15))

def registration():
    CTkMessagebox(title= 'login page', message= 'thank you for registering')





def login_page():
    signup_frames.grid_remove()
    login_frames.grid(row= 0, column= 1)

    # login section
    login_title = ctk.CTkLabel(login_frames, text='login section', font= ('montserat', 20, 'bold'))
    login_title.grid(row= 0, column= 0, pady=(10, 30))

    email = ctk.CTkLabel(login_frames, text='Email')
    email.grid(row= 1, column= 0, padx= 100)

    email_entry = ctk.CTkEntry(login_frames)
    email_entry.grid(row= 2, column= 0, pady=(0, 20))

    password_label = ctk.CTkLabel(login_frames, text='password')
    password_label.grid(row= 3, column= 0)

    password_entry = ctk.CTkEntry(login_frames, show= '*')
    password_entry.grid(row= 4, column= 0)

    signin_in_button = ctk.CTkButton(login_frames, text='sigin')
    signin_in_button.grid(row= 5, column= 0, pady= (20, 10))

def get_info():
    # getting entries from users
    firstname= firstname_entry.get()
    lastname= lastname_entry.get()
    email= email_entry.get()
    phonenumber= password_entry.get()
    password= password_entry.get
    confirmpassword= confirm_password_entry.get()

    if password == confirmpassword:
         CTkMessagebox(title= 'login page', message= 'thank you for registering')
    elif password!= confirmpassword:
         CTkMessagebox(title= 'login page', message= 'your password is incorrect')






if __name__ == '__main__':
    window = ctk.CTk()
    window.geometry('700x600')#how to give your window its size
    window.title('MUSTY Login Page')#how to add title on your title page
    window.iconbitmap()#how to add image to you icon bar/button

    # Section Frames
    button_frames = ctk. CTkFrame(window)
    button_frames.grid(row= 0, column= 0, padx= (30, 50))

    login_frames = ctk. CTkFrame(window)
    login_frames.grid(row= 0, column= 1, pady= 50)

    signup_frames = ctk. CTkFrame(window)
    signup_frames.grid(row= 0, column= 1, pady= 50)

    # Login and Signup section

    login_button = ctk.CTkButton(button_frames, text='Login', command= login_page)
    login_button.grid(row= 0, column= 0, pady= (15, 30), padx= 20)

    signup_button = ctk.CTkButton(button_frames, text= 'Sign up',command= signup_page)
    signup_button.grid(row= 1, column= 0, pady= (0, 15))

    join_button = ctk.CTkButton(button_frames, text = 'join meeting')
    join_button.grid(row= 2, column= 0, pady= (15, 30), padx= 20)



    signup_page()

    # column and row configuration
    window.columnconfigure(0, weight= 1)
    window.columnconfigure(1, weight= 1)
    window.rowconfigure(0, weight= 1)
    



   

    
    window.mainloop()
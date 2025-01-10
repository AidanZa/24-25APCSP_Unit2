#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("222x222")
root.resizable(False, False)

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
frame_login.grid(row="0", column="0", sitcky="mews")
frame_auth.grid(row="0", column="0", sitcky="mews")

# Activate the grid in our new frame
frame_login.grid()

def login():
    frame_auth.tkraise()


# username box
lbl_username = tk.Label(frame_login, text='Username:', fg="red", font=('14'))
tk.Label(frame_login,text="Password:",font="Courier")
lbl_username.pack(padx=50,)
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()


# password box
lbl_password = tk.Label(frame_login, text='Password:', fg="red", font=('14'))
tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack(padx=50,)
ent_password= tk.Entry(frame_login, bd=3)
ent_password.pack()

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack(pady=10)

#Auth Frame label
lbl_authorized = tk.Label(frame_auth, text='Authorization Screen:', font=('24'))
tk.Label(frame_login,text="Password:",font="Courier")
lbl_authorized.pack(padx=50,)

frame_login.tkraise()
root.mainloop()
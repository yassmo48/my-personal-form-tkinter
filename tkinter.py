from tkinter import *
window=Tk()
window.title("my personal form")
window.geometry("400x300")


title=Label(window,text="my personal form", fg=white, bg="brown", width=40)
title.grid(row=0, column= 0, columnspan=2, padx=10, pady=10)


email_label=Label(window, text="email", fg="black", bg="white")
email_label.grid(row=1, column=0, padx=10, pady=5)

email_entry=Entry(window, fg="blue", bg="lightyellow", width=25)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label=Label(window, text="password", fg="black", bg="white")
password_label.grid(row=1, column=0, padx=10, pady=5)


password_entry=Entry(window, fg="blue", bg="lightyellow", width=25)
password_entry.grid(row=1, column=1, padx=10, pady=5)



form_frame=Frame(window, relief=RAISED, borderwidth=3)
form_frame.grid(row=3, column=0, columnspan=2, padx=10,pady=5)

form_label=Label(form_frame, text="FORM LOGIN")
form_label.pack()

sumbit=Button(window, text="Login", bg="purple", fg="white", width=20)
sumbit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
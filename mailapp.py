import smtplib
from tkinter import *

def msg():
    sender_mail_id = "You have to enter your mail id"
    password = "Here you have to enter your gamil password"
    reciever_mail_id = e1.get()

    

    message = text.get(1.0, END)
    text.insert('1.0', f"Sending\"{message}\" to {reciever_mail_id}\nPlease Wait !!!")
    s = smtplib.SMTP('smtp.gamil.com', 587)

    s.starttls()

    s.login(sender_mail_id, password)

    s.sendmail(sender_mail_id, reciever_mail_id, message)

    s.quit()

master = Tk()
master.title('Gmail App')
master.geometry('450x350')
Label(master, text='Enter Receiver\'s mail id').place(x = 170, y= 0)
e1 = Entry(master, width = 30)
e1.place(x= 140, y = 50)
text = Text(master, height = 10, width = 54, bg = "light yellow")
text.place(x = 8, y = 170)
button = Button(master, text = 'Send', width =25, bd = 5, bg = "green", command = msg)
button.place(x = 8, y = 110)
button1 = Button(master, text = 'Exit', width =25, bd = 5, bg = "red", command = quit)
button1.place(x = 253, y = 110)
master.mainloop()
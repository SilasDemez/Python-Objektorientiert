# coding=utf-8
import socket, threading
import tkinter as tk
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialization
FORMAT = "utf-8"


# GUI class for the chat
class GUI:
    username = ""
    address = ""
    port = 0

    index = 0

    # constructor method
    def __init__(self):
        self.window = tk.Tk()
        self.chatwindow = tk.Tk()
        self.chatwindow.withdraw()

        self.entry1 = tk.StringVar(self.window)
        self.entry2 = tk.StringVar(self.window)
        self.entry3 = tk.IntVar(self.window)

        self.msg = tk.StringVar(self.chatwindow)

        self.l1 = tk.Label(self.window, text="Username:").grid(row=0, column=0)
        self.e1 = tk.Entry(self.window, textvariable=self.entry1).grid(row=0, column=1)

        self.l2 = tk.Label(self.window, text="IP-Address:").grid(row=1, column=0)
        self.e2 = tk.Entry(self.window, textvariable=self.entry2).grid(row=1, column=1)

        self.l3 = tk.Label(self.window, text="Port:").grid(row=2, column=0)
        self.e3 = tk.Entry(self.window, textvariable=self.entry3).grid(row=2, column=1)

        self.b1 = tk.Button(self.window, text="Submit", command=self.submit).grid(row=3, column=0, columnspan=2,
                                                                                  sticky=tk.N + tk.S + tk.E + tk.W)

        self.textbox = tk.Text(self.chatwindow)
        self.textbox.grid(row=0, column=0)
        self.textentry = tk.Entry(self.chatwindow, textvariable=self.msg).grid(row=1, column=0,
                                                                               sticky=tk.N + tk.S + tk.E + tk.W)

        self.b2 = tk.Button(self.chatwindow, text="Send", command=self.sendmessage).grid(row=1, column=1,
                                                                                         sticky=tk.N + tk.S + tk.E + tk.W)

        self.window.mainloop()

    def submit(self):

        self.username = self.entry1.get()
        self.address = self.entry2.get()
        self.port = self.entry3.get()

        client.connect((self.address, self.port))  # connecting client to server

        self.window.withdraw()
        self.window.destroy()

        # client.send(self.username.encode(FORMAT))

        self.chatwindow.deiconify()

        self.textbox.insert("end", "hoi")

        t = threading.Thread(target=self.receive())
        t.start()

        self.chatwindow.mainloop()

    def sendmessage(self):
        msg = self.msg.get()
        msg = (f"{self.username}: {msg}")
        print("Sending this message: " + msg)
        client.send(msg.encode(FORMAT))

    def receive(self):
        while True:
            try:
                print("Waiting for message")
                time.sleep(1)
                msg = client.recv(1024).decode(FORMAT)
                print("Message: " + msg)
                if msg == 'NAME':
                    client.send(self.username.encode(FORMAT))
                elif msg == "":
                    pass
                else:
                    # self.textbox.configure(state="normal")
                    print("Trying to write to textbox")
                    self.textbox.insert("end", "msg")
                    # self.textbox.configure(state="disabled")
                    print("WTF")
            except:
                print("FATAL ERROR!")
                client.close()
                break




"""
    def nextWindow(self, name):
        self.login.destroy()
        self.layout(name)

        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

    # The main layout of the chat
    def layout(self, name):

        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,
                              height=False)
        self.Window.configure(width=470,
                              height=550,
                              bg="#17202A")
        self.labelHead = Label(self.Window,
                               bg="#17202A",
                               fg="#EAECEE",
                               text=self.name,
                               font="Helvetica 13 bold",
                               pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,
                          width=450,
                          bg="#ABB2B9")

        self.line.place(relwidth=1,
                        rely=0.07,
                        relheight=0.012)

        self.textCons = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=5,
                             pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.labelBottom = Label(self.Window,
                                 bg="#ABB2B9",
                                 height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                              bg="#2C3E50",
                              fg="#EAECEE",
                              font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74,
                            relheight=0.06,
                            rely=0.008,
                            relx=0.011)

        self.entryMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text="Send",
                                font="Helvetica 10 bold",
                                width=20,
                                bg="#ABB2B9",
                                command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.06,
                             relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

        def receive():
            while True:  # making valid connection
                try:
                    message = client.recv(1024).decode('utf8')
                    if message == 'NICKNAME':
                        client.send(nickname.encode('utf8'))
                    else:
                        print(message)
                except:  # case on wrong ip/port details
                    print("FATAL ERROR!")
                    client.close()
                    break

    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                # if the messages from the server is NAME send the client's name
                if message == 'NICKNAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END,
                                         message + "\n\n")

                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break

                # function to send messages

    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

"""
# create a GUI class object
g = GUI()

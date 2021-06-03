import socket
import threading
import tkinter
import tkinter.scrolledtext

FORMAT = 'utf-8'


class Client:

    def __init__(self):

        self.msg = tkinter.Tk()

        self.entry1 = tkinter.StringVar(self.msg)
        self.entry2 = tkinter.StringVar(self.msg)
        self.entry3 = tkinter.IntVar(self.msg)

        self.l1 = tkinter.Label(self.msg, text="Username:").grid(row=0, column=0, padx=20, pady=5)
        self.entry1.set("user")
        self.e1 = tkinter.Entry(self.msg, textvariable=self.entry1).grid(row=0, column=1, padx=20, pady=5)

        self.l2 = tkinter.Label(self.msg, text="IP-Address:").grid(row=1, column=0, padx=20, pady=5)
        self.entry2.set("127.0.0.1")
        self.e2 = tkinter.Entry(self.msg, textvariable=self.entry2).grid(row=1, column=1, padx=20, pady=5)

        self.l3 = tkinter.Label(self.msg, text="Port:").grid(row=2, column=0, padx=20, pady=5)
        self.entry3.set("7976")
        self.e3 = tkinter.Entry(self.msg, textvariable=self.entry3).grid(row=2, column=1, padx=20, pady=5)

        self.b1 = tkinter.Button(self.msg, text="Submit", command=self.submit).grid(row=3, column=0, columnspan=2, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W, padx=20, pady=5)

        self.gui_done = False
        self.running = True

        self.msg.mainloop()

    def submit(self):
        self.nickname = self.entry1.get()
        self.host = self.entry2.get()
        self.port = self.entry3.get()

        self.msg.withdraw()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Trying to connect to: " + self.host + ", " + str(self.port))
        self.sock.connect((self.host, self.port))

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text='Send', command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):

        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode(FORMAT))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode(FORMAT)
                if message == 'NICK':
                    self.sock.send(self.nickname.encode(FORMAT))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break

client = Client()

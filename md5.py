import hashlib
import tkinter as tk


bg = "#030303"
fg = "#ffffff"

def Hash():
    hashnya.set(hashlib.md5(teksnya.get().encode()).hexdigest())


root = tk.Tk()
root.title("MD5 Encrypter")
root.geometry("400x200")
root.configure(bg=bg)

teksnya = tk.StringVar()
hashnya = tk.StringVar()

label1 = tk.Label(text="Tulislah sebuah kata : ", fg=fg,bg=bg,width=100)
label1.pack()
txtTeks = tk.Entry(textvar = teksnya, width = 50)
txtTeks.pack()
btnHitung = tk.Button(text = "ENCRYPT",fg=fg,bg=bg, command = Hash)
btnHitung.pack()
label2 = tk.Label(text="Output : ",fg=fg,bg=bg, width=50)
label2.pack()
txtTeks = tk.Entry(textvar = hashnya, width = 50)
txtTeks.pack()

root.mainloop()

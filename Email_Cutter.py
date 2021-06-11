import tkinter as tk

root = tk.Tk()
root.title("Email Cutter")

canvas = tk.Canvas(root, width = 400, height = 300)
canvas.pack()

label = tk.Label(root, font = 30, text = "Email Cutter")
canvas.create_window(200, 30, window=label)

def click(*args):
        entry.delete(0,'end')
        

entry = tk.Entry(root, font=10)
entry.insert(0,"Enter email:")
entry.pack()

entry.bind("<Button-1>", click)
entry.pack()
canvas.create_window(200, 80, window=entry)


def emailSlicer():
        x = entry.get()
        global label1
        global label2
        label1 = tk.Label(root, font = 20, text = "Username is: " + "" + x[:x.index('@')])
        label2 = tk.Label(root, font = 20, text = "Domain is: " + "" + x[x.index('@') + 1:])
        canvas.create_window(200, 130, window=label1)
        canvas.create_window(200, 170, window=label2)
        
def clear():
        label1.destroy()
        label2.destroy()

button = tk.Button(text="Cut", font = 30, width=15, command=emailSlicer)
canvas.create_window(200, 220, window=button)

button1 = tk.Button(text = "Clear" , font = 30, width=15, command=clear)
canvas.create_window(200, 270, window=button1)

root.mainloop()


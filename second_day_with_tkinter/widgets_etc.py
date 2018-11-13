import tkinter as tk
from tkinter import Label

def write_slogan():
        print("birseyler karalamalisin")



root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button =tk.Button(frame,text="cikis",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan= tk.Button(frame, text="selam",command=write_slogan)
slogan.pack(side=tk.TOP)
widget = Label(None, text='İlk denemeler için ideal gibi ') # make a Label
widget.pack() # arrange it in its parent
widget.mainloop()
root.mainloop()

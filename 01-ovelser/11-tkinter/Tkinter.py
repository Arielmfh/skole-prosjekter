import tkinter as tk

root = tk.Tk()
root.geometry("200x150")
frame = tk.Frame(root)
frame.pack()
  
leftframe = tk.Frame(root)
leftframe.pack(side=tk.LEFT)
  
rightframe = tk.Frame(root)
rightframe.pack(side=tk.RIGHT)
  
label = tk.Label(frame, text = "Hello world")
label.pack()
  
button1 = tk.Button(leftframe, text = "Knapp 1")
button1.pack(padx = 3, pady = 3)
button2 = tk.Button(rightframe, text = "Knapp 2")
button2.pack(padx = 3, pady = 3)
button3 = tk.Button(leftframe, text = "Knapp 3")
button3.pack(padx = 3, pady = 3)
  
root.title("Test")

""" root = tk.Tk()

message = tk.Label(root, text="Hello, World!")
message.pack()
"""
root.mainloop() 

input("Press enter to exit...")
from tkinter import *

def processOK():
    print("OK Button was pressed!")

def processCancel():
    print("Cancel button was pressed!")

def main():
    window = Tk() # create a window
    label = Label(window, text = "This is my window!") #Create a label
    #button = Button(window, text = "Click me!") #Create a button
    btOK = Button(window, text = "OK", fg="red", command = processOK)
    btCancel = Button(window, text = "Cancel", bg="yellow",
                      command = processCancel)
    label.pack()
    btOK.pack()
    btCancel.pack()
    #button.pack()

    window.mainloop()

main()
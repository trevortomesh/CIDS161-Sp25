# Introduction to Tkinter and File Dialogs in Python

## Summary
In this session, we introduced graphical user interfaces (GUIs) using the `tkinter` library in Python. We explored how to create a basic window, use widgets like labels and buttons, and handle user interaction through event-driven programming. The lecture also demonstrated file dialogs to open and save files using `tkinter.filedialog`, laying the groundwork for building simple file editors and user-friendly applications.

## What is Tkinter?
Tkinter (short for "Tk Interface") is Python's standard GUI (Graphical User Interface) package. It enables developers to create desktop applications with windows, buttons, text inputs, and more. It is particularly useful for learning GUI development and serves as a bridge to object-oriented programming concepts.

## Getting Started with Tkinter
To begin using Tkinter:
```python
from tkinter import *
```
This imports all necessary classes and functions.

### Creating a Window
```python
def main():
    window = Tk()  # Creates the main window
    window.mainloop()  # Starts the GUI event loop

main()
```
The `mainloop()` method keeps the window open and listens for user interactions.

### Adding Widgets
Widgets are GUI elements like buttons, labels, and text entries. Here’s how to add a label and a button:
```python
label = Label(window, text="This is my window")
label.pack()

button = Button(window, text="Click Me")
button.pack()
```
Use `.pack()` to display the widgets within the window.

## Handling Events
Tkinter supports event-driven programming. This means that certain functions (event handlers) are executed when users perform actions like clicking a button.

### Example with Buttons
```python
def process_ok():
    print("The OK button was pressed")

def process_cancel():
    print("The Cancel button was pressed")

bt_ok = Button(window, text="OK", fg="red", command=process_ok)
bt_ok.pack()

bt_cancel = Button(window, text="Cancel", bg="yellow", command=process_cancel)
bt_cancel.pack()
```
The `command` attribute specifies which function to run when the button is clicked. Note: **do not** include parentheses after the function name in the `command=` argument.

## Introducing File Dialogs
Tkinter includes a module `filedialog` for opening and saving files via a graphical interface.

### Importing File Dialog Functions
```python
from tkinter.filedialog import askopenfilename, asksaveasfilename
```

### Asking for File Paths
```python
filename_for_reading = askopenfilename()
print("You can read from:", filename_for_reading)

filename_for_writing = asksaveasfilename()
print("You can write data to:", filename_for_writing)
```
These methods open native file dialog windows for selecting or naming files.

## Putting It All Together
You can combine GUI interaction and file handling to build useful tools. For example, you might:
- Open a file using `askopenfilename()`
- Read its contents and display them in a GUI
- Edit the contents with input fields
- Save changes using `asksaveasfilename()`

We will continue this project in the next lecture by building a simple file editor.

## Practice Exercise
Try creating a small Tkinter GUI with two buttons: one to open a file and display its name, and another to choose where to save a file. Display the selected file paths in the GUI using labels.

## Coming Up Next
On Friday, we will use what we've learned to build a basic text editor GUI that can:
- Load the contents of a file
- Let the user make edits
- Save the edited content to a new file

## Key Terms
- **GUI (Graphical User Interface)**: Interface allowing user interaction through graphical elements.
- **Widget**: Individual GUI element like a button, label, or text box.
- **Event-driven programming**: Programming model where code responds to user actions.
- **Tkinter**: Python library used for GUI applications.
- **mainloop()**: Starts the GUI event loop that listens for user events.
- **askopenfilename() / asksaveasfilename()**: Functions from `filedialog` to interact with the file system.

---
**End of Section**


from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

filenameForReading = askopenfilename()
print("You can read from " + filenameForReading)

filenameForWriting = asksaveasfilename()
print("You can write data to " + filenameForWriting)
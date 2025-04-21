CSIS 161 - April 21, 2025
Lecture Summary: File I/O, String Formatting, and Final Assignment Overview

⸻

Final Assignment Overview: “Egg Tracker”

Students were introduced to their final assignment: an egg-tracking program that requires the use of file input/output, loops, string formatting, and user input. The goal is to:
	•	Prompt the user for a file name to store daily egg logs.
	•	Ask for chicken names and the number of eggs laid daily.
	•	Stop collecting input when the user types done.
	•	Reopen the file and read entries.
	•	Display a summary table with total eggs collected.

Restrictions: Students do not need to use lists or dictionaries, though they can for extra features. Focus is on fundamental Python tools: int, str, input, print, open, format, loops, and conditionals.

Deliverables

Students must submit a PDF using the official Program Write-Up Generator (PWUDGen):
https://trevortomesh.github.io/pwudgen/161-a3-pwud.html

The write-up must include:
	•	Full Python code
	•	Program output
	•	Process documentation
	•	Any extra features
	•	Final reflection
	•	References/resources

⸻

File Input and Output in Python

Key Concepts:
	•	I/O = Input and Output to/from files.
	•	Useful in science, data collection, game save states, logging, etc.

Reading Files:

with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)

	•	"r" mode means read-only.
	•	with open(...) ensures safe file handling.
	•	Use .strip() to remove whitespace.
	•	Use loops to read line-by-line:

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

Writing Files:

with open("output.txt", "w") as file:
    file.write("I choose you, Pikachu!\n")

	•	"w" mode means write, which overwrites contents.
	•	"a" mode means append, which adds to the end of the file.

Example: Appending

with open("output.txt", "a") as file:
    file.write("I choose you, Squirty Guy!\n")



⸻

String Formatting and Looping Over Files

with open("pokemon.txt", "r") as file:
    i = 1
    for line in file:
        formatted = f"Pokemon {str(i).rjust(3, '0')}: {line.strip()}"
        print(formatted)
        i += 1

	•	str(i).rjust(3, '0') creates a padded number like 001, 002, etc. (Alternative to zfill() which students do not know.)

⸻

Writing Looped Output to a File

with open("pokemon.txt", "r") as file:
    i = 1
    for line in file:
        outstring = f"Pokemon {str(i).rjust(3, '0')}: {line.strip()}\n"
        with open("output.txt", "a") as outfile:
            outfile.write(outstring)
        i += 1

	•	Demonstrated opening a file inside the loop for repeated writing.
	•	Emphasized safety and clarity using separate file handles.

⸻

Exception Handling

Problem:

Trying to open a non-existent file causes a crash:

with open("doesnotexist.txt", "r") as file:
    # crash!

Solution:

try:
    with open("example.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")

	•	Prevents the program from crashing.
	•	Allows for graceful continuation or retry logic.

⸻

File I/O Modes Recap:

Mode	Description
r	Read only
w	Write (overwrite)
a	Append (add to end)
b	Binary mode (not covered)
+	Read and write



⸻

Closing Notes
	•	This lecture gave students all tools necessary to complete Assignment 3.
	•	Wednesday’s class will reinforce file writing and formatted output.
	•	Final assignment is due May 5, 2025.
	•	Students were reminded to check the PWUDGen tool and consent to (or opt-out of) AI-assisted grading.

⸻

Practice Questions
	1.	What does the with open(...) as file: structure ensure?
	2.	What happens if you open a file in write mode and the file already exists?
	3.	How can you format a number to display like 005 in Python without using zfill()?
	4.	What is the difference between file.read() and looping over file line-by-line?
	5.	How would you handle a situation where a file doesn’t exist using try/except?
	6.	Modify the example to write out each line of a file with a prefix like Entry #001: ... to an output file.
	7.	What is the purpose of .strip() when reading file lines?
	8.	Why might you want to avoid using "w" mode if appending is your goal?

⸻

End of Lecture Summary
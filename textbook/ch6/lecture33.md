**CS 161 Lecture Summary — April 23, 2025**

### Reading and Writing Files, Exception Handling, and Numbering Records

#### Summary
In today's lecture, we continued our exploration of file input and output in Python. We reviewed safe practices for reading and writing files using `with open(...)`, covered exception handling using `try` and `except`, and then focused on an in-class activity that involved reading a list of U.S. Presidents and prepending each one with a number.

---

### Key Concepts

#### 1. **Exception Handling with `try` and `except`**
- Purpose: Prevent the program from crashing when a file is missing or an operation fails.
- Syntax:
  ```python
  try:
      with open("somefile.txt", "r") as file:
          # do something
  except FileNotFoundError:
      print("File not found.")
  ```

#### 2. **`with open(...)` for File Safety**
- Preferred method for file I/O in Python.
- Automatically closes the file after use.
- Example:
  ```python
  with open("output.txt", "w") as outfile:
      outfile.write("Hello")
  ```

#### 3. **File Modes**
- `"r"` - Read
- `"w"` - Write (overwrites the file)
- `"a"` - Append (adds to end of file)

#### 4. **Reading a File Line-by-Line**
```python
with open("presidents.txt", "r") as file:
    for line in file:
        print(line.strip())
```

#### 5. **Numbering File Entries**
In-class activity: Add a number in front of each line in a file.
```python
with open("presidents.txt", "r") as file:
    i = 1
    for line in file:
        numbered = str(i) + " " + line.strip() + "\n"
        with open("numbered_presidents.txt", "a") as out:
            out.write(numbered)
        i += 1
```

- `line.strip()` removes leading/trailing whitespace (especially newlines).
- Make sure `out.write(...)` is inside the loop.
- Avoid using `"w"` inside the loop unless you want to overwrite every time.

#### 6. **Activity Setup**
- Students were provided a `presidents.txt` file.
- Goal: Number each president, write to a new file `numbered_presidents.txt`.
- Emphasis on using string formatting and loops without using lists or dictionaries.

---

### Final Notes
- A follow-up activity will be posted Friday (asynchronous), involving writing a program that can search the numbered list of presidents by number.
- Office hours will be virtual only for the remainder of the semester.
- Zoom links will be posted for online sessions; students are encouraged (but not required) to attend live.

---

### Practice Questions
1. What is the difference between the file modes `"w"` and `"a"`?
2. How does `with open(...)` differ from using `open(...)` without `with`?
3. What does `line.strip()` do?
4. Why is exception handling important when working with files?
5. Write a short Python snippet that appends the text "Hello World" to a file called `log.txt`.

---

Great job today! Let me know if you want help finishing the in-class activity or if you’d like feedback on your code. You now know enough to complete the final assignment!


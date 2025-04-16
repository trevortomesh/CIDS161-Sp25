# CIS 161 Lecture Summary – April 16, 2025

## Title: Strings, Characters, and Unicode in Python

### Summary
In this lecture, we shifted focus from numeric data types to non-numeric data types, specifically strings and characters. We began by exploring the concept of strings as sequences of characters and discussed how Python treats characters and strings as essentially the same type. The lecture also introduced string concatenation, character encoding, and how strings are handled internally via Unicode. We explored ASCII as a subset of Unicode and performed live demonstrations of printing characters, converting between types, and manipulating string output with escape characters and print formatting.

---

### Key Concepts

#### 1. **Strings and Characters**
- A string is a sequence of characters: e.g., `'hello world!'`.
- Python does not distinguish between single characters and one-character strings.
- You can use either single or double quotes for strings: `'A'` or `"A"`.

#### 2. **String Concatenation**
- Use `+` to concatenate strings: `'hello' + 'world'` results in `'helloworld'`.
- No space is inserted unless explicitly added.
- Strings cannot be added to integers without conversion: `"4" + 4` causes a `TypeError`.

#### 3. **Character Encoding and Unicode**
- Characters are stored in binary format inside the computer.
- Encoding maps characters to binary representations.
- Unicode is a universal encoding scheme that includes characters from almost all human languages, living and dead.
- ASCII is a subset of Unicode (characters 0 to 127).
- We demonstrated rendering Unicode characters via `\u` codes.

#### 4. **ASCII Table and ord/chr Functions**
- `ord('A')` returns 65 – the ASCII code of character 'A'.
- `chr(65)` returns `'A'`.
- ASCII characters 0–31 are non-printing control characters.
- Unicode includes emojis, Chinese, Greek, Cuneiform, and many others.

#### 5. **Escape Characters and Special Formatting**
- `\n`: new line
- `\t`: tab
- `\"` or `\'`: allows quotation marks inside strings
- These are treated as **single characters**

#### 6. **Print Behavior and `end` Keyword**
- The `print()` function by default adds a newline after printing.
- Use `end=""` to control the line ending.

```python
print("hello", end=" ")
print("world")
# Output: hello world
```

#### 7. **Converting Between Types**
- `str(x)` converts a number to a string.
- `eval(input())` can be used to convert user input into evaluated expressions (e.g., numbers).
- Avoid using `eval()` unless necessary; alternatives include `int()` and `float()`.

---

### Demonstrations
- Used `turtle.write()` to render Unicode characters graphically.
- Explored ASCII codes 0–127 using a loop and `chr(i)`.
- Calculated uppercase/lowercase conversions with `ord()` and `chr()`.
- Discussed the offset of 32 between lowercase and uppercase letters in ASCII.

---

### Practice Prompts
1. What is the difference between a string and a character in Python?
2. How do you concatenate two strings? What happens if one operand is an integer?
3. What is the output of `ord('a')`? What about `chr(66)`?
4. What are escape characters, and how are they used in strings?
5. Write a function that takes two strings and prints them on the same line, separated by a tab.
6. What does Unicode offer that ASCII doesn’t?
7. What is the difference between `str()`, `int()`, and `eval()`?

---

### Next Lecture
On Friday, we will continue discussing strings by learning about string formatting, string methods, and how to convert between various data types. We will also explore reading from and writing to text files using Python.

---

_Thank you for your attention, and see you Friday!_


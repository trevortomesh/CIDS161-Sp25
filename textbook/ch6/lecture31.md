# CIS 161 Lecture: String Formatting and Output Control (April 18, 2025)

## Summary
In this lecture, we transitioned from basic string operations into more advanced concepts of **string formatting**, including formatting numbers, controlling precision, alignment, and using format specifiers for different representations (decimal, hexadecimal, octal, binary, scientific notation, and percentages). These techniques are essential for producing clean, aligned output, particularly when writing to files or displaying tables of data. We also reviewed escape characters and special sequences within strings.

---

## Key Concepts

### 1. String vs. Number Representation
- Strings are sequences of characters.
- Characters like `'4'` are different from integers like `4`.
- Python does not automatically coerce between strings and numbers: use `str()`, `int()`, or `eval()`.

### 2. Escape Characters and Special Sequences
| Escape Sequence | Meaning             |
|------------------|----------------------|
| `\n`              | Newline              |
| `\t`              | Tab                  |
| `\"`             | Double quote         |
| `\'`              | Single quote (apostrophe) |
| `\\`              | Backslash            |

Used when inserting special characters inside strings.

---

### 3. String Input
```python
name = input("Enter your name: ")
```
- Always returns a string.
- Use `eval()` to convert string input to numeric values.

---

## 4. String Formatting with `format()`
The `format()` function allows detailed control over the layout and precision of printed data.

### Syntax:
```python
format(value, "[width].[precision][type]")
```

### Common Format Specifiers:
| Specifier | Meaning                       |
|-----------|-------------------------------|
| `d`       | Decimal integer               |
| `f`       | Floating point number         |
| `e`       | Scientific notation (e.g. 1.23e+02) |
| `%`       | Percentage                    |
| `x`       | Hexadecimal                   |
| `o`       | Octal                         |
| `b`       | Binary                        |
| `s`       | String                        |

### Field Width and Precision
```python
print(format(57.4657, "10.2f"))  # Field width 10, 2 decimals
```
This reserves 10 total spaces (including the decimal point), rounded to 2 decimal places.

### Justification
| Symbol | Meaning        |
|--------|----------------|
| `<`    | Left justified |
| `>`    | Right justified (default) |
| `^`    | Centered       |

```python
print(format("eggs", "<10s"))  # Left-justified string
```

### Scientific Notation
```python
print(format(0.0033923, "10.2e"))  # Outputs 3.39e-03
```

### Percent Formatting
```python
print(format(0.5346, "10.2%"))  # Outputs 53.46%
```
Automatically multiplies by 100 and appends `%`.

---

## 5. Ordinal Values with `ord()`
```python
print(ord('a'))  # Outputs 97
```
Returns the Unicode code point (ASCII for basic Latin letters).

---

## Unicode Review
- Unicode supports characters from almost all human languages (Greek, Kanji, Braille, Emoji, etc.).
- Unicode characters can be inserted with `\u` followed by the 4-digit hex code.
```python
print("\u03A9")  # Greek Omega: Ω
```

---

## Practice Questions

### Conceptual:
1. What does the format specifier `10.3f` mean?
2. Why is `format(3.1, ".2f")` more useful than `round(3.1, 2)` for string output?
3. What will the output be for `format(0.25, "10.1%")`?
4. What is the difference between `'4'` and `4` in Python?

### Code Practice:
**Q1:** Format the number `1234.56789` to show only two decimal places and right-justify it in a field of width 12.
```python
print(format(1234.56789, "12.2f"))
```

**Q2:** Display the string `"hello"` centered in a 20-character wide field.
```python
print(format("hello", "^20s"))
```

**Q3:** Convert the number `255` into hexadecimal and binary format using `format()`.
```python
print(format(255, "x"))  # hex
print(format(255, "b"))  # binary
```

**Q4:** Display `0.0075` as a percentage with three decimal places.
```python
print(format(0.0075, ".3%"))
```

**Q5:** What escape sequence would you use to output the string `He said "Python is fun!"`?
```python
print("He said \"Python is fun!\"")
```

---

Next class, we will begin reading from and writing to files using Python. This will build on the string formatting skills we covered today, as clean formatting is critical for working with text files and data storage.

---

**Reminder:** Our last in-person class is **Wednesday**, after which all sessions will move online. A Zoom room will be open during regular class time and recordings will be made available. You're encouraged to attend live if possible!


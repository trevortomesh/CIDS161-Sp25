**CS 161 - March 28 Lecture Summary**

---

**Topic:** Prime Number Generator and Loop Review

**Overview:**
In this class, we continued our deep dive into loops by writing a program to calculate the first 50 prime numbers. We discussed the complexity and unpredictability of prime numbers, their significance, and how to break down the logic of identifying them through nested loops and conditionals.

---

### Key Concepts:

- **Prime Number Definition:** A prime number is an integer greater than 1 that is only divisible by 1 and itself.
- **Challenge:** There is no known formula for predicting the next prime number. Therefore, computer scientists use heuristics ("good enough" methods) to calculate primes.

---

### Prime Number Algorithm Plan:

1. **Determine if a number is prime**
   - Divide the number by all integers from 2 up to half of the number (inclusive).
   - If any division results in no remainder, it's not prime.

2. **Iterate through candidate numbers (starting at 2)**
   - Use a while loop to iterate while we have fewer than 50 primes.

3. **Track the number of primes found**
   - Use a `count` variable initialized to 0.
   
4. **Display output in rows of 10 primes per line**
   - Keep a constant `PRIMES_PER_LINE = 10`

---

### Implementation Details:

- Constants are written in uppercase in Python to signify that they shouldn’t change (`NUMBER_OF_PRIMES = 50`).
- Loop logic:
  ```python
  while count < NUMBER_OF_PRIMES:
      # check if 'number' is prime
      # if yes, print it and increment count
      number += 1
  ```
- To determine primality:
  ```python
  is_prime = True
  divisor = 2
  while divisor <= number // 2:
      if number % divisor == 0:
          is_prime = False
          break
      divisor += 1
  ```
- Use `break` to exit the divisor-checking loop early once non-primality is confirmed.
- Use formatted printing and modulus to print 10 primes per line.

---

### Bonus Examples:

- Increased the number of primes to 100, 1,000, and even 10,000 to demonstrate how the algorithm scales (and slows).
- Discussed the real-world difficulty in finding primes and noted that massive primes (e.g., 41 million digits long) are found using similar techniques on powerful computers.

---

### Mathematical Note:

- The **Riemann Hypothesis** is one of the most famous unsolved problems related to prime number distribution. It proposes a pattern in the spacing of primes, but no proof exists yet.
- John Nash (of *A Beautiful Mind*) also attempted work on the Riemann Hypothesis.

---

### Next Steps:

- **Monday:** Exam review (based on quizzes)
- **Wednesday:** In-person exam (30 questions, no notes, no devices)
- **Friday (Next Week):** Begin next major topic — **functions**

---

**Closing Notes:**
- This was one of our most complex programs so far, showcasing the power of breaking problems into smaller, testable pieces.
- Prime number generation is a classic example of problem-solving with loops and conditions, and is still an active area of research in computer science and mathematics.

Thanks for your attention! See you Monday for review!


# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
OJ3355 - Shorten
```

OJ submission ID, if submitted:

```text
688500
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
The program must read a sequence of increasing positive integers terminated by -1 and output a shortened representation where consecutive numbers are combined into a range using a hyphen
Input:
Each line contains a single integer; the sequence is strictly increasing and ends with a line containing -1
Output:
A single line that lists the numbers and ranges separated by commas and a space, e.g., 1-3, 5, 7-10
Constraints:
The numbers are positive integers and strictly increase
The terminating value -1 is not part of the output
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: Read integers until -1 is encountered and store them in a list
Step 2: If the list is not empty, initialise start and end with the first number
Step 3: Iterate through the remaining numbers plus a sentinel value
Step 4: When the current number continues the consecutive run, extend end
Step 5: When the run ends, record either a single number or a start‑end range and reset start and end
Step 6: After the loop, join the recorded parts with ", " and print the result
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
The solution uses a while loop to read input, a list to store the numbers, a for loop with a sentinel to detect the end of a consecutive run, conditional logic to decide between a single value and a range, and string joining to produce the final output
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
Tests the smallest possible valid sequence containing only one number before -1
```

Input:

```text
1
-1
```

Expected output:

```text
1
```

Actual output:

```text
1
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
Tests a sequence where every number is isolated, so no ranges should be created
```

Input:

```text
2
4
6
8
-1
```

Expected output:

```text
2, 4, 6, 8
```

Actual output:

```text
2, 4, 6, 8
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
Tests a long consecutive run that ends exactly at the sentinel handling point
```

Input:

```text
5
6
7
8
9
10
-1
```

Expected output:

```text
5-10
```

Actual output:

```text
5-10
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
```

What did they help with?

```text
```

What did you still do by yourself?

```text
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |

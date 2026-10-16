# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
OJ3476 - CuteCat CuteFox
```

OJ submission ID, if submitted:

```text
688555
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
1-3 hours
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
The program must read a number of animal entries, store each animal name with its label, ensure that a cat named Garfield with label Cat01 and a fox named Fubuki with label Fox01 are present, count how many cats and foxes there are, and then print the counts followed by all animals sorted by the numeric part of their labels
Input:
Line 1: an integer N, the number of animal entries
Lines 2 to N+1: each line is a dictionary literal that maps one animal name to its label, e.g. {"Milo":"Cat02"}
Output:
Line 1: "Cat :" followed by the number of cats
Line 2: "Fox :" followed by the number of foxes
Subsequent lines: each animal name, a space, a colon, a space, and its label, ordered by the numeric part of the label, cats first then foxes
Constraints:
Each label starts with either "Cat" or "Fox" and is followed by a two‑digit number
Animal names are unique
If Garfield or Fubuki are missing, they must be added with labels Cat01 and Fox01 respectively
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
Step 1: Read the integer N
Step 2: Loop N times and read each dictionary string, converting it to a Python dict and merging it into a single collection
Step 3: Add Garfield and Fubuki with default labels if they are not already present
Step 4: Separate the entries into cat and fox groups, extracting the numeric part of each label
Step 5: Sort each group by the numeric part and print the required counts and formatted lines
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
The solution uses input reading, the ast.literal_eval function to parse dictionary strings, dictionary update operations, conditional checks for missing default animals, list building with tuple items containing the numeric label, sorting of those lists, and formatted printing. No advanced data structures beyond dicts and lists are required.
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
Minimum input size; only the required default animals are added automatically
```

Input:

```text
0
```

Expected output:

```text
Cat : 1
Fox : 1
Garfield : Cat01
Fubuki : Fox01
```

Actual output:

```text
Cat : 1
Fox : 1
Garfield : Cat01
Fubuki : Fox01
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
All entries are already the default ones, testing that duplicates are not added
```

Input:

```text
2
{"Garfield":"Cat01"}
{"Fubuki":"Fox01"}
```

Expected output:

```text
Cat : 1
Fox : 1
Garfield : Cat01
Fubuki : Fox01
```

Actual output:

```text
Cat : 1
Fox : 1
Garfield : Cat01
Fubuki : Fox01
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
Labels with the same numeric part but different prefixes, checking correct grouping and ordering
```

Input:

```text
3
{"Alpha":"Cat05"}
{"Beta":"Fox05"}
{"Gamma":"Cat03"}
```

Expected output:

```text
Cat : 3
Fox : 2
Garfield : Cat01
Gamma : Cat03
Alpha : Cat05
Fubuki : Fox01
Beta : Fox05
```

Actual output:

```text
Cat : 3
Fox : 2
Garfield : Cat01
Gamma : Cat03
Alpha : Cat05
Fubuki : Fox01
Beta : Fox05
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

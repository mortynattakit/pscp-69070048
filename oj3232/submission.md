# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
OJ3232 - กบน้อยกระโดด
```

OJ submission ID, if submitted:

```text
651118
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
Determine the minimum number of jumps required for the rabbit to cover at least the target distance Y, starting with a jump of X meters and decreasing each subsequent jump by 2 meters; output -1 if the target cannot be reached.
Input:
two integers X and Y which is the first jump distance and the goal distance
Output:
the least number of jumps whose total distance is greater than or equal to Y, or -1 if the total distance never reaches Y
Constraints:
Each jump length decreases by exactly 2 meters, no further distance can be added after jump distance becomes zero
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
Step 1: Read X and Y
Step 2: Initialize a counter for jumps and a variable for the current jump length
Step 3: While the current jump length is positive, add it to the covered distance and increase the counter
Step 4: After each addition, check if the covered distance has reached or exceeded Y and stop if it has
Step 5: If the loop ends without reaching Y, output -1
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
The program uses a while True loop that checks whether the current jump length is still positive. Inside the loop it increments a jump counter, minus the current jump length from the remaining distance and reduces the jump length by 2. When the remaining distance becomes zero or negative the counter is printed, if the jump length drops to zero or below before reaching the goal, -1 is printed
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
Smallest possible values, the first jump already meets the goal
```

Input:

```text
1 1
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
Goal is just one more than the first jump, requiring a second jump that becomes negative, so the goal is unreachable
```

Input:

```text
1 2
```

Expected output:

```text
-1
```

Actual output:

```text
-1
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
Maximum starting jump with a large goal, testing many iterations and the condition when the jump length eventually becomes non‑positive
```

Input:

```text
1000 100000
```

Expected output:

```text
113
```

Actual output:

```text
113
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

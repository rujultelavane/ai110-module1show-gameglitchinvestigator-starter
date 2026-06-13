# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When you first run it, the game appears to be fine: the UI looks great and the game feels self-explanatory, all instructions are provided.
However, when I ran it, the hints were broken. For example, if I typed in 100, it said go higher even though that's the highest it goes. And if I type in 1, it says go lower even though thats as low as you can go. It should have pointed me in the right direction and said lower/higher, respectively.
Another bug I found was that the hints were backwards. On one run of the game, I was guessing 25 and it said go lower. Once I "lost" and ran out of hints, the real answer was 45. The hint should've said go higher.
Real quick, another thing I found was when switching between game difficulty modes, when I switch from Medium to Easy, I see both in the blue box and on the side panel for Medium the range is 1-100 and I have 8 guesses. But for Easy mode, in the blue box I see the range is from 1-100 with 6 guesses, but the side panel says 1-20 with 6 guesses.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 100   |   correct guess   |   "go higher"   |         none           |
|  1    |     "go higher"   |   "go lower"    |         none           |
|  25   |    "go higher"    |    "go lower"   |         none           |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

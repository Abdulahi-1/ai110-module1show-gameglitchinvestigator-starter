# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


When I started the game, it looked normal except the number of attempts were negative numbers. I already knew that there was a bug in the way attempts were decremented. I played with the hints toggle, it seemed to work perfectly. One other bug that I found when I explored the game, the attempts and guess range were mismatched between the different difficulty levels.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

On this project I used Claude. I asked claude about why scoring was acting weird and it suggested and pointed out removing the off-by-one calculation thats stored in the score. One example of an AI suggestion that was incorrect or misleading was when it suggested to refactor the session event handler even though there wasn't anything remotely similar in the file. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


After fixing a bug in VS code, I went back to the game and refreshed it, testing whether the fix actually worked and was implemented in the game. It showed me that my code was operating correclty and that there didn't seem to be other bugs building off of the fix. At times, I ran pytest to test generated test cases to make sure a specific function was working. I tested the highscore changing after getting a guess correct, it showed me that my code was correct. AI did help me design the tests by generating them not to pass with hardcoded data but upon interaction. It tested didnt possibilities and them passing shows that they've all been accounted for as I hoped.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?


The secret number kept changing because it was in a loop that kept randomizing it from a hardcoded low and high range like "1 to 100". Streamlit "reruns" are just a way to refresh the game with the new fixes, think of it like refreshing a web browser. Its just to make sure the app itself is update to date with the changes. Session states kept track of all the changing events. For example, when we click "new game" it changes the state to a new game and starts over. when we're making a guess, the state changes to "playing". The change that I made that finally gave the game a stable secret number was by changing the hardcoded range to match the difficulty level. So instead of randomizing numbers from 1 to 100, it randomized numbers within the domain of the selected difficulty level. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.



One habit or strategy from this project that I want to reuse in the future labs or projects is determining where the errors are happening before consulting AI. One thing I would do differently next time I work with AI on a coding task is be more specific on what I expect the changes to result to. This project changed the way I think about AI generated code by allowing me to reason with AI generated code with my own intentions of how I expect the game to function.
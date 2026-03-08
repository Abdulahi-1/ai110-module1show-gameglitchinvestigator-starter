# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!


## 📝 Document Your Experience


The game's purpose is to give users a certain amount of tries and a range of numbers to guess from. Its a modern number guessing game that also calculates ones own high score from the number of questions they get correct. When I initially played the game, the attempts (number of tries a user has) were below zero. I instantly knew that there was a bug in the way the attempts decremented, you cannot have negative number amount of attempts. When I occassionally swapped difficulty levels, I noticed that the normal level was much more harder than the hard level. This was because their guessing ranges were mismatched. Each time I got a quess correct, the score didn't accumulate or save after every game. To fix these bugs, I changed the range for the "Easy" level to be between 1 to 20. I then changed the range for the "Normal" level to be between 1 to 50. Lastly, the "Hard" level was changed between 1 to 100. I swapped the number of attempts for both Easy and Normal difficulty levels. 

## 📸 Demo

<img width="744" height="766" alt="Screenshot 2026-03-08 at 2 48 48 PM" src="https://github.com/user-attachments/assets/8cf520ca-238c-4f5f-866f-0a8d44e8f512" />


## 🚀 Stretch Features

<img width="744" height="766" alt="Screenshot 2026-03-08 at 2 49 49 PM" src="https://github.com/user-attachments/assets/c82ea0ab-d55a-479f-8fda-28a87841187e" />


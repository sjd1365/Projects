readme_content = """
# 🧠 Python Trivia Quiz Game

A simple, interactive command-line interface (CLI) quiz application built with Python. This game presents randomized questions to the user and calculates their score in real-time.

## ✨ Features
* **Randomized Questions**: Every time you play, the order of questions is shuffled.
* **Score Tracking**: Keeps track of correct answers and provides a final percentage.
* **Input Validation**: Handles user input gracefully.

## 🚀 How to Run
1. Open the `.ipynb` file in Google Colab.
2. Click 'Run All' or press `Ctrl + F9`.
3. Follow the instructions in the console.

## 🛠️ Built With
* **Python 3.x**
* **Google Colab**
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md file has been created!")

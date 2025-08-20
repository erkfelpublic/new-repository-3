import random

def get_food_joke():
    jokes = [
        "Why don't eggs tell jokes? They'd crack each other up.",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An Impasta.",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_food_joke())

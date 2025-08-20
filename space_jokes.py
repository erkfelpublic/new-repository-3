import random

def get_space_joke():
    jokes = [
        "Why did the sun go to school? To get brighter!",
        "What do you call a lazy kangaroo? Pouch potato!",
        "Why don't aliens eat clowns? Because they taste funny!",
        "What is an astronaut's favorite part of a computer? The space bar.",
        "How do you organize a space party? You planet.",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_space_joke())

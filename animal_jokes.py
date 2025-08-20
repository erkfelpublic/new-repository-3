import random

def get_animal_joke():
    jokes = [
        "What do you call a fish with no eyes? Fsh!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't scientists trust atoms? Because they make up everything!",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_animal_joke())

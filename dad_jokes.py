import random

def get_dad_joke():
    jokes = [
        "I'm afraid for the calendar. Its days are numbered.",
        "My wife said I should do lunges to stay in shape. That would be a big step forward.",
        "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
        "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
        "What do a tick and the Eiffel Tower in Paris have in common? They're both Paris sites.",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_dad_joke())

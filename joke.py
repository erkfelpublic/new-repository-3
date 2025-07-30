import random

def tell_joke():
    """
    This function tells a random programming joke.
    """
    jokes = [
        ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
        ("Why don't programmers like nature?", "It has too many bugs."),
        ("What's a programmer's favorite hangout place?", "Foo Bar."),
        ("How many programmers does it take to change a light bulb?", "None, that's a hardware problem."),
        ("Why was the JavaScript developer sad?", "Because he didn't Node how to Express himself.")
    ]

    question, answer = random.choice(jokes)

    print(question)
    print(answer)

if __name__ == "__main__":
    tell_joke()

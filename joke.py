import random

def tell_joke():
    """
    This function tells a random programming joke.
    """
    jokes = [
        {
            "question": "Why do programmers prefer dark mode?",
            "answer": "Because light attracts bugs!"
        },
        {
            "question": "Why did the scarecrow win an award?",
            "answer": "Because he was outstanding in his field!"
        },
        {
            "question": "What do you call a fake noodle?",
            "answer": "An Impasta!"
        }
    ]

    joke = random.choice(jokes)
    print(joke["question"])
    print(joke["answer"])

if __name__ == "__main__":
    tell_joke()

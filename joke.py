import random

jokes = [
    {
        "question": "Why do programmers prefer dark mode?",
        "answer": "Because light attracts bugs!"
    },
    {
        "question": "Why don't programmers like nature?",
        "answer": "It has too many bugs."
    },
    {
        "question": "What's a programmer's favorite hangout place?",
        "answer": "Foo Bar."
    },
    {
        "question": "Why did the developer go broke?",
        "answer": "Because he used up all his cache."
    }
]

def tell_joke():
    """
    This function randomly selects and tells a programming joke.
    """
    joke = random.choice(jokes)
    question = joke["question"]
    answer = joke["answer"]

    print(question)
    print(answer)

if __name__ == "__main__":
    tell_joke()

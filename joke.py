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
    },
    {
        "question": "What is a programmer's favorite drink?",
        "answer": "Java."
    },
    {
        "question": "Why was the JavaScript developer sad?",
        "answer": "Because he didn't Node how to Express himself."
    },
    {
        "question": "How many programmers does it take to change a light bulb?",
        "answer": "None. It's a hardware problem."
    },
    {
        "question": "What's the object-oriented way to become wealthy?",
        "answer": "Inheritance."
    },
    {
        "question": "Why did the web developer refuse to leave the house?",
        "answer": "He had a cache flow problem."
    },
    {
        "question": "What do you call a programmer from Finland?",
        "answer": "Nerdic."
    },
    {
        "question": "What did the Java code say to the C code?",
        "answer": "You've got no class."
    },
    {
        "question": "Why do Java developers wear glasses?",
        "answer": "Because they don't C#."
    },
    {
        "question": "How do you comfort a JavaScript bug?",
        "answer": "You console it."
    },
    {
        "question": "What's the best thing about a boolean?",
        "answer": "Even if you're wrong, you're only off by a bit."
    },
    {
        "question": "Why do programmers always mix up Christmas and Halloween?",
        "answer": "Because Oct 31 == Dec 25."
    },
    {
        "question": "What is a computer's favorite snack?",
        "answer": "Computer chips."
    },
    {
        "question": "Why was the computer cold?",
        "answer": "It left its Windows open."
    },
    {
        "question": "What do you call a computer that sings?",
        "answer": "A-dell."
    },
    {
        "question": "Why did the scarecrow win an award?",
        "answer": "Because he was outstanding in his field."
    },
    {
        "question": "What did the spider do on the computer?",
        "answer": "It made a website."
    },
    {
        "question": "Why was the developer always calm?",
        "answer": "He had inner peace."
    },
    {
        "question": "Why did the programmer quit his job?",
        "answer": "Because he didn't get arrays."
    },
    {
        "question": "What's a developer's favorite type of music?",
        "answer": "Algo-rhythm."
    },
    {
        "question": "What is the most used language in programming?",
        "answer": "Profanity."
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

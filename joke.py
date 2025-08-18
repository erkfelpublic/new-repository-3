import random

jokes = [
    {
        "number": 1,
        "question": "Why do programmers prefer dark mode?",
        "answer": "Because light attracts bugs!"
    },
    {
        "number": 2,
        "question": "Why don't programmers like nature?",
        "answer": "It has too many bugs."
    },
    {
        "number": 3,
        "question": "What's a programmer's favorite hangout place?",
        "answer": "Foo Bar."
    },
    {
        "number": 4,
        "question": "Why did the developer go broke?",
        "answer": "Because he used up all his cache."
    },
    {
        "number": 5,
        "question": "What is a programmer's favorite drink?",
        "answer": "Java."
    },
    {
        "number": 6,
        "question": "Why was the JavaScript developer sad?",
        "answer": "Because he didn't Node how to Express himself."
    },
    {
        "number": 7,
        "question": "How many programmers does it take to change a light bulb?",
        "answer": "None. It's a hardware problem."
    },
    {
        "number": 8,
        "question": "What's the object-oriented way to become wealthy?",
        "answer": "Inheritance."
    },
    {
        "number": 9,
        "question": "Why did the web developer refuse to leave the house?",
        "answer": "He had a cache flow problem."
    },
    {
        "number": 10,
        "question": "What do you call a programmer from Finland?",
        "answer": "Nerdic."
    },
    {
        "number": 11,
        "question": "What did the Java code say to the C code?",
        "answer": "You've got no class."
    },
    {
        "number": 12,
        "question": "Why do Java developers wear glasses?",
        "answer": "Because they don't C#."
    },
    {
        "number": 13,
        "question": "How do you comfort a JavaScript bug?",
        "answer": "You console it."
    },
    {
        "number": 14,
        "question": "What's the best thing about a boolean?",
        "answer": "Even if you're wrong, you're only off by a bit."
    },
    {
        "number": 15,
        "question": "What's a developer's favorite type of music?",
        "answer": "Algo-rhythm."
    },
    {
        "number": 16,
        "question": "Why did the programmer quit his job?",
        "answer": "He didn't get arrays."
    },
    {
        "number": 17,
        "question": "Why do programmers always mix up Christmas and Halloween?",
        "answer": "Because Oct 31 == Dec 25."
    },
    {
        "number": 18,
        "question": "What's the difference between a programmer and a pilot?",
        "answer": "A pilot knows when to stop."
    },
    {
        "number": 19,
        "question": "How do you generate a random string?",
        "answer": "Put a first-year student in front of vim and ask them to exit."
    },
    {
        "number": 20,
        "question": "What's a programmer's favorite movie?",
        "answer": "The Social Network."
    },
    {
        "number": 21,
        "question": "Why was the computer cold?",
        "answer": "It left its Windows open."
    },
    {
        "number": 22,
        "question": "What is a computer's favorite snack?",
        "answer": "Microchips."
    },
    {
        "number": 23,
        "question": "Why are Assembly programmers always soaking wet?",
        "answer": "They work below C-level."
    },
    {
        "number": 24,
        "question": "Why don't bachelors like Git?",
        "answer": "Because they are afraid to commit."
    },
    {
        "number": 25,
        "question": "How do you tell an introvert developer from an extrovert developer?",
        "answer": "An extrovert developer looks at your shoes when he is talking to you."
    },
    {
        "number": 26,
        "question": "What is the most used language in programming?",
        "answer": "Profanity."
    },
    {
        "number": 27,
        "question": "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "answer": "The punchline is that '10' in binary is equal to 2 in decimal."
    },
    {
        "number": 28,
        "question": "Why was the developer always calm?",
        "answer": "He knew how to handle exceptions."
    },
    {
        "number": 29,
        "question": "What's the best way to get a developer to write documentation?",
        "answer": "Tell them it's 'code'."
    },
    {
        "number": 30,
        "question": "Why did the functions stop calling each other?",
        "answer": "Because they had constant arguments."
    },
    {
        "number": 31,
        "question": "What do you call a group of 8 Hobbits?",
        "answer": "A Hobbyte."
    },
    {
        "number": 32,
        "question": "Why did the developer break up with the designer?",
        "answer": "They didn't see eye to eye on the interface."
    },
    {
        "number": 33,
        "question": "Why do front-end developers eat lunch alone?",
        "answer": "Because they don't know how to join tables."
    }
]

def tell_joke():
    """
    This function randomly selects and tells a programming joke.
    """
    joke = random.choice(jokes)
    number = joke["number"]
    question = joke["question"]
    answer = joke["answer"]

    print(f"Joke #{number}")
    print(question)
    if answer:
        print(answer)

if __name__ == "__main__":
    tell_joke()

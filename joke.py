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
        "question": "Why did the programmer quit his job?",
        "answer": "Because he didn't get arrays."
    },
    {
        "question": "What is a computer's favorite beat?",
        "answer": "An algo-rhythm."
    },
    {
        "question": "Why do programmers always mix up Christmas and Halloween?",
        "answer": "Because Oct 31 == Dec 25."
    },
    {
        "question": "What's a programmer's favorite karaoke song?",
        "answer": "Hello, World!"
    },
    {
        "question": "Why are Assembly programmers always soaking wet?",
        "answer": "They work below C-level."
    },
    {
        "question": "What do you call a group of 8 hobbits?",
        "answer": "A hob-byte."
    },
    {
        "question": "Why was the developer always calm?",
        "answer": "He had inner peace."
    },
    {
        "question": "Why did the functions stop calling each other?",
        "answer": "They had constant arguments."
    },
    {
        "question": "What's a bug's life motto?",
        "answer": "To err is human, to really foul things up you need a computer."
    },
    {
        "question": "Why don't bachelors like Git?",
        "answer": "Because they are afraid to commit."
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

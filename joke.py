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
        "question": "What's the best way to learn to code?",
        "answer": "Make mistakes and then debug them."
    },
    {
        "question": "Why did the programmer quit his job?",
        "answer": "He didn't get arrays."
    },
    {
        "question": "What is a computer's favorite beat?",
        "answer": "An algo-rhythm."
    },
    {
        "question": "Why did the two Java methods get a divorce?",
        "answer": "Because they had constant arguments."
    },
    {
        "question": "What do you call a programmer who is also a bodybuilder?",
        "answer": "A strong developer."
    },
    {
        "question": "Why did the CSS developer go to the eye doctor?",
        "answer": "He had a problem with his vision."
    },
    {
        "question": "What did the server say to the client who was leaving?",
        "answer": "Bye, have a good time!"
    },
    {
        "question": "Why was the database administrator always so calm?",
        "answer": "Because he knew how to handle a crisis."
    },
    {
        "question": "What's a developer's favorite type of music?",
        "answer": "Heavy metal, because it's full of lead."
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

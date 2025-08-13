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
        "question": "I've got a really good UDP joke to tell you, but I don't know if you'll get it.",
        "answer": "..."
    },
    {
        "question": "There are 10 kinds of people in the world.",
        "answer": "Those who understand binary and those who don't."
    },
    {
        "question": "A guy walks into a bar and asks for 1.4 root beers.",
        "answer": "The bartender says “I'll have to charge you extra, that's a root beer float”. The guy says “In that case, better make it a double.”"
    },
    {
        "question": "Knock, knock.",
        "answer": "(A very long pause) Java."
    },
    {
        "question": "Why did the programmer quit his job?",
        "answer": "Because he didn't get arrays."
    },
    {
        "question": "A programmer puts two glasses on his bedside table before going to sleep.",
        "answer": "A full one, in case he gets thirsty, and an empty one, in case he doesn't."
    },
    {
        "question": "What's a programmer's motto?",
        "answer": "Things aren't always #000000 and #FFFFFF."
    },
    {
        "question": "99 little bugs in the code, 99 little bugs, you take one down and patch it around...",
        "answer": "125 little bugs in the code."
    },
    {
        "question": "What's a programmer's favorite pick-up line?",
        "answer": "Are you a keyboard? Because you're my type."
    },
    {
        "question": "Why do programmers always carry umbrellas?",
        "answer": "In case it starts raining cats and dogs."
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

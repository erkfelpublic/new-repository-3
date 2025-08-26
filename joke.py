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
        "question": "Why do programmers like to use the command line?",
        "answer": "Because it's a direct order!"
    },
    {
        "number": 34,
        "question": "What's a programmer's favorite place to swim?",
        "answer": "The data lake."
    },
    {
        "number": 35,
        "question": "Why did the programmer get stuck in the shower?",
        "answer": "The instructions said: Lather, Rinse, Repeat."
    },
    {
        "number": 36,
        "question": "What do you call a programmer who is also a bodybuilder?",
        "answer": "A strong developer."
    },
    {
        "number": 37,
        "question": "Why was the database administrator so good at his job?",
        "answer": "He had a lot of table manners."
    },
    {
        "number": 38,
        "question": "What's a ghost's favorite data type?",
        "answer": "Boo-lean."
    },
    {
        "number": 39,
        "question": "Why did the developer break up with the QA tester?",
        "answer": "They were always finding faults in the relationship."
    },
    {
        "number": 40,
        "question": "What's a programmer's favorite song?",
        "answer": "'Hello, World!' by The Code."
    },
    {
        "number": 41,
        "question": "Why did the programmer bring a ladder to the bar?",
        "answer": "He heard the drinks were on the house."
    },
    {
        "number": 42,
        "question": "How do you know a programmer is an extrovert?",
        "answer": "They'll look at *your* shoes when they're talking to you."
    },
    {
        "number": 43,
        "question": "Why did the developer go to the gym?",
        "answer": "To get a better commit history."
    },
    {
        "number": 44,
        "question": "What's a programmer's favorite type of story?",
        "answer": "A recursion."
    },
    {
        "number": 45,
        "question": "Why don't programmers like to play hide and seek?",
        "answer": "Because they always get caught in a loop."
    },
    {
        "number": 46,
        "question": "What do you call a programmer who can't code?",
        "answer": "A project manager."
    },
    {
        "number": 47,
        "question": "Why did the programmer get fired?",
        "answer": "He had a bad attitude."
    },
    {
        "number": 48,
        "question": "What's the difference between a programmer and a magician?",
        "answer": "A magician can make things disappear without a trace."
    },
    {
        "number": 49,
        "question": "Why was the developer always so calm?",
        "answer": "He had a good handle on his exceptions."
    },
    {
        "number": 50,
        "question": "What's a programmer's favorite breakfast?",
        "answer": "A stack of pancakes."
    },
    {
        "number": 51,
        "question": "Why did the programmer refuse to use the new framework?",
        "answer": "He was afraid of commitment."
    },
    {
        "number": 52,
        "question": "What's a programmer's favorite animal?",
        "answer": "A Python."
    },
    {
        "number": 53,
        "question": "Why did the programmer break up with the database?",
        "answer": "It was too relational."
    },
    {
        "number": 54,
        "question": "What's a programmer's favorite song?",
        "answer": "'Don't Stop Me Now' by Queen, because it's about not having any breakpoints."
    },
    {
        "number": 55,
        "question": "Why did the programmer get lost in the forest?",
        "answer": "He took the wrong branch."
    },
    {
        "number": 56,
        "question": "What's a programmer's favorite type of tree?",
        "answer": "A binary tree."
    },
    {
        "number": 57,
        "question": "Why did the programmer get kicked out of the library?",
        "answer": "He was too loud when he was debugging."
    },
    {
        "number": 58,
        "question": "What's a programmer's favorite movie?",
        "answer": "'The Matrix', because it's all about code."
    },
    {
        "number": 59,
        "question": "Why did the programmer get a tattoo of a bug?",
        "answer": "He wanted to show his commitment to debugging."
    },
    {
        "number": 60,
        "question": "What's a programmer's favorite type of coffee?",
        "answer": "A Java."
    },
    {
        "number": 61,
        "question": "Why did the programmer get a job at the bakery?",
        "answer": "He wanted to work with cookies."
    },
    {
        "number": 62,
        "question": "What's a programmer's favorite type of car?",
        "answer": "A Tesla, because it's all about software."
    },
    {
        "number": 63,
        "question": "Why did the programmer get a job as a gardener?",
        "answer": "He wanted to work with root access."
    },
    {
        "number": 64,
        "question": "What's a programmer's favorite type of music?",
        "answer": "Heavy metal, because it's all about the hardware."
    },
    {
        "number": 65,
        "question": "Why did the programmer get a job at the zoo?",
        "answer": "He wanted to work with pythons."
    },
    {
        "number": 66,
        "question": "What's a programmer's favorite type of food?",
        "answer": "A byte-sized snack."
    },
    {
        "number": 67,
        "question": "Why did the programmer get a job as a chef?",
        "answer": "He wanted to work with APIs (Apple Pie Interfaces)."
    },
    {
        "number": 68,
        "question": "What's a programmer's favorite type of book?",
        "answer": "A manual."
    },
    {
        "number": 69,
        "question": "Why did the programmer get a job as a doctor?",
        "answer": "He wanted to work with patients (as in, have a lot of patience)."
    },
    {
        "number": 70,
        "question": "What's a programmer's favorite type of game?",
        "answer": "A sandbox game."
    },
    {
        "number": 71,
        "question": "Why did the programmer get a job as a pilot?",
        "answer": "He wanted to work with cloud computing."
    },
    {
        "number": 72,
        "question": "What's a programmer's favorite type of drink?",
        "answer": "A root beer."
    },
    {
        "number": 73,
        "question": "Why did the programmer get a job as a construction worker?",
        "answer": "He wanted to work with frameworks."
    },
    {
        "number": 74,
        "question": "What's a programmer's favorite type of shoe?",
        "answer": "A boot."
    },
    {
        "number": 75,
        "question": "Why did the programmer get a job as a librarian?",
        "answer": "He wanted to work with archives."
    },
    {
        "number": 76,
        "question": "What's a programmer's favorite type of plant?",
        "answer": "A java fern."
    },
    {
        "number": 77,
        "question": "Why did the programmer get a job as a musician?",
        "answer": "He wanted to work with chords (cords)."
    },
    {
        "number": 78,
        "question": "What's a programmer's favorite type of weather?",
        "answer": "A cloud."
    },
    {
        "number": 79,
        "question": "Why did the programmer get a job as a fisherman?",
        "answer": "He wanted to work with nets."
    },
    {
        "number": 80,
        "question": "What's a programmer's favorite type of art?",
        "answer": "ASCII art."
    },
    {
        "number": 81,
        "question": "Why did the programmer get a job as a comedian?",
        "answer": "He had a great sense of humor (or at least, he thought he did)."
    },
    {
        "number": 82,
        "question": "What's a programmer's favorite type of clothing?",
        "answer": "A hoodie."
    },
    {
        "number": 83,
        "question": "Why did the programmer get a job as a teacher?",
        "answer": "He wanted to work with classes."
    },
    {
        "number": 84,
        "question": "What's a programmer's favorite type of pet?",
        "answer": "A cat, because it's always purr-fecting its code."
    },
    {
        "number": 85,
        "question": "Why did the programmer get a job as a lawyer?",
        "answer": "He wanted to work with arguments."
    },
    {
        "number": 86,
        "question": "What's a programmer's favorite type of vacation?",
        "answer": "A trip to the cloud."
    },
    {
        "number": 87,
        "question": "Why did the programmer get a job as a detective?",
        "answer": "He was good at finding bugs."
    },
    {
        "number": 88,
        "question": "What's a programmer's favorite type of candy?",
        "answer": "A bit-o-honey."
    },
    {
        "number": 89,
        "question": "Why did the programmer get a job as a mailman?",
        "answer": "He wanted to work with addresses."
    },
    {
        "number": 90,
        "question": "What's a programmer's favorite type of sport?",
        "answer": "A sprint."
    },
    {
        "number": 91,
        "question": "Why did the programmer get a job as a waiter?",
        "answer": "He wanted to work with servers."
    },
    {
        "number": 92,
        "question": "What's a programmer's favorite type of holiday?",
        "answer": "A hackathon."
    },
    {
        "number": 93,
        "question": "Why did the programmer get a job as a writer?",
        "answer": "He wanted to work with scripts."
    },
    {
        "number": 94,
        "question": "What's a programmer's favorite type of fruit?",
        "answer": "A raspberry pi."
    },
    {
        "number": 95,
        "question": "Why did the programmer get a job as a mechanic?",
        "answer": "He wanted to work with engines."
    },
    {
        "number": 96,
        "question": "What's a programmer's favorite type of building?",
        "answer": "A library."
    },
    {
        "number": 97,
        "question": "Why did the programmer get a job as a politician?",
        "answer": "He was good at making promises."
    },
    {
        "number": 98,
        "question": "What's a programmer's favorite type of furniture?",
        "answer": "A table."
    },
    {
        "number": 99,
        "question": "Why did the programmer get a job as a baker?",
        "answer": "He wanted to work with dough (DOM)."
    },
    {
        "number": 100,
        "question": "What's a programmer's favorite type of dance?",
        "answer": "The algorithm."
    },
    {
        "number": 101,
        "question": "Why did the programmer get a job as a security guard?",
        "answer": "He was good at protecting against attacks."
    },
    {
        "number": 102,
        "question": "What's a programmer's favorite type of party?",
        "answer": "A LAN party."
    },
    {
        "number": 103,
        "question": "Why did the programmer get a job as a scientist?",
        "answer": "He wanted to work with experiments."
    },
    {
        "number": 104,
        "question": "What's a programmer's favorite type of flower?",
        "answer": "A rose, because it has thorns (bugs)."
    },
    {
        "number": 105,
        "question": "Why did the programmer get a job as a judge?",
        "answer": "He was good at making decisions."
    },
    {
        "number": 106,
        "question": "What's a programmer's favorite type of movie genre?",
        "answer": "A thriller, because it's full of suspense (suspenseful code)."
    },
    {
        "number": 107,
        "question": "Why did the programmer get a job as a historian?",
        "answer": "He was good at looking at logs."
    },
    {
        "number": 108,
        "question": "What's a programmer's favorite type of musical instrument?",
        "answer": "A keyboard."
    },
    {
        "number": 109,
        "question": "Why did the programmer get a job as a spy?",
        "answer": "He was good at hiding things."
    },
    {
        "number": 110,
        "question": "What's a programmer's favorite type of weapon?",
        "answer": "A laser, because it's all about focus."
    },
    {
        "number": 111,
        "question": "Why did the programmer get a job as a philosopher?",
        "answer": "He was good at thinking about abstract concepts."
    },
    {
        "number": 112,
        "question": "What's a programmer's favorite type of animal?",
        "answer": "A bug."
    },
    {
        "number": 113,
        "question": "Why did the programmer get a job as a farmer?",
        "answer": "He wanted to work with fields."
    },
    {
        "number": 114,
        "question": "What's a programmer's favorite type of drink?",
        "answer": "A mocktail, because it's just a mock object."
    },
    {
        "number": 115,
        "question": "Why did the programmer get a job as a lifeguard?",
        "answer": "He was good at saving people from drowning in technical debt."
    },
    {
        "number": 116,
        "question": "What's a programmer's favorite type of transportation?",
        "answer": "A bus."
    },
    {
        "number": 117,
        "question": "Why did the programmer get a job as a tailor?",
        "answer": "He was good at making things fit."
    },
    {
        "number": 118,
        "question": "What's a programmer's favorite type of weather?",
        "answer": "A storm, because it's all about the cloud."
    },
    {
        "number": 119,
        "question": "Why did the programmer get a job as a zookeeper?",
        "answer": "He was good at handling wild animals (bugs)."
    },
    {
        "number": 120,
        "question": "What's a programmer's favorite type of food?",
        "answer": "A sandwich, because it's a stack."
    },
    {
        "number": 121,
        "question": "Why did the programmer get a job as a librarian?",
        "answer": "He was good at organizing things."
    },
    {
        "number": 122,
        "question": "What's a programmer's favorite type of tree?",
        "answer": "A git tree."
    },
    {
        "number": 123,
        "question": "Why did the programmer get a job as a chef?",
        "answer": "He was good at following recipes (algorithms)."
    },
    {
        "number": 124,
        "question": "What's a programmer's favorite type of book?",
        "answer": "A cookbook, because it's full of recipes (algorithms)."
    },
    {
        "number": 125,
        "question": "Why did the programmer get a job as a doctor?",
        "answer": "He was good at diagnosing problems."
    },
    {
        "number": 126,
        "question": "What's a programmer's favorite type of game?",
        "answer": "A puzzle game, because it's all about solving problems."
    },
    {
        "number": 127,
        "question": "Why did the programmer get a job as a pilot?",
        "answer": "He was good at navigating."
    },
    {
        "number": 128,
        "question": "What's a programmer's favorite type of drink?",
        "answer": "A smoothie, because it's a mix of different things."
    },
    {
        "number": 129,
        "question": "Why did the programmer get a job as a construction worker?",
        "answer": "He was good at building things."
    },
    {
        "number": 130,
        "question": "What's a programmer's favorite type of shoe?",
        "answer": "A boot, because it's a good way to start things up."
    },
    {
        "number": 131,
        "question": "Why did the programmer get a job as a librarian?",
        "answer": "He was good at finding things."
    },
    {
        "number": 132,
        "question": "What's a programmer's favorite type of plant?",
        "answer": "A cactus, because it's low-maintenance."
    },
    {
        "number": 133,
        "question": "Why did the programmer get a job as a musician?",
        "answer": "He was good at composing things."
    },
    {
        "number": 134,
        "question": "What's a programmer's favorite type of weather?",
        "answer": "A sunny day, because there are no clouds in the sky."
    },
    {
        "number": 135,
        "question": "Why did the programmer get a job as a fisherman?",
        "answer": "He was good at catching things."
    },
    {
        "number": 136,
        "question": "What's a programmer's favorite type of art?",
        "answer": "A masterpiece, because it's a work of art."
    },
    {
        "number": 137,
        "question": "Why did the programmer get a job as a comedian?",
        "answer": "He was good at making people laugh."
    },
    {
        "number": 138,
        "question": "What's a programmer's favorite type of clothing?",
        "answer": "A t-shirt with a funny slogan."
    },
    {
        "number": 139,
        "question": "Why did the programmer get a job as a teacher?",
        "answer": "He was good at explaining things."
    },
    {
        "number": 140,
        "question": "What's a programmer's favorite type of pet?",
        "answer": "A dog, because it's always loyal."
    },
    {
        "number": 141,
        "question": "Why did the programmer get a job as a lawyer?",
        "answer": "He was good at arguing."
    },
    {
        "number": 142,
        "question": "What's a programmer's favorite type of vacation?",
        "answer": "A staycation, because he can code from home."
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

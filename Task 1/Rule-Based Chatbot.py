import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there","Hi",]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot!",]
    ],
    [
        r"how are you?",
        ["I'm fine, thank you!, how can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you?",
        ["i am looking for an online guides and courses to learn python and machine learning",]
    ],
    [
        r"i am looking for an online guides and courses to learn python and machine learning",
        ["You can check udemy","You can check coursera","You can check Youtube for tutorials",]
    ],
    [
        r"i'm (.*) doing great.",
        ["That's great to hear","How can i help you",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help","No problem","You're welcome",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)","It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi I am a Rule-Based Chatbot! What can i do for you?")
    
chat = Chat(set_pairs,reflections)

chat.converse()
if __name__ == "__main__":
    chatbot()


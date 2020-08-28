'''import sys
import random

question = input("Ask the magic 8 ball a question: ")

def answer():

    answers = random.randint(1, 20)

    if answers == 1:
        return "As I see it, yes."

    elif answers == 2:
        return "Ask again later."

    elif answers == 3:
        return "Better not tell you now."

    elif answers == 4:
        return "Cannot predict now."

    elif answers == 5:
        return "Concentrate and ask again"

    elif answers == 6:
        return "Don’t count on it."

    elif answers == 7:
        return "It is certain."

    elif answers == 8:
        return "It is decidedly so."

    elif answers == 9:
        return "Most likely."

    elif answers == 10:
        return "My reply is no."

    elif answers == 11:
        return "My sources say no."

    elif answers == 12:
        return "Outlook not so good."

    elif answers == 13:
        return "Outlook good."

    elif answers == 14:
        return "Reply hazy, try again."

    elif answers == 15:
        return "Signs point to yes."

    elif answers == 16:
        return "Very doubtful."

    elif answers == 17:
        return "Without a doubt."

    elif answers == 18:
        return "Yes."

    elif answers == 19:
        return "Yes – definitely."

    elif answers == 20:
        return "You may rely on it."

    else:
        return "Magic is lost..."

print(answer())'''

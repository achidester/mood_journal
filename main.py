# Mood Journal App


from cProfile import label
from tkinter import *
import random

# Mood arrays 
negative_moods = ['sad', 'cranky', 'depressed', 'mad', 'bored', 'meh', 'scared','bad', 'down', 'terrible']
positive_moods = ['happy', 'super', 'excited', 'peachy', 'silly', 'great', 'loved', 'giddy']

negative_prompts = ['What little thing can you do to improve your mood right now?', 'Where would you go if you could go anywhere?', 'Is there anything you can learn from this?', 'What upset you today?']
positive_prompts = ['What made you smile today?',  'What was your favorite thing about today?', 'Did something make you laugh?', 'What do you want to remember about today?', 'What song makes you happy?']

both_prompts = negative_prompts + positive_prompts

#I watched this video for all tkinter (https://www.youtube.com/watch?v=YXPyB4XeYLA)
window = Tk()
window.configure(bg='white')
window.geometry('630x600')
window.resizable(0,0)


def moodEntry(event=None):
    reaction_string = "So you are feeling " + user_mood.get() + " today"
    reaction_label = Label(window, bg="white", pady=5, text=reaction_string)
    reaction_label.pack()
    mood_button['state'] = DISABLED # you can only hit the button once

    if user_mood.get() in negative_moods:
        response_string = "Well I hope you feel better soon."
        mood = 'bad'
    elif user_mood.get() in positive_moods:
        response_string = "That is great news!"
        mood = 'good'
    else:
        response_string = "I guess I dont know how that feels."
        mood = 'null'

    response_label = Label(window, bg="white", pady=5, text=response_string)
    response_label.pack()
    writingPrompts(mood)

def promptEntry(event=None):
    reaction_string = Label(window, bg="white", pady=5, text="Okay I will generate your journal post for today")
    reaction_string.pack()
    

def writingPrompts(mood):
    prompts_label = Label(window, bg="white", pady=5, text="Here is a writing prompt based off your mood... ")
    prompts_label.pack()

    if mood == 'bad':
        random_number = random.randint(1, len(negative_prompts))
        actual_prompt = Label(window, bg="white", pady=5, text=negative_prompts[random_number])
    elif mood == 'good':
        random_number = random.randint(1, len(positive_prompts))
        actual_prompt = Label(window, bg="white", pady=5, text=positive_prompts[random_number])
    else:
        random_number = random.randint(1, len(both_prompts))
        actual_prompt = Label(window, bg="white", pady=5, text=both_prompts[random_number])

    actual_prompt.pack()
    
    window.bind('<Return>', promptEntry)
    userPromptResponse()


def userPromptResponse():
    user_response = Entry(window, width=20)
    response_button = Button(window, bg="white",text="Enter journal entry", command=promptEntry)
    user_response.pack()
    response_button.pack()
    window.bind('<Return>', None)


# Top logo
canvas = Canvas(window, width=630, height=200, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(330,100,image=img)
canvas.pack(side=TOP)


# intro question
introduction = Label(window, bg="white", text ='How are you feeling today?')
introduction.pack()

# user_mood entry
user_mood = Entry(window, width=20)
user_mood.pack()

window.bind('<Return>', moodEntry)

mood_button = Button(window, bg="white", text="Enter mood", command=moodEntry)
mood_button.pack()
window.mainloop()

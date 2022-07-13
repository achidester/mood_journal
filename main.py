# Mood Journal App
#I used this video as a tkinter resource (https://www.youtube.com/watch?v=YXPyB4XeYLA)

from cProfile import label
from tkinter import *
import random, datetime

# Mood arrays 
negative_moods = ['sad', 'cranky', 'depressed', 'mad', 'bored', 'meh', 'scared','bad', 'down', 'terrible']
positive_moods = ['happy', 'super', 'excited', 'peachy', 'silly', 'great', 'loved', 'giddy']

negative_prompts = ['What little thing can you do to improve your mood right now?', 'Where would you go if you could go anywhere?', 'What can you learn from today?', 'What upset you today?']
positive_prompts = ['What made you smile today?',  'What was your favorite thing about today?', 'Did something make you laugh?', 'What do you want to remember about today?']

both_prompts = negative_prompts + positive_prompts

# tkinter "canvas" window
window = Tk()
window.configure(bg='white')
window.geometry('630x450')
window.resizable(0,0)


# continue button will clear the intro and pipe to mood entry
def continueButton(event=None):
    intro.destroy()
    continue_button.destroy()
    moodQuestion()

def moodQuestion():
    global user_mood, mood_button, intro_question

    intro_question = Label(window, bg="white", text ="In one word, tell me how you're feeling today")
    intro_question.pack()
    # user_mood entry
    user_mood = Entry(window, width=20)
    user_mood.pack()
    mood_button = Button(window, bg="white", text="Enter mood", command=moodEntered) 
    mood_button.pack()
    window.bind('<Return>', moodEntered)


def moodEntered(event=None):
    global reaction_label, response_label, mood

    intro_question.pack_forget()
    user_mood.pack_forget()
    mood_button.pack_forget()

    reaction_string = "So you are feeling " + user_mood.get() + " today"
    reaction_label = Label(window, bg="white", pady=5, text=reaction_string)
    reaction_label.pack()

    if user_mood.get() in negative_moods:
        response_string = "Well, I hope you feel better soon."
        mood = 'bad'
    elif user_mood.get() in positive_moods:
        response_string = "That is great news!"
        mood = 'good'
    else:
        response_string = "I guess I dont know how that feels."
        mood = 'null'

    response_label = Label(window, bg="white", pady=5, text=response_string)
    response_label.pack()
    writingPrompts()
    
def writingPrompts():
    global prompts_label, actual_prompt

    prompts_label = Label(window, bg="white", pady=5, text="Here is a writing prompt based off your mood... ")
    prompts_label.pack()

    if mood == 'bad':
        random_number = random.randint(0, len(negative_prompts)-1)
        actual_prompt = Label(window, bg="white", pady=5, text=negative_prompts[random_number])
    elif mood == 'good':
        random_number = random.randint(0, len(positive_prompts)-1)
        actual_prompt = Label(window, bg="white", pady=5, text=positive_prompts[random_number])
    else:
        random_number = random.randint(0, len(both_prompts)-1)
        actual_prompt = Label(window, bg="white", pady=5, text=both_prompts[random_number])
    actual_prompt.pack()
    
    window.bind('<Return>', promptEntry)
    userPromptResponse()


def userPromptResponse():
    global user_response, response_button
    user_response = Entry(window, width=80)
    response_button = Button(window, bg="white",text="Create journal entry", command=promptEntry)
    user_response.pack()
    response_button.pack()
    window.bind('<Return>', None)

def promptEntry(event=None):
    user_response.pack_forget()
    response_button.pack_forget()
    reaction_label.pack_forget()
    response_label.pack_forget()
    prompts_label.pack_forget()
    actual_prompt.pack_forget()
    
    reaction_string = Label(window, bg="white", pady=5, text="Here is your journal post for today")
    reaction_string.pack()
    journalPage()

    
def journalPage(event=None):
    global mood_image
    journal_page = Toplevel()
    journal_page.configure(bg='white')
    journal_page.geometry("522x400")

    mood_canvas = Canvas(journal_page, width=522, height=227, bg="white")

    if mood == 'bad':
        mood_image = PhotoImage(file="sad.png")
    elif mood == 'good':
        mood_image = PhotoImage(file="happy.png")
    else:
        mood_image = PhotoImage(file="unknown.png")

    mood_canvas.create_image(0,0, anchor=NW, image=mood_image)
    mood_canvas.pack(side=TOP)

    todays_date = str(datetime.date.today())

    date = Label(journal_page, bg="white", padx=15, text ='Date: ' + todays_date, font=25)
    date.pack()

    journal_mood = Label(journal_page, bg="white", padx=15, text ='Today I was feeling ' + user_mood.get(), font=25)
    journal_mood.pack()

    journal_prompt = Label(journal_page, bg="white", padx=15, text=actual_prompt.cget("text"), font=25)
    journal_prompt.pack()

    journal_entry = Label(journal_page, bg="white", padx=15, text=user_response.get(), font=25)
    journal_entry.pack()


# Top logo
logo_canvas = Canvas(window, width=630, height=200, bg="white")
img = PhotoImage(file="logo.png")
logo_canvas.create_image(330,100,image=img)
logo_canvas.pack(side=TOP)

# intro page
intro = Label(window, bg="white", padx=15, text ='Welcome to the mood journal. \n Tell me how you feel today and I will give you a prompt based off your mood', font=25)
intro.pack()
continue_button = Button(window, bg="white", text="Let's start", command=continueButton)
continue_button.pack()
window.bind('<Return>', continueButton)



window.mainloop()

# Mood Journal App


import tkinter as tk

#I watched this video for all tkinter (https://www.youtube.com/watch?v=YXPyB4XeYLA)
window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=500)
canvas.grid(columnspan=5)
img = tk.PhotoImage(file="logo.png")
img.subsample(20,20)
canvas.create_image(400,100,image=img)


#possibly break this into smaller hashes that will help the computer respond in certain ways based on mood.
mood_hash = {
    "sad": "\nSurely tomorrow will be better",
    "happy": "\nThat's great news!",
    "meh": "\nNot very happy, or very sad just kind of meh?"
}


print("How are you feeling today?", f"\n")

user_mood = input()

#responding to the mood
#else: ask user to describe it (add mood to the hash table) !Microservice needed to dynamically add things to hash!

if user_mood in mood_hash:
    print(mood_hash[user_mood], f"\n")
else:
    print("I haven't heard that one, what does it feel like?")
    mood_value = input()
    mood_hash[user_mood] = mood_value


print("Here are some journal writing prompts for today...", f"\n")
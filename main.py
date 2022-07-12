mood_hash = {
    "sad": "\nSurely tomorrow will be better",
    "happy": "\nThat's great news!",
    "meh": "\nNot very happy, or very sad just kind of meh?"
}


print("How are you feeling today?", f"\n")

user_mood = input()

print(mood_hash[user_mood], f"\n")

print("Here are some journal writing prompts for today...", f"\n")
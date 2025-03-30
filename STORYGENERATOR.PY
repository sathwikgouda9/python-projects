def storybuilder():
    print("Welcome to story generator! ")
    print("pkease enter details to get your story")
    day = input("Enter day/Evening / night: ")
    mood = input("Enter your mood: ")
    reason = input("reason for the mood ")
    time = int(input("Enter time (0-23 only): "))
    character = input("Girl/Boy")
    gender = input("she/he")
    pronoun = input("him/her")
    town = input("Town: ")
    story = f"""
    On a fine {day}, our {character} visted {town} where {gender} met {pronoun} grandmother who is {mood} 
    {gender} asked the why are you {mood} grandmother told {pronoun} that {reason} as they were discussing time went by and it's {time}'O clock
       """
    print(story)
storybuilder()
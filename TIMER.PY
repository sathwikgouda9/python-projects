#THIS PROJECT IS ABOUT A SIMPLE COUNTDOWN TIMER THAT TAKES INPUT IN SECONDS AND DISPLAYS THE TIME LEFT IN HH:MM:SS FORMAT.
import time
def timer(seconds):
    while seconds:
        hrs, rem = divmod(seconds, 3600)
        mins, secs = divmod(rem, 60)
        print(f"\r Time Left: {hrs:02}:{mins:02}:{secs:02}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")
try:
    total_seconds = int(input("Enter countdown time in seconds: "))
    timer(total_seconds)
except ValueError:
    print("Invalid integer.")

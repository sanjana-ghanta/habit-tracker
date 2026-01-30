habit = input("What habit are you tracking? ").strip()

while True:
    done = input("Did you complete it today? (y/n) ").strip().lower()
    if done in ("y", "n"):
        break
    print("Please enter 'y' or 'n'.")

if done == "y":
    print(f"Yay! Great job sticking to your {habit}!")
else:
    print(f"It's okay, tomorrow is a fresh start!")

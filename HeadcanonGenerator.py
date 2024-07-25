import tkinter
import random

root = tkinter.Tk()
root.geometry("600x600")
root.title("Headcanon Generator")
root.configure(bg = "green")

header = tkinter.Label(root, text = "Headcanon Generator", bg = "green", font = "Copperplate_Gothic_Light 17")
header.pack()

name = tkinter.StringVar()

input = tkinter.Entry(root, border = "3", textvariable = name)
input.pack()

def get_name():
  printed_name = name.get()
  headcanon = random.choice(headcanon_list)
  headcanon_text = tkinter.Label(text = f"{printed_name} {headcanon}", bg = "green")
  headcanon_text.pack()

headcanon_list = ["is a big bookworm", "can't spell gorgeous", "swallowed a penny before", "is deathly afraid of bugs",
"makes dad jokes", "has tea parties with barbies", "cries during horror movies", "hates sugary cereals", "used to bark and/or hiss at people",
"hates being sick and adamantly denies it", "cries if an animal dies in a movie", "sleep talks", "snores", "sleep walks","hates kids",
"loves kids (not in the drake/kris/diddy/dr disrespect/dream way)", "has a really big appetite", "has a really small appetite", "has an odd obsession with the 4th of July",
"pays for a streaming service but still pirates movies", "stole their parents' car before", "cannot stay up to save their life", "hates going outside",
"is excessively brainrotted (skibidi, sigma, ohio, mewing)", "randomly references internet memes that you either do or don't get", "obsessed with the movie Frozen",
"never sleeps at all", "runs off pure caffeine", "hates long-sleeved shirts", "always talks about the power of friendship (ironically)", "always talks about the power of friendship (unironically)",
"uses emoticons more than emojis", "is always hungry", "is never hungry", "talks to their pets in a babyish voice", "constantly closes and opens the fridge to check if something to eat appeared"]

button = tkinter.Button(root, text = "Generate Headcanon", command = get_name)
button.pack()

root.mainloop()
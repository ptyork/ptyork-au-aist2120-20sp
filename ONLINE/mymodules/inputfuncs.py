default_prompt = "Enter: "

def get_text(prompt):
    while True:
        text = input(prompt)
        text = text.strip()
        if len(text) == 0:
            print('Entry cannot be blank')
            continue
        return text

def get_int(prompt):
    while True:
        text = get_text(prompt)
        try:
            num = int(text)
            return num
        except:
            print("Entry must be a number")
            continue

#print(__name__)  # will be "__main__" if running interactively, otherwise name
                 # of the module (mod)
if __name__ == "__main__":
    print("You're running the mod.py directly")
    print("TESTING STUFF....")


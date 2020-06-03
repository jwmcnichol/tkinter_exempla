from tkinter import Tk, Label, Button, Entry


class MainBox:

    def __init__(self, start_box):
        self.start_box = start_box
        start_box.title('The main frame')

        self.label = Button(start_box, text="First number", command=get_attack_skill())
        self.label.pack()
        self.retrieve_box = 1
        self.enter_attack_value = Entry(start_box, text='Enter attack.value')
        self.enter_attack_value.pack()

    def retrieve_input():
        self.myText_Box =
        input = self.myText_Box.get("1.0", 'end-1c') #line 1 index 0
        return input


class Getters:

    def get_attack_skill():
        skill_dice = int(input('Enter attacker skill rating: '))
        return skill_dice


root = Tk()
my_gui = MainBox(root)
root.mainloop()
import tkinter as tk
from tkinter import messagebox

class GameInterface:
    """
    A class to represent the game interface for "Escape the Prison".
    Attributes
    ----------
    root : tk.Tk
        The root window of the Tkinter application.
    text_area : tk.Text
        The text area widget to display game text.
    choice_frame : tk.Frame
        The frame to hold choice buttons.
    choice_buttons : list of tk.Button
        A list of buttons for player choices.
    current_function : function
        The current game function being executed.
    Methods
    -------
    __init__(root):
        Initializes the game interface.
    create_widgets():
        Creates and packs the widgets for the game interface.
    start_game():
        Starts the game with an introductory message and initial action.
    display_text(text):
        Displays the given text in the text area.
    clear_text():
        Clears the text area.
    update_choices(choices):
        Updates the choice buttons with the given choices.
    on_choice(choice):
        Handles the player's choice and calls the appropriate action function.
    cell_action():
        Displays the initial cell action choices.
    cell_action_choice(choice):
        Handles the player's choice for the cell action.
    vent_action():
        Displays the vent action choices.
    vent_action_choice(choice):
        Handles the player's choice for the vent action.
    key_action():
        Displays the key action choices.
    key_action_choice(choice):
        Handles the player's choice for the key action.
    hallway_action():
        Displays the hallway action choices.
    hallway_action_choice(choice):
        Handles the player's choice for the hallway action.
    armory_action():
        Displays the armory action choices.
    armory_action_choice(choice):
        Handles the player's choice for the armory action.
    secret_tunnel_action():
        Displays the secret tunnel action choices.
    secret_tunnel_action_choice(choice):
        Handles the player's choice for the secret tunnel action.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Escape the Prison")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, height=20, width=100)
        self.text_area.pack(pady=10)

        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=10)

        self.choice_buttons = []
        for i in range(3):
            button = tk.Button(self.choice_frame, text=f"Choice {i+1}", command=lambda i=i: self.on_choice(i+1))
            button.pack(side=tk.LEFT, padx=5)
            self.choice_buttons.append(button)

        self.start_game()

    def start_game(self):
        self.display_text("Welcome to Escape the Prison!\nYour goal is to escape without getting caught. Choose wisely!")
        self.cell_action()

    def display_text(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def update_choices(self, choices):
        for i, choice in enumerate(choices):
            if i < len(self.choice_buttons):
                self.choice_buttons[i].config(text=choice, state=tk.NORMAL)
            else:
                button = tk.Button(self.choice_frame, text=choice, command=lambda i=i: self.on_choice(i+1))
                button.pack(side=tk.LEFT, padx=5)
                self.choice_buttons.append(button)
        for j in range(i+1, len(self.choice_buttons)):
            self.choice_buttons[j].pack_forget()

    def on_choice(self, choice):
        if self.current_function == self.cell_action:
            self.cell_action_choice(choice)
        elif self.current_function == self.vent_action:
            self.vent_action_choice(choice)
        elif self.current_function == self.key_action:
            self.key_action_choice(choice)
        elif self.current_function == self.hallway_action:
            self.hallway_action_choice(choice)
        elif self.current_function == self.armory_action:
            self.armory_action_choice(choice)
        elif self.current_function == self.secret_tunnel_action:
            self.secret_tunnel_action_choice(choice)

    def cell_action(self):
        self.current_function = self.cell_action
        self.display_text("\nYou wake up in your prison cell. The door is locked, but you see a vent above and hear footsteps outside.\n\nWhat do you do ?")
        choices = ["Shout for help", "Try to open the vent", "Wait and listen"]
        self.update_choices(choices)

    def cell_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nYou shout for help, but a guard hears you and comes to check. You're caught! Game Over.")
            messagebox.showinfo("Game Over", "You're caught! Game Over.")
            self.root.quit()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nYou manage to open the vent and crawl into the air ducts.")
            self.vent_action()
        elif choice == 3:
            self.clear_text()
            self.display_text("\nYou wait and listen. A guard passes by, and you hear him muttering about a missing key.")
            self.display_text("You notice a key hanging from his belt.")
            self.key_action()

    def vent_action(self):
        self.current_function = self.vent_action
        self.display_text("\nYou crawl through the vents and reach a junction.\n\nWhere do you go ?")
        choices = ["Go left (towards the kitchen)", "Go right (towards the armory)"]
        self.update_choices(choices)

    def vent_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nYou reach the kitchen and find a knife. A cook sees you and raises the alarm. Game Over.")
            messagebox.showinfo("Game Over", "You're caught! Game Over.")
            self.root.quit()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nYou reach the armory and find a guard's uniform. You put it on and continue exploring the prison.")
            self.armory_action()

    def key_action(self):
        self.current_function = self.key_action
        self.display_text("\nYou decide to take the key from the guard.\n\nWhat do you do ?")
        choices = ["Pickpocket the key quietly", "Distract the guard and grab the key"]
        self.update_choices(choices)

    def key_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nYou quietly take the key and unlock your cell. You sneak out and find yourself in a hallway.")
            self.hallway_action()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nYou try to distract the guard, but he notices you and calls for backup. You're caught! Game Over.")
            messagebox.showinfo("Game Over", "You're caught! Game Over.")
            self.root.quit()

    def hallway_action(self):
        self.current_function = self.hallway_action
        self.display_text("\nYou are in a dimly lit hallway. There are two paths ahead.\n\nWhere do you go ?")
        choices = ["Go left (towards the warden's office)", "Go right (towards the exit)"]
        self.update_choices(choices)

    def hallway_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nYou sneak into the warden's office and find a map of the prison. It shows a secret tunnel leading outside.")
            self.secret_tunnel_action()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nYou head towards the exit but encounter a locked door with a keypad. Without the code, you can't proceed. You're caught by guards! Game Over.")
            messagebox.showinfo("Game Over", "You're caught! Game Over.")
            self.root.quit()

    def armory_action(self):
        self.current_function = self.armory_action
        self.display_text("\nDressed as a guard, you move freely through the prison. You overhear two guards talking about a supply truck leaving soon.\n\nWhat do you do ?")
        choices = ["Head to the truck loading area", "Investigate the warden's office"]
        self.update_choices(choices)

    def armory_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nYou reach the truck loading area and hide in the back of a supply truck. The truck leaves the prison. You escaped! Congratulations!")
            messagebox.showinfo("Congratulations", "You escaped! Congratulations!")
            self.root.quit()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nYou sneak into the warden's office and find a map of the prison. It shows a secret tunnel leading outside.")
            self.secret_tunnel_action()

    def secret_tunnel_action(self):
        self.current_function = self.secret_tunnel_action
        self.display_text("\nYou follow the map to the secret tunnel. It's dark and filled with obstacles.\n\nWhat do you do ?")
        choices = ["Use a flashlight you found in the armory", "Proceed carefully in the dark"]
        self.update_choices(choices)

    def secret_tunnel_action_choice(self, choice):
        if choice == 1:
            self.clear_text()
            self.display_text("\nUsing the flashlight, you navigate the tunnel safely and find an exit leading to freedom. You escaped! Congratulations!")
            messagebox.showinfo("Congratulations", "You escaped! Congratulations!")
            self.root.quit()
        elif choice == 2:
            self.clear_text()
            self.display_text("\nIn the dark, you trip over a rock and make noise. Guards discover the tunnel and catch you. Game Over.")
            messagebox.showinfo("Game Over", "You're caught! Game Over.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameInterface(root)
    root.mainloop()

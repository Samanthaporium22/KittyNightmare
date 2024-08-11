from browser import document

def run_game():
    user_input = document["user_input"].value
    document["game_output"].text = f"Hello, {user_input}! Welcome to Kitty's Worst Nightmare!"


class AsciiArt:
    def __init__(self):
        self.fishless_world = """
             _   _      _ _        
            | | | |    | | |       
            | |_| | ___| | | ___   
            |  _  |/ _ \ | |/ _ \  
            | | | |  __/ | | (_) | 
            \_| |_/\___|_|_|\___/  

        """

        self.kitty = """
           |\---/|
           | o_o |
            \_^_/
        """

    def get_fishless_world(self):
        return self.fishless_world

    def get_kitty(self):
        return self.kitty


class Kitty:
    def __init__(self):
        self.name = "Whiskers"
        self.brave = False

    def set_brave(self, brave: bool):
        self.brave = brave


class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What do kitties love to eat the most?",
                "options": ["1. Fish", "2. Carrots", "3. Lettuce"],
                "answer": "1"
            },
            {
                "question": "How many lives do kitties have?",
                "options": ["1. 1", "2. 7", "3. 9"],
                "answer": "3"
            }
        ]

    def ask_quiz(self):
        for q in self.questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Your answer (enter the number): ")
            if answer == q["answer"]:
                print("Correct!")
            else:
                print("Wrong answer!")


class Scene:
    def __init__(self, description: str, ascii_art: str):
        self.description = description
        self.ascii_art = ascii_art

    def show(self):
        print(self.ascii_art)
        print(self.description)


class Game:
    def __init__(self):
        self.kitty = Kitty()
        self.ascii_art = AsciiArt()
        self.quiz = Quiz()

    def start(self):
        print(self.ascii_art.get_fishless_world())
        print("Welcome to Kitty's Worst Nightmare!")
        print(f"{self.kitty.name} has woken up to a terrible realization...")
        print("There are no fish left in the world!")

        self.scene1()

    def scene1(self):
        scene_description = """
        Whiskers looks around in disbelief. No fish in sight, anywhere!
        Whiskers must be brave to solve this mystery. Will Whiskers be brave?
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        choice = input("Will Whiskers be brave? (yes/no): ").strip().lower()

        if choice == "yes":
            self.kitty.set_brave(True)
            print("\nWhiskers decides to be brave!")
            self.scene2()
        else:
            print("\nWhiskers decides to stay safe at home. But the fish won't come back by themselves...")
            self.end_game()

    def scene2(self):
        scene_description = """
        Whiskers ventures out into the unknown world. The path splits into two:
        One path leads to the mysterious forest, the other to the dark cave.
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        choice = input("Which path will Whiskers take? (forest/cave): ").strip().lower()

        if choice == "forest":
            print("\nWhiskers heads to the forest.")
            self.quiz.ask_quiz()
        elif choice == "cave":
            print("\nWhiskers heads into the cave.")
            self.scene3()
        else:
            print("\nWhiskers is confused and decides to go back home.")
            self.end_game()

    def scene3(self):
        scene_description = """
        Inside the dark cave, Whiskers finds a magic fish bone.
        It's glowing with a strange light. Should Whiskers take it?
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        choice = input("Take the magic fish bone? (yes/no): ").strip().lower()

        if choice == "yes":
            print("\nWhiskers takes the magic fish bone and suddenly... all the fish return to the world!")
            self.win_game()
        else:
            print("\nWhiskers decides to leave the bone. The fish remain lost forever...")
            self.end_game()

    def win_game(self):
        print("\nCongratulations! Whiskers has restored the fish to the world!")
        print(self.ascii_art.get_kitty())
        print("The End.")

    def end_game(self):
        print("\nThe adventure ends here. Better luck next time!")
        print(self.ascii_art.get_kitty())


# To start the game
#if __name__ == "__main__":
#    game = Game()
#    game.start()


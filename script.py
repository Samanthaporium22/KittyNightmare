from browser import document, html

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


class Scene:
    def __init__(self, description: str, ascii_art: str):
        self.description = description
        self.ascii_art = ascii_art

    def show(self):
        # Output to a div in the HTML
        output_div = document["game_output"]
        output_div.clear()
        output_div <= html.P(self.ascii_art)
        output_div <= html.P(self.description)


class Game:
    def __init__(self):
        self.kitty = Kitty()
        self.ascii_art = AsciiArt()

    def start(self):
        output_div = document["game_output"]
        output_div <= html.P(self.ascii_art.get_fishless_world())
        output_div <= html.P("Welcome to Kitty's Worst Nightmare!")
        output_div <= html.P(f"{self.kitty.name} has woken up to a terrible realization...")
        output_div <= html.P("There are no fish left in the world!")
        self.scene1()

    def scene1(self):
        scene_description = """
        Whiskers looks around in disbelief. No fish in sight, anywhere!
        Whiskers must be brave to solve this mystery. Will Whiskers be brave?
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        # Set up button interaction for the next choice
        brave_button = document["brave_button"]
        brave_button.bind("click", self.brave_choice)

        scared_button = document["scared_button"]
        scared_button.bind("click", self.scared_choice)

    def brave_choice(self, event):
        self.kitty.set_brave(True)
        document["game_output"] <= html.P("\nWhiskers decides to be brave!")
        self.scene2()

    def scared_choice(self, event):
        document["game_output"] <= html.P("\nWhiskers decides to stay safe at home. But the fish won't come back by themselves...")
        self.end_game()

    def scene2(self):
        scene_description = """
        Whiskers ventures out into the unknown world. The path splits into two:
        One path leads to the mysterious forest, the other to the dark cave.
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        # Set up interaction for choosing the path
        forest_button = document["forest_button"]
        forest_button.bind("click", self.forest_path)

        cave_button = document["cave_button"]
        cave_button.bind("click", self.cave_path)

    def forest_path(self, event):
        document["game_output"] <= html.P("\nWhiskers heads to the forest.")
        document["game_output"] <= html.P("No further implementation of the forest scene yet...")

    def cave_path(self, event):
        document["game_output"] <= html.P("\nWhiskers heads into the cave.")
        self.scene3()

    def scene3(self):
        scene_description = """
        Inside the dark cave, Whiskers finds a magic fish bone.
        It's glowing with a strange light. Should Whiskers take it?
        """
        scene = Scene(scene_description, self.ascii_art.get_kitty())
        scene.show()

        take_button = document["take_button"]
        take_button.bind("click", self.take_fish_bone)

        leave_button = document["leave_button"]
        leave_button.bind("click", self.leave_fish_bone)

    def take_fish_bone(self, event):
        document["game_output"] <= html.P("\nWhiskers takes the magic fish bone and suddenly... all the fish return to the world!")
        self.win_game()

    def leave_fish_bone(self, event):
        document["game_output"] <= html.P("\nWhiskers decides to leave the bone. The fish remain lost forever...")
        self.end_game()

    def win_game(self):
        document["game_output"] <= html.P("\nCongratulations! Whiskers has restored the fish to the world!")
        document["game_output"] <= html.P(self.ascii_art.get_kitty())
        document["game_output"] <= html.P("The End.")

    def end_game(self):
        document["game_output"] <= html.P("\nThe adventure ends here. Better luck next time!")
        document["game_output"] <= html.P(self.ascii_art.get_kitty())


# Start the game when the button is clicked
def start_game(event):
    game = Game()
    game.start()

# Bind the start game function to the button
document["start_button"].bind("click", start_game)

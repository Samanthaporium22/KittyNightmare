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
        One path leads to the mysterious forest, the other

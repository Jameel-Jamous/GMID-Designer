class Option:
    """A template for generating executable Options for a Menu."""
    def __init__(self, name, action):
        self.name = name
        self.actionCB = action

    def execute(self):
        return self.actionCB()

class Menu:
    """A class and template for creating a Menu"""
    def __init__(self, title):
        self.title = title
        self.options = {}
    
    def add_option(self, key : str, option : Option):
        """Adds options to the Menu"""
        self.options[key] = option
    
    def display(self):
        """Displays the menu to user"""
        print(f"\n{self.title}")
        for key, option in self.options.items():
            print(f"{key}. {option.name}")
    
    def execute(self, choice):
        """Executes the chosen options"""
        ret = None
        if choice in self.options:
            print(self.options[choice])
            ret = self.options[choice].execute()
        else:
            print("Invalid Entry. Please Re-enter your choice.")

        return ret


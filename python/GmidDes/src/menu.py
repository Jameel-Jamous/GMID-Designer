from src.blocks import Menu

class MainMenu(Menu):
    """A class for creating the main menu"""
    def __init__(self, title):
        super().__init__(title)
    
    def display(self):
        super().display()
        print("Z. Close Program")
        
class SubMenu(Menu):
    """A class for creating submenus."""
    def __init__(self, title):
        super().__init__(title)
    
    def display(self):
        super().display()
        print("X. Back")
from notebook import Notebook, Note
import sys


class Menu:
    def __init__(self):
        """
        Initialize the menu with parameters
        """
        self.choices = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit}
        self.notebook = Notebook()

    def show_notes(self, notes=None):
        """
        Show notes in the notebook
        :param notes: notes, which we want to see, if it is None, show all
        :return: None
        """
        if not notes:
            notes = self.notebook.notes
        if notes:
            for note in notes:
                print('{}: memo: {}\n tags: {}\n'.format(note.last_id,
                                                         note.memo, note.tags))

    def add_note(self):
        """
        Add the note, depending on user's input
        :return: None
        """
        value = input("Enter the memo, but if u want to add tags too"
                      " (optionally),"
                      " type ';' and then type tags to note\n"
                      "(FORMAT: memo;tags) : ")
        if ';' not in value:
            memo = value
            tags = ''
        else:
            memo, tags = value.split(';')
        self.notebook.new_note(memo, tags)
        print("Added successfully!")

    def modify_note(self):
        """
        Modify the note, depending on user's input
        :return: None
        """
        note_id = input("Enter id of the note, which u want to change:")
        memo = input("Enter the memo: ")
        tags = input("Enter the tags: ")
        self.notebook.modify_note(note_id, memo, tags)

    def quit(self):
        """
        Quit from the menu
        :return: None
        """
        print("Hope u've enjoyed using this notebook")
        sys.exit(0)

    def search_notes(self):
        """
        Search for the target, which user inputs in all notes
        :return: None
        """
        target = input("Enter the value, which u want to search for: ")
        notes = self.notebook.search(target)
        print(self.show_notes(notes))

    def display_menu(self):
        """
        Display the menu
        :return: None
        """
        info = "Notebook Menu: \n1. Show all notes\n2. Search notes\n" \
               "3. Add note\n4. Modify note\n5. Quit"
        print(info)

    def run(self):
        """
        Run the menu
        :return: None
        """
        while True:
            self.display_menu()
            key = input("Enter an option: ")
            action = self.choices.get(key)
            if action:
                action()
            else:
                print("{} is not a valid option".format(key))


if __name__ == "__main__":
    Menu().run()



import datetime


last_id = 0


class Note:
    """
    Use a note, will be used in Notebook
    """
    def __init__(self, memo: str, tags=''):
        """
        Initialize the note.

        :param memo: it is a note basically
        :param tags: optional param
        """
        self.memo = memo
        self.tags = tags
        self.creation_data = datetime.date.today()
        global last_id
        last_id += 1
        self.last_id = last_id

    def find_match(self, target: str):
        """
        Determine whether there are matches in note with target.

        :param target: it is a target which one wants to check
        :return: True/False, depending on matches
        """
        return target in self.memo or target in self.tags


class Notebook:
    """
    Use as a database for all notes
    """
    def __init__(self):
        """
        Initialize the notebook with no notes inside
        """
        self.notes = []

    def new_note(self, memo: str, tags=''):
        """
        Create a new note with a memo and tags.

        :param memo: it is a note basically
        :param tags: optional param
        :return: None
        """
        self.notes.append(Note(memo, tags))

    def modify_note(self, note_id, memo='', tags=''):
        """
        Modify note with note_id and change its properties.

        :param note_id: id of the note
        :param memo: if one wants to change memo
        :param tags:if one wants to change tags
        :return: None
        """
        for note in self.notes:
            if str(note.last_id) == str(note_id):
                if memo:
                    note.memo = memo
                if tags:
                    note.tags = tags
                break

    def search(self, target: str):
        """
        Search for the concrete value in all notes
        :param target: concrete value, which one wants to find
        :return: list of notes(objects) with matches
        """
        temp = []
        for note in self.notes:
            if note.tags == target or note.memo == target:
                temp.append(note)
        return temp

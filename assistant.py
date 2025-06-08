
import json
import os

class Assistant:
    def __init__(self, file_path='notes.json'):
        self.file_path = file_path
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    self.notes = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.notes = []
                self.save_notes()
        else:
            self.save_notes()

    def save_notes(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword):
        return [n for n in self.notes if keyword.lower() in n.lower()]

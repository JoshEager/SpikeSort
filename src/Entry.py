"""
Purpose: An instance of this class represents a team's entries by event
"""
import json
import typing


class Entry:
    def __init__(self, event_name:str, athlete_name:str, athlete_pr:float):
        self.event = event_name
        self.name = athlete_name
        self.pr = athlete_pr

    @classmethod
    def from_file(cls, json_path:str) -> typing.Self:
        data = {}
        with open(json_path, 'r') as f:
            data = json.load(f)
        return cls(data["event"], data["name"], data["pr"])
    
    def print_entry(self):
        print(f"{self.name}:\t{self.pr}")
    

if __name__ == "__main__":
    print("Loading an entry from a file: ")
    test_1 = Entry.from_file("tests/EntryTest.json")
    print(f"{test_1.event}, {test_1.name}, {test_1.pr}")

    print()
    print("Creating an Entry normally:")
    test_2 = Entry("400", "Josh Eager", 54.8)
    print(f"{test_2.event}, {test_2.name}, {test_2.pr}")

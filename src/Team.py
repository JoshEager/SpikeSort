"""
Purpose: An instance of this class represents a track team. 
"""

from Athlete import Athlete
from Entry import Entry
import typing
import json

class Team:
    def __init__(self, athletes: list[Athlete], entries: list[Entry]):
        self.athletes = athletes
        self.entries = entries

    @classmethod
    def from_file(cls, json_path:str) -> typing.Self:
        data = {}
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Create a list of athletes from the JSON file
        athletes: list[Athlete] = []
        for athlete in data["athletes"]:
            athletes.append(Athlete(athlete["name"], athlete["gender"], athlete["events"]))

        # Create a list of entries from the JSON file
        entries: list[Entry] = []
        for entry in data["entries"]:
            entries.append(Entry(entry["event"], entry["name"], entry["pr"]))

        return cls(athletes, entries)
    

if __name__ == "__main__":
    print("Reading a team from a file: ")
    test_1 = Team.from_file("tests/TeamTest.json")
    print(f"{test_1.athletes}, {test_1.entries}")
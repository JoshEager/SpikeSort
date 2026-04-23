"""
Purpose: An instance of this class represents one track/field athlete

"""
import json
import typing

class Athlete:
    def __init__(self, name:str, gender:str, events:dict[str, float]):
        self.name = name
        self.gender = gender
        self.events = events

    @classmethod
    def from_file(cls, json_path:str) -> typing.Self:
        data = {}
        with open(json_path, 'r') as f:
            data = json.load(f)
        return cls(data["name"], data["gender"], data["events"])

if __name__ == "__main__":
    print("Initialize an athlete from a file: ")
    test_1: Athlete = Athlete.from_file("tests/AthleteTest.json")
    print(test_1.events)

    print()
    print("Initialize an athlete normally: ")
    test_2: Athlete = Athlete("Josh Eager", "male", {
        "100": 12.0,
        "200": 24.8,
        "400": 54.8
    })
    print(test_2.events)
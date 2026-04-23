"""
Purpose: An instance of this class represents a track and field meet.
"""

import json
import typing
from Team import Team

class Meet:
    def __init__(self, teams:list[Team]):
        self.teams = teams

    @classmethod
    def from_file(cls, json_path:str) -> typing.Self:
        data = {}
        with open(json_path, 'r') as f:
            data = json.load(f)

        teams: list[Team] = []
        for team_dict in data["teams"]:
            team = Team.from_dict(team_dict)
            teams.append(team)
        
        return cls(teams)
    

if __name__ == "__main__":
    print("Load a meet from a file: ")
    test_1 = Meet.from_file("tests/MeetTest.json")
    print(f"{test_1.teams}")
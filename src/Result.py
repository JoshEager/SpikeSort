"""
Purpose: An instance of this class represents the results of a track meet. 
"""

from Entry import Entry
from Team import Team
import Constants

class Result:
    def __init__(self, teams:list[Team]):
        self.teams:list[Team] = teams

        # Initialize the event scores to a dictionary whose keys are all the allowed events and values are a list of all the entries for that event from every team
        self.event_scores:dict[str, list[Entry]] = {}
        for event in (Constants.ALLOWED_EVENTS["running"] + Constants.ALLOWED_EVENTS["field"]):
            self.event_scores[event] = []
            for team in self.teams:
                for entry in team.entries:
                    if entry.event == event:
                        self.event_scores[event].append(entry)
        self.sort_event_scores()

        # Initialize the team scores to a dictionary whose keys are all the team names and values are 0.0
        self.team_scores:dict[str, float] = {}
        for team in self.teams:
            self.team_scores[team.team_name] = 0.0
        self.calculate_team_scores()

    def calculate_team_scores(self):
        # Iterate over the teams, then iterate over their entries and see if they scored in event_scores
        for team in self.teams:
            for team_entry in team.entries:

                # At this point, we are iterating over ALL the entries and we know who they belong to

                # Now we need to check to see if the athlete name scored.
                # To do that, we need to find the position of the entry in event_scores[team_entry.event]

                for i in range(len(Constants.POINT_VALUES)):

                    try:
                        if team_entry.name == self.event_scores[team_entry.event][i].name:
                            self.team_scores[team.team_name] += Constants.POINT_VALUES[i]
                    except IndexError:
                        # This would indicate that there were not enough entries in an event to claim all available points
                        pass



        

    def sort_event_scores(self):
        for event in self.event_scores:
            if (event not in Constants.ALLOWED_EVENTS["running"]) and (event not in Constants.ALLOWED_EVENTS["field"]):
                raise ValueError("Tried to sort an unallowed event!")
            
            # If it is a running event, we need to sort by the entry's pr ascending
            if (event in Constants.ALLOWED_EVENTS["running"]):
                self.event_scores[event].sort(key=lambda entry: entry.pr)
            else: # Field event means we need to sort descending
                self.event_scores[event].sort(key=lambda entry: entry.pr, reverse=True)

    def print_team_scores(self):
        print("---------------------------------------------")
        print("Team Results")
        print("---------------------------------------------")


        for team_name in self.team_scores:
            print(f"{team_name}: {self.team_scores[team_name]}")

    def print_event_scores(self):
        for event in self.event_scores:
            print("---------------------------------------------")
            print(f"{event}")
            print("---------------------------------------------")

            for entry in self.event_scores[event]:
                entry.print_entry()
            print()


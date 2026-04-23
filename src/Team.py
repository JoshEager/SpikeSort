"""
    Contains a class to represent any team. A team *can* contain a list of athletes, which will enable it to be optimized for. 
    Otherwise, it will contain a list of entries (Entry objects). These entries and list of athletes are used to apply the
    entry optimization. The optimization process will simply alter the team's list of entries to be the most effecient. 

"""
import json
import Athlete
import Entry

class Team: 
    name = ""
    gender = ""

    entries = []
    athletes: list[Athlete.Athlete] = []

    """
    Every team needs to contain a list of their entries and optionally a list of their athletes. 

    Athletes can either be initialized by a string that is a json dump or a path to a json object. 

    """
    def __init__(self, athletesJSONString:str="", pathToAthletesJSON:str="", entriesJSONString:str="", pathToEntriesJSON:str=""):
        # Initialize the list of athletes from either a valid JSON string or a JSON file
        if athletesJSONString:
            data = json.loads(athletesJSONString)
            for athleteDict in data:
                newAthlete = Athlete.Athlete(JSONString=json.dumps(athleteDict))
                self.athletes.append(newAthlete)
        else:
            with open(pathToAthletesJSON, 'r') as f:
                data = json.load(f)
                for athleteDict in data:
                    newAthlete = Athlete.Athlete(JSONString=json.dumps(athleteDict))
                    self.athletes.append(newAthlete)


if __name__ == "__main__":
    testTeam1 = Team(pathToAthletesJSON="tests/Athletes.json")

    print("Loading a list of athletes from a file: ")
    for athlete in testTeam1.athletes:
        print(athlete.toJSON())
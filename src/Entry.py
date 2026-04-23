"""
    Contains a data structure that holds information for any team's entries into one event.

    An entry contains an event name as well as a list of athletes that the team is putting into the event.
    When it comes to making the final simulaiton, all the teams' entries must be combined. 
"""

import json
import Athlete
import Constants

class Entry:
    event = ""
    athletes: list[Athlete.Athlete] = []

    def __init__(self, pathToJSON:str="",  JSONString:str=""):
        if pathToJSON or JSONString:
            if pathToJSON:
                self.fromJSON(pathToJSON)
            else:
                self.fromJSON(JSONString=JSONString)


    def toJSON(self)->str:
        data = {
            "event": self.event,
            "athletes": []
        }
        for athlete in self.athletes:
            data["athletes"].append({
                "name": athlete.name,
                "gender": athlete.gender,
                "events": athlete.events
            })
        return json.dumps(data, indent=4)
        
    def fromJSON(self, pathToJSON:str="", JSONString:str=""):
        if pathToJSON or JSONString:
            data = {}
            if pathToJSON:
                with open(pathToJSON, 'r') as f:
                    data = json.load(f)
            else:
                data = json.loads(JSONString)
            
            if data["event"] not in Constants.ALLOWED_EVENTS:
                raise ValueError("Tried to process an entry for an invalid event!")
            else:
                self.event = data["event"]

            for athleteDict in data["athletes"]:
                self.athletes.append(Athlete.Athlete(JSONString=json.dumps(athleteDict)))
        else:
            raise ValueError("fromJSON needs either a path or valid JSON String")
        

if __name__ == "__main__": 
    testEntry1 = Entry("test/Entry.json")
    print(testEntry1.toJSON())
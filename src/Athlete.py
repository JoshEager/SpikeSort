"""
Class that holds data (times, heights, distances) for athletes in as many events as possible


"""

import json
import Constants

class Athlete:
    name = ""
    gender = ""
    events = {}

    def __init__(self, JSONPath:str="", JSONString:str="",):
        if JSONPath or JSONString:
            if JSONString:
                self.fromJSON(JSONData=JSONString)
            else:
                self.fromJSON(JSONPath)
        else:
            raise Exception("An athlete must be constructed from a json string or a json file! Please give it at least either")


    def toJSON(self) ->str: 
        data = {
            "name": self.name,
            "gender": self.gender,
            "events": self.events
        }

        return json.dumps(data, indent=4)
    
    def fromJSON(self, JSONPath:str="", JSONData:str=""):
        # Load the data from either the json string or the file into their appropriate variables
        loadedData = ""
        if JSONData:
            loadedData = json.loads(JSONData)
        else:
            with open(JSONPath, 'r') as f:
                loadedData = json.load(f)
        
        self.name = loadedData["name"]
        self.gender = loadedData["gender"]
        self.events = loadedData["events"]

        # Check that all the events read from the json are valid
        for key in self.events:
            if key not in Constants.ALLOWED_EVENTS:
                raise ValueError("Tried to initialize an athlete who had invalid events!")

    


# Class Tests
if __name__ == "__main__":
    # Demonstrate that athletes can be loaded from either a file or from a valid json string
    print("Initialize an athlete from a file:")
    testAthlete1 = Athlete("tests/Athlete.json")
    print(testAthlete1.toJSON())
    print(testAthlete1.events["100"])
    print()

    print("Initialize an athlete from a valid JSON string:")
    testAthlete2 = Athlete(JSONString=testAthlete1.toJSON())
    print(testAthlete2.toJSON())

    # Demonstrate that error handling finds if an athlete had an invalid event
    print()
    print("Catch invalid event entries: ")
    testAthlete3 = Athlete("tests/InvalidAthlete.json")
    


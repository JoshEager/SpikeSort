"""
Purpose: This file contains a function that returns the results of a meet (a Result object) given a list of teams
"""

from Team import Team
from Result import Result

def simulate(teams: list[Team]) -> Result:
    return Result(teams)
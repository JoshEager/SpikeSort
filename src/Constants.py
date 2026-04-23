"""
Purpose: Contains track and field constants for any given set of rules
"""

ALLOWED_EVENTS = {
    "running": ["100m", "200m", "400m", "800m", "1600m", "3200m", "110h", "300h", "4x100m", "4x200m", "4x400m", "4x800m"],
    "field": [ "Shotput", "Discus", "High Jump", "Long Jump", "Pole Vault"]
    }

MAX_EVENTS_PER_ATHLETE = 4
POINT_VALUES = [10, 8, 6, 5, 4, 3, 2, 1] # First place gets 10 points, second 8, etc
"""
Connor Mentel
CS 5002 - Foundations
Programming #2
mbta.py
"""


RED_LINE = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass", "Andrew", "Broadway", "South Station",
            "Downtown Crossing", "Park St", "Charles/MGH", "Kendall", "Central", "Harvard", "Porter", "Davis", "Alewife"]


# Function to validate if input station exists.
def is_valid_station (station):
    if station in RED_LINE:
        return True
    else:
        return False

# Function to calculate the direction in which the train is headed.
def get_direction (x,y):
    if RED_LINE.index(x) > RED_LINE.index(y):
        direction = "Ashmont"
        return direction
    elif RED_LINE.index(y) > RED_LINE.index(x):
        direction = "Alewife"
        return direction
    elif (RED_LINE.index(y)) == (RED_LINE.index(x)):
        return("no destination found.")
    elif y not in RED_LINE or x not in RED_LINE:
        return("no destination found.")

# Function to count the number of stops during the ride.
def get_num_stops (x,y):
    if RED_LINE.index(x) - RED_LINE.index(y) > 0:
        num_stops = (RED_LINE.index(x) - RED_LINE.index(y))
        return num_stops
    elif RED_LINE.index(y) - RED_LINE.index(x) > 0:
        num_stops = RED_LINE.index(y) - RED_LINE.index(x)
        return num_stops
    elif RED_LINE.index(y) - RED_LINE.index(x) == 0:
        num_stops = RED_LINE.index(y) - RED_LINE.index(x)
        return num_stops







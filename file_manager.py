# file_manager.py

import json

def save_events_to_file(events, filename):
    # Convert events to dictionaries and open the file in write mode
    with open(filename, 'w') as file:
         # Dump the dictionary representation of events to the file
        json.dump([event.to_dict() for event in events], file)

def load_events_from_file(filename):
    try:
         # Open the file in read mode and load the JSON data
        with open(filename, 'r') as file:
            data = json.load(file)
            # Convert dictionaries back to Event objects and return the list
            return [Event.from_dict(event_dict) for event_dict in data]
    except FileNotFoundError:
         # If the file doesn't exist, return an empty list
        return []

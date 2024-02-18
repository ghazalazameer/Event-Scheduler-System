# test_event_manager.py

import pytest
from event import Event
from event_manager import EventManager

@pytest.fixture
def event_manager():
    return EventManager()

# Test for adding an event
def test_add_event(event_manager):
    event = Event("Project1", "Flask Framework", "2024-02-02T09:00:00", "2024-02-02T11:30:00")
    event_manager.add_event(event)
    assert len(event_manager.events) == 1

# Test for getting sorted events
def test_get_sorted_events(event_manager):
    event1 = Event("Project1", "Flask Framework", "2024-02-02T09:00:00", "2024-02-02T11:30:00")
    event2 = Event("Presentation", "Project presentation", "2024-02-18T13:00:00", "2024-02-02T09:00:00")
    event_manager.add_event(event1)
    event_manager.add_event(event2)
    sorted_events = event_manager.get_sorted_events()
    assert sorted_events[0].title == "Presentation"
    assert sorted_events[1].title == "Project1"

# Test for updating an event
def test_update_event(event_manager):
    event = Event("Project1", "Flask Framework", "2024-02-02T09:00:00", "2024-02-02T11:30:00")
    event_manager.add_event(event)
    updated_event = Event("Updated Project1", "Flask Framework updates", "2024-02-02T11:30:00", "2024-02-18T16:00:00")
    event_manager.update_event(0, updated_event)
    assert event_manager.events[0].title == "Updated Project1"

# Test for deleting an event
def test_delete_event(event_manager):
    event = Event("Project1", "Flask Framework", "2024-02-02T09:00:00", "2024-02-02T11:30:00")
    event_manager.add_event(event)
    event_manager.delete_event(0)
    assert len(event_manager.events) == 0

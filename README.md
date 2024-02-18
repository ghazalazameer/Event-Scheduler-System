# Event Management API

A simple Flask API for creating, viewing, updating, and deleting events.

## Features

* Event Creation: Add new events via a POST request.
* Event Listing: Retrieve all events or search by title/description using GET.
* Event Modification: Update existing events using PUT requests.
* Event Deletion: Remove events via DELETE requests.

## Endpoints:

- POST /events : Add a new event
- GET /events : Get all events or search for events 
- PUT /events/<int:index> : Update an event by index
- DELETE /events/<int:index> : Delete an event by index

## Data Structure:

Events are expected in JSON format with the following structure:

```json
{
    "title": "Event Title",
    "description": "Event description",
    "start_time": "YYYY-MM-DDTHH:MM:SS",
    "end_time": "YYYY-MM-DDTHH:MM:SS"
}
```

## Getting Started:

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the API using a tool like Postman or curl.

## Additional Notes:

- The API uses a JSON file (`events.json`) to store events.
- Error handling is in place for potential exceptions.
- Debugging is enabled for development purposes.

## Contributing:

- Fork this repository.
- Create a branch for your changes.
- Make your changes and commit them.
- Open a pull request.




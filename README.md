# Event Scheduler System 🗓

This project is a simple Flask-based RESTful API for managing events. It allows users to perform CRUD (Create, Read, Update, Delete) operations on events stored in a JSON file. The API supports endpoints for adding, retrieving, updating, and deleting events. Additionally, it includes a search functionality to find events based on specific criteria.

## Technologies Used:

- Python: Backend logic is written in Python programming language.
- Flask: The web framework used for building the RESTful API.
- Postman: Utilized for testing CRUD operations and interacting with the API endpoints.
- JSON: Events are stored in a JSON file for persistence.
- Git: Version control system used for managing the project.

## Features:

- Event Creation: Add new events via a POST request.
- Event Listing: Retrieve all events or search by title/description using GET.
- Event Modification: Update existing events using PUT requests.
- Event Deletion: Remove events via DELETE requests.

## Endpoints:

- POST /events : Add a new event
- GET /events : Get all events or search for events
- PUT /events/<int:index> : Update an event by index
- DELETE /events/<int:index> : Delete an event by index

## Data Structure:

Events are expected in JSON format with the following structure:

```json
{
  "description": "Event description",
  "end_time": "YYYY-MM-DDTHH:MM:SS",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "title": "Event Title"
}
```

## Getting Started:

1. Clone this repository.
2. Install dependencies: `pip freeze > requirements.txt`
3. Run the application: `python app.py` or `flask run` (This will start the flask development server)
4. Access the API using a tool like Postman.

## Additional Notes:

- The API uses a JSON file (`events.json`) to store events.
- Error handling is in place for potential exceptions.
- Debugging is enabled for development purposes.

## Contributing:

- Fork this repository.
- Create a branch for your changes.
- Make your changes and commit them.
- Open a pull request.

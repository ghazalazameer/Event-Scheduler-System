<p align="center" style="color: #6f55f2; font-family: Rockwell, serif; font-size: 24px; font-weight: bold;">
  🏋🏽Fitness Flix🏋🏽
</p>


## Event Management API

A simple Flask API for creating, viewing, updating, and deleting events.

## Features

* Event Creation: Add new events via a POST request.
* Event Listing: Retrieve all events or search by title/description using GET.
* Event Modification: Update existing events using PUT requests.
* Event Deletion: Remove events via DELETE requests.

## Endpoints

* *POST /events* 
    * Adds a new event.
* *GET /events*
    * Retrieves all events.
    * Supports optional search by query (?query=search_term).
* *PUT /events/<int:index>*
    * Modifies an existing event based on its index.
* *DELETE /events/<int:index>*
    * Deletes an event specified by its index.

## Data Structure

Events are structured as JSON objects:

```json
{
  "title": "Event Title",
  "description": "Event description",
  "start_time": "YYYY-MM-DDTHH:MM:SS", // ISO 8601 format recommended
  "end_time": "YYYY-MM-DDTHH:MM:SS" 
}

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



# Event Management API

This Flask API provides endpoints for managing events.

## Features:

- Add events
- Get all events or search for events by query
- Update events<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Event_Management_API_0"></a>Event Management API</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">This Flask API provides endpoints for managing events.</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Features_4"></a>Features:</h2>
<ul>
<li class="has-line-data" data-line-start="6" data-line-end="7">Add events</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">Get all events or search for events by query</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">Update events</li>
<li class="has-line-data" data-line-start="9" data-line-end="11">Delete events</li>
</ul>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="Endpoints_11"></a>Endpoints:</h2>
<ul>
<li class="has-line-data" data-line-start="13" data-line-end="14">POST /events : Add a new event</li>
<li class="has-line-data" data-line-start="14" data-line-end="15">GET /events : Get all events or search for events</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">PUT /events/&lt;int:index&gt; : Update an event by index</li>
<li class="has-line-data" data-line-start="16" data-line-end="18">DELETE /events/&lt;int:index&gt; : Delete an event by index</li>
</ul>
<h2 class="code-line" data-line-start=18 data-line-end=19 ><a id="Data_Structure_18"></a>Data Structure:</h2>
<p class="has-line-data" data-line-start="20" data-line-end="21">Events are expected in JSON format with the following structure:</p>
<pre><code class="has-line-data" data-line-start="23" data-line-end="30" class="language-json">{
    "<span class="hljs-attribute">title</span>": <span class="hljs-value"><span class="hljs-string">"Event Title"</span></span>,
    "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"Event description"</span></span>,
    "<span class="hljs-attribute">start_time</span>": <span class="hljs-value"><span class="hljs-string">"YYYY-MM-DDTHH:MM:SS"</span></span>,
    "<span class="hljs-attribute">end_time</span>": <span class="hljs-value"><span class="hljs-string">"YYYY-MM-DDTHH:MM:SS"</span>
</span>}
</code></pre>
<h2 class="code-line" data-line-start=31 data-line-end=32 ><a id="Getting_Started_31"></a>Getting Started:</h2>
<ol>
<li class="has-line-data" data-line-start="33" data-line-end="34">Clone this repository.</li>
<li class="has-line-data" data-line-start="34" data-line-end="35">Install dependencies: <code>pip install -r requirements.txt</code></li>
<li class="has-line-data" data-line-start="35" data-line-end="36">Run the application: <code>python app.py</code></li>
<li class="has-line-data" data-line-start="36" data-line-end="38">Access the API using a tool like Postman or curl.</li>
</ol>
<h2 class="code-line" data-line-start=38 data-line-end=39 ><a id="Additional_Notes_38"></a>Additional Notes:</h2>
<ul>
<li class="has-line-data" data-line-start="40" data-line-end="41">The API uses a JSON file (<code>events.json</code>) to store events.</li>
<li class="has-line-data" data-line-start="41" data-line-end="42">Error handling is in place for potential exceptions.</li>
<li class="has-line-data" data-line-start="42" data-line-end="44">Debugging is enabled for development purposes.</li>
</ul>
<h2 class="code-line" data-line-start=44 data-line-end=45 ><a id="Contributing_44"></a>Contributing:</h2>
<ul>
<li class="has-line-data" data-line-start="46" data-line-end="47">Fork this repository.</li>
<li class="has-line-data" data-line-start="47" data-line-end="48">Create a branch for your changes.</li>
<li class="has-line-data" data-line-start="48" data-line-end="49">Make your changes and commit them.</li>
<li class="has-line-data" data-line-start="49" data-line-end="51">Open a pull request.</li>
</ul>
- Delete events

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



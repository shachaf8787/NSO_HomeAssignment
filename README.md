# NSO Home Exercise - Shachaf Chen
[my email](shachaf8787@gmail.com "my email")
This project implements a simple message management system using Flask and SQLite. It provides APIs to add, retrieve, and delete messages from a SQLite database.


## Getting Started
### Prerequisites

-   Python 3.11.5 (Or any version after 3.7)
-   Virtual Environment (venv) (Optional, but recommended)
### Overview
The API provides routes to:
-   Add a new message
-   Get a message
-   Delete a message
The messages are stored in a SQLite database `messages.db`.

### Installation
1. Clone the repository:
`git clone https://github.com/shachaf8787/NSO_HomeAssignment`
`cd NSO_HomeAssignment`

2. (Optional) Create and activate a virtual environment:
`python -m venv venv`
`.\venv\Scripts\activate      # On Linux: source venv/bin/activate `

3. Install the required packages:
`pip install -r requirements.txt`

###Usage
1. Run the Flask application:
`python main.py`

2. The application will start running at http://localhost:5000.

### API Endpoints
| Endpoint  | HTTP Method  | Description  |
| ------------ | ------------ | ------------ |
|  /AddMessage | POST   |  Add a new message to the database.  |
|  /GetMessage |  GET  |  Retrieve messages based on application ID, session ID, or message ID. |
| /DeleteMessage  |  DELETE  |  Delete messages based on application ID, session ID, or message ID. |

###Running Tests
(Optional) Run the test suite using pytest:
`pytest tests/`


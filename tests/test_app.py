import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import pytest
from flask import Flask
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


#Test SQL Injection isnt required, because I am using Parametrized Queries (the ? symbol) 


def test_add_message(client):
    data = {
        "application_id": "app1",
        "session_id": "session1",
        "message_id": "msg1",
        "participants": ["user1", "user2"],
        "content": "Hello, world!"
    }
    response = client.post("/AddMessage", json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "OK"}


def test_add_message_missing_parameters(client):
    data = {
        "application_id": "app1",
        "session_id": "session1",
        "participants": ["user1", "user2"],
        "content": "Hello, world!"
    }
    response = client.post("/AddMessage", json=data)
    assert response.status_code == 400
    assert json.loads(response.data) == {"error": "Missing required parameters"}


def test_get_message(client):
    response = client.get("/GetMessage?applicationId=app1&sessionId=session1&messageId=msg1")
    assert response.status_code == 200
    # You can further validate the response data here


def test_get_message_not_found(client):
    response = client.get("/GetMessage?applicationId=app2&sessionId=session2&messageId=msg2")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Message not found"}


def test_delete_message(client):
    response = client.delete("/DeleteMessage?applicationId=app1&sessionId=session1&messageId=msg1")
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "OK"}


def test_delete_message_not_found(client):
    response = client.delete("/DeleteMessage?applicationId=app2&sessionId=session2&messageId=msg2")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Message not found"}

def test_add_message_invalid_json(client):
    response = client.post("/AddMessage", data="invalid json data")
    assert response.status_code == 415


def test_get_message_invalid_parameters(client):
    response = client.get("/GetMessage?applicationId=app1")
    assert response.status_code == 404


def test_delete_message_invalid_parameters(client):
    response = client.delete("/DeleteMessage?applicationId=app1&sessionId=session1")
    assert response.status_code == 404


def test_get_message_no_parameters(client):
    response = client.get("/GetMessage")
    assert response.status_code == 400


def test_delete_message_no_parameters(client):
    response = client.delete("/DeleteMessage")
    assert response.status_code == 400


def test_get_message_nonexistent(client):
    response = client.get("/GetMessage?applicationId=app1&sessionId=session1&messageId=nonexistent")
    assert response.status_code == 404


def test_delete_message_nonexistent(client):
    response = client.delete("/DeleteMessage?applicationId=app1&sessionId=session1&messageId=nonexistent")
    assert response.status_code == 404

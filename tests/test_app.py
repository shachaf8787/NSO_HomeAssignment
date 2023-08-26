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


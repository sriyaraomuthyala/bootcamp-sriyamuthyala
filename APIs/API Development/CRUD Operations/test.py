from fastapi.testclient import TestClient
from main import app  # Adjust the import based on your file structure

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"id": 1, "name": "Item 1", "description": "A test item"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "A test item"}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "A test item"}

def test_update_item():
    response = client.put("/items/1", json={"id": 1, "name": "Updated Item", "description": "An updated test item"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Item", "description": "An updated test item"}

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
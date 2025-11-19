# test_flask_app.py
import requests

def test_add_item():
    url = "http://flask_app:5001/add"  # זה ה-service name מ-Docker Compose
    data = {"title": "Buy groceries"}

    response = requests.post(url, data=data)
    
    # בדיקה בסיסית שהבקשה הצליחה
    assert response.status_code == 200
    # אופציונלי: בדיקה שהתגובה כוללת מילת מפתח
    assert "success" in response.text.lower()

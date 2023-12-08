### Local Setup and Run

1. **Clone the Repository**:
2. **Navigate to the Project Directory**:
3. **Create and Activate a Virtual Environment**:
- Windows: `python -m venv venv` then `venv\Scripts\activate`
- Unix/MacOS: `python3 -m venv venv` then `source venv/bin/activate`
4. **Install Dependencies**:
  pip install -r requirements.txt
5. **Initialize the Database**:
```python
from app import db
db.create_all()
```
or use the init_db.py
6. **Run the application**
```python
python run.py
```

The server will start running on http://localhost:5000
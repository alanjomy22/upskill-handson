## Framework: FastAPI (Python)

### Why FastAPI?
- Modern Python async framework
- Auto-generates API documentation at /docs
- Built-in data validation via Pydantic
- High performance with Uvicorn ASGI server


## Project setup

# 1. Create virtual environment
python -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Install FastAPI + server
pip install fastapi uvicorn python-dotenv

# 4. Save dependencies
pip freeze > requirements.txt

# 5. Run
uvicorn app.main:app --reload
# run.py
from app import create_app
from config import DEBUG

if __name__ == "__main__":
    app = create_app()

    app.run(debug=DEBUG)

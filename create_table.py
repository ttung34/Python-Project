from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:trinhthanhtung30@127.0.0.1:5432/postgres"
app.config["SQLALCGEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
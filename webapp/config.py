"""Configure application settings such as the database URI, secret key, etc."""

import socket

TEAM = "team27"

# Determine whether connecting from on/off campus
try:
    socket.gethostbyname("data.cs.jmu.edu")
    HOST = "data.cs.jmu.edu"
except socket.gaierror:
    HOST = "localhost"


# See https://flask-appbuilder.readthedocs.io/en/latest/config.html

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg://{TEAM}@{HOST}/{TEAM}"

SECRET_KEY = "c46096d07cfae2ef311332eb98bc8336acaacf162427122b285ceb388a1cade1"

AUTH_TYPE = 1  # Database style (user/password)

APP_NAME = "Virginia Flora and Fauna Database"

APP_THEME = "lumen.css"


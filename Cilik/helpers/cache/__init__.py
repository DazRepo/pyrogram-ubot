from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL0t5dXJheHAvQmFrdWdvdS1QeXJvYm90").decode("utf-8"),
)

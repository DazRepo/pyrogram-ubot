from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1Rhcm9qaW0vS2l0YXJvVWJvdA==").decode("utf-8"),
)

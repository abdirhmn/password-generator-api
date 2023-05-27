from fastapi import FastAPI
import random
import string

app = FastAPI()
def generate_password(length: int, uppercase: bool = False, lowercase: bool = False, numbers: bool = False, special: bool = False):
    letters = ''
    if not any([uppercase, lowercase, numbers, special]):
        return ("At least one of the criteria must be selected.")
    if uppercase:
        letters += string.ascii_uppercase
    if lowercase:
        letters += string.ascii_lowercase
    if numbers:
        letters += string.digits
    if special:
        letters += string.punctuation
    return "".join(random.choice(letters) for i in range(length))
@app.get('/password')
async def get_password(length: int = 12, uppercase: bool = False, lowercase: bool = False, numbers: bool = False, special: bool = False):
    password = generate_password(length, uppercase, lowercase, numbers, special)
    return {"password": password}
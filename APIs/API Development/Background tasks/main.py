from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class Notification(BaseModel):
    email: str
    message: str

def send_email_notification(email: str, message: str):
    # Simulate sending an email
    print(f"Sending email to {email}: {message}")

@app.post("/notify/")
def notify(notification: Notification, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_notification, notification.email, notification.message)
    return {"message": "Notification sent in the background"}
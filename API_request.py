import requests
import time

# Replace with chatbot's API endpoint and necessary headers
API_URL = "https://api.chatbot.com/endpoint"
HEADERS = {"Authorization": "Bearer API_TOKEN"}

def send_question(question):
    response = requests.post(API_URL, json={"question": question}, headers=HEADERS)
    return response.json()  

questions = [...]  # List of questions

start_time = time.time()

# Sequentially send requests
responses = []
for question in questions:
    response = send_question(question)
    responses.append(response)
    time.sleep(0.1)  # small delay to avoid API rate limits

end_time = time.time()

print(f"Finished sending 1000 questions in {end_time - start_time} seconds.")

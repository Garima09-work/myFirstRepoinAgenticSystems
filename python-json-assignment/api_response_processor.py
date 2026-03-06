import json

# 1. Store JSON formatted string (simulating API response)
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

# 2. Parse JSON string into Python object
data = json.loads(api_response)

# 3. Extract required values
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

# Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# 4. Check confidence score
if confidence_score < 0.89:
    print("Warning: Confidence score is low!")

# 5. Create new Python dictionary (follow-up result)
follow_up = {
    "request_id": request_id,
    "status": "processed",
    "message": "Follow-up completed"
}

# Convert dictionary to JSON
json_output = json.dumps(follow_up, indent=4)

# 6. Write JSON output to file
with open("response.json", "w") as file:
    file.write(json_output)

print("Follow-up response written to response.json")
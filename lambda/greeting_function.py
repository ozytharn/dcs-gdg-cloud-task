import json


def lambda_handler(event, context):
    payload = event if isinstance(event, dict) else json.loads(event)
    name = payload.get("name", "Guest")
    message = f"Hello {name}, welcome to Cloud Computing!"

    return {
        "statusCode": 200,
        "body": json.dumps({"message": message}),
        "headers": {
            "Content-Type": "application/json"
        }
    }

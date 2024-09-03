import requests

def create_policy(policy_data):
    url = "https://api.example.com/insurance/policies"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=policy_data, headers=headers)
    return response.json()

if __name__ == "__main__":
    policy_data = {
        "name": "Health Insurance",
        "policy_type": "health",
        "customer_id": 1,
        "start_date": "2024-01-01",
        "end_date": "2025-01-01",
        "premium_amount": 500.0
    }
    response = create_policy(policy_data)
    print(response)


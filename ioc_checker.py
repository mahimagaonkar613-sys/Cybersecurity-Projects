import requests

API_KEY = "b5d8eec0ea0bedfee8b094ee110849ea625504f3f5f9770b934775931ea6412f7a31f8d54697d847"

ip = input("Enter IP address: ")

url = "https://api.abuseipdb.com/api/v2/check"

headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

params = {
    "ipAddress": ip,
    "maxAgeInDays": 90
}

response = requests.get(url, headers=headers, params=params)

data = response.json()

# Check if response contains expected data
if "data" in data:
    print("IP Address:", data["data"]["ipAddress"])
    print("Abuse Score:", data["data"]["abuseConfidenceScore"])
    print("Country:", data["data"]["countryCode"])
else:
    print("Error from API:")
    print(data)
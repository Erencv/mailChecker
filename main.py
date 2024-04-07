import requests
import time

API_KEY = ""

def generate_email_combinations(first_name, last_name, domain):
    patterns = [
        '{first}@{domain}',
        '{first}.{last}@{domain}',
        '{first}{last}@{domain}',
        '{f}.{last}@{domain}',
        '{f}{last}@{domain}',
        '{last}.{first}@{domain}',
        '{first}_{last}@{domain}',
        '{last}@{domain}',
    ]
    first = first_name.lower()
    last = last_name.lower()
    f = first[0]
    for pattern in patterns:
        yield pattern.format(first=first, last=last, f=f, domain=domain)

valid_emails = []
for email in generate_email_combinations("eren", "cavus", "leanscale.com"):
    response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEY}&email={email}")
    time.sleep(1)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("deliverability") == "DELIVERABLE" and data.get("is_valid_format", {}).get("value"):
            print(f"Valid email found: {email}")
            valid_emails.append(email)
        else:
            print(f"Invalid email: {email}")
    else:
        print(f"Error validating email {email}: {response.status_code}")

print("\nValid emails:")
for email in valid_emails:
    print(email)

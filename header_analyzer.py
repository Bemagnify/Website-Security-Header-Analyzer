import requests

security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

url = input("Enter Website URL (with https://) : ")

try:
    response = requests.get(url)
    print("\nSecurity Headers Check:\n")

    for header in security_headers:
        if header in response.headers:
            print(f"[+] {header} : Found")
        else:
            print(f"[-] {header} : Missing")

except Exception as e:
    print(f"Error: {e}")

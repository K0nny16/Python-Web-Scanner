from bs4 import BeautifulSoup
import requests

def analyze_page(content,scan_result):
    """
    Använder BeautifulSoup för att analysera innehållet på sidan.
    """
    soup = BeautifulSoup(content,"html.parser")
    title = soup.title.string if soup.title else "No titles found!"
    print(f"Pagetitle: {title}")
    forms = soup.find_all("form")
    if forms:
        scan_result.add_warning("Form detected! - Try XSS")


def check_security_headers(response,scan_result):
    """
    Kollar ifall det sknas säkerhets data från sidhuvudet.
    """
    headers_to_check = ["Content-Security-Policy","Strict-Transport-Security","X-Content-Type-Options","X-Frame-Options","X-XSS-Protection","Permissions-Policy","Referrer-Policy"]
    for header in headers_to_check:
        if header not in response.headers:
            scan_result.add_warning(f"{header} missing!")
        if not response.url.startswith("https://"):
            scan_result.add_warning(f"Connection not safe missing HTTPS connection!")

def check_sql_injection(url, scan_result):
    """
    Försöker identifiera SQL-injektion genom att testa vanliga payloads.
    """
    test_payloads = ["' OR '1'='1", "' OR 'x'='x"]
    vulnerable = False

    for payload in test_payloads:
        if '?' not in url:
            return
        else:
            test_url = url + payload

        try:
            response = requests.get(test_url)
            if "syntax error" in response.text.lower() or "sql" in response.text.lower():
                vulnerable = True
                break
        except requests.RequestException:
            continue

    if vulnerable:
        scan_result.add_warning("Possible SQL-Injection discovered!")

def check_cookies(response, scan_result):
    if "Set-Cookie" in response.headers:
        cookies = response.headers.get("Set-Cookie")
        if "HttpOnly" not in cookies:
            scan_result.add_warning("Cookie missing HttpOnly attribut!")
        if "Secure" not in cookies:
            scan_result.add_warning("Cookie missing Secure attribut!")
        if "SameSite" not in cookies:
            scan_result.add_warning("Cookie missing SameSite attribut!")

def check_clickjacking_protection(response,scan_result):
    if "X-Frame-Options" not in response.headers and "Content-Security-Policy" not in response.headers:
        scan_result.add_warning("Missing clickjacking protection (No X-Frame-Options!)")

def check_directory_enumeration(url,enumeration_result):
    directories = ["admin","login","backup","config","test","staging"]
    for directory in directories:
        test_url = f"{url}/{directory}/"
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                enumeration_result.add_warning(f"Directory found: {test_url}")
        except requests.RequestException:
            continue

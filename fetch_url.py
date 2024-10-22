import requests
from vulnerabilities import check_security_headers, check_sql_injection, check_cookies, check_clickjacking_protection, check_directory_enumeration

def fetch_page(url, scan_result,enumeration_result):
    """
    Hämtar innehållet från URLn.
    Returnerar HTML-kod om fetchen lyckas annars None
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            check_security_headers(response,scan_result)
            check_sql_injection(url,scan_result)
            check_cookies(response,scan_result)
            check_clickjacking_protection(response,scan_result)
            check_directory_enumeration(url,enumeration_result)
            return response.text
        else:
            print(f"Failed to get url:{url}")
            print(f"Statuscode: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")
    return None
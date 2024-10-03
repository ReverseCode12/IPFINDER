import requests

def get_user_input() -> str:
    """Get IP address from user input"""
    return input('Enter IPv4 address: ')

def get_ip_lookup_url(ip_address: str) -> str:
    """Construct IP lookup URL with given IP address (http://ip-api.com/json/[IP])"""
    return f'http://ip-api.com/json/{ip_address}'

def fetch_ip_info(ip_address: str, info=[]) -> dict | None:
    """Fetch IP information using requests and BeautifulSoup"""
    response = requests.get(url=get_ip_lookup_url(ip_address))
    if response.status_code == 200 and response.json()['status'] == 'success':
        print_results(response.json())
        return response.json()
    else:
        print(f"Failed to retrieve IP info. Status code: {response.status_code}. Try checking your IP address.")
        get_user_input()
        return {}
    
def print_results(json):
    """Print JSON results."""
    for i in json.items():
        print(f"{i[0]}: {i[1]}")


def main() -> None:
    ip_address = get_user_input()
    fetch_ip_info(ip_address)

if __name__ == '__main__':
    main()
    
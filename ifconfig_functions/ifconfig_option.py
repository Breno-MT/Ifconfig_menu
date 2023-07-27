import requests

url_ifconfig = "https://ifconfig.co/"
headers = {"Accept": "application/json"}

def ifconfig_ip(ip):
    url = url_ifconfig + f"?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)

def ifconfig_country(ip):
    url = url_ifconfig + f"country?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)

def ifconfig_country_iso(ip):
    url = url_ifconfig + f"country-iso?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)

def ifconfig_city(ip):
    url = url_ifconfig + f"city?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)

def ifconfig_asn(ip):
    url = url_ifconfig + f"asn?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(response_json)

def ifconfig_json(ip):
    url = url_ifconfig + f"json?ip={ip}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    print(f"""
    ---------
    IP: {response_json.get("ip", "Not Informed")}
    ---------
    Country ISO: {response_json.get("country_iso", "Not Informed")}
    ---------
    Country: {response_json.get("country", "Not Informed")}
    ---------
    City: {response_json.get("city", "Not Informed")}
    ---------
    Region Name: {response_json.get("region_name", "Not Informed")}
    ---------
    Internet Provider: {response_json.get("asn_org", "Not Informed")}
    ---------
    Time Zone: {response_json.get("time_zone", "Not Informed")}
    ---------
    """)
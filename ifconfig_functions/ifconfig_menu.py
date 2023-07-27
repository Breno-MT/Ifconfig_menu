from ifconfig_functions.ifconfig_option import ifconfig_ip, ifconfig_country
from ifconfig_functions.ifconfig_option import ifconfig_country_iso, ifconfig_city, ifconfig_asn, ifconfig_json

def main_menu():
    while True:
        option = int(input("""
            Select an option:
            1. Ifconfig IP
            2. Ifconfig Country
            3. Ifconfig Country ISO
            4. Ifconfig City
            5. Ifconfig ASN
            6. Ifconfig JSON (More complete)
            0. Exit
            Your option: """))


        match option:
            case 1:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_ip(ip)
            case 2:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_country(ip)
            case 3:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_country_iso(ip)
            case 4:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_city(ip)
            case 5:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_asn(ip)
            case 6:
                ip = str(input("Type the IP (IPV4/IPV6): "))
                ifconfig_json(ip)
            case 0:
                break
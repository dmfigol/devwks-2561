DEVICE_USERNAME = "vagrant"
DEVICE_PASSWORD = "vagrant"
NC_HOST = "127.0.0.1"
NC_PORT = "2223"

NC_SAVE_CONFIG_RPC = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'

NC_CONN_PARAMS = {
    "host": NC_HOST,
    "port": NC_PORT,
    "username": DEVICE_USERNAME,
    "password": DEVICE_PASSWORD,
    "hostkey_verify": False
}

NETMIKO_CONN_PARAMS = {
    "ip": NC_HOST,
    "username": DEVICE_USERNAME,
    "password": DEVICE_PASSWORD,
    "device_type": "cisco_ios",
    "port": 2222,
}
result = {
    "GigabitEthernet1": {
        "description": "MANAGEMENT INTERFACE - DON'T TOUCH ME",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "00:50:56:BB:E9:9C",
        "speed": 0
    },
    "GigabitEthernet2": {
        "description": "ConfiguredNetConf",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "00:50:56:BB:77:1A",
        "speed": 1000
    },
    "GigabitEthernet3": {
        "description": "Network Interface",
        "is_enabled": False,
        "is_up": False,
        "last_flapped": -1.0,
        "mac_address": "00:50:56:BB:EB:1E",
        "speed": 1000
    },
    "Loopback1001": {
        "description": "GenieLoop1001",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback101": {
        "description": "Created with Ansible",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback102": {
        "description": "Created with Ansible",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback1150": {
        "description": "Pod Number 1150",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback1184": {
        "description": "New Interface Created with Genie change",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback1250": {
        "description": "Pod Number 1250",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback1350": {
        "description": "Pod Number 1350",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback1450": {
        "description": "Pod Number 1450",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback199": {
        "description": "New Loopback by Priv15 user",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback211": {
        "description": "Developers Priv15 Interface",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback231": {
        "description": "DEVELOPER PRIV15 INTERFACE",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback5050": {
        "description": "Pod Number 5050",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback5150": {
        "description": "Pod Number 5150",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback5250": {
        "description": "Pod Number 5250",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback5350": {
        "description": "Pod Number 5350",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback555": {
        "description": "Added by xxx",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback556": {
        "description": "Added by GuGame",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Loopback99": {
        "description": "Developers interface",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 8000
    },
    "Port-channel1": {
        "description": "This is a port-channel interace",
        "is_enabled": True,
        "is_up": False,
        "last_flapped": -1.0,
        "mac_address": "00:1E:E5:65:3F:C0",
        "speed": 1000
    },
    "Tunnel0": {
        "description": "",
        "is_enabled": True,
        "is_up": False,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 0
    },
    "Tunnel1": {
        "description": "",
        "is_enabled": True,
        "is_up": False,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 0
    },
    "VirtualPortGroup0": {
        "description": "",
        "is_enabled": True,
        "is_up": True,
        "last_flapped": -1.0,
        "mac_address": "00:1E:E5:65:3F:BD",
        "speed": 750
    }
}

for key in result:
    device = result[key]
    desc = device["description"]
    ma = device["mac_address"]
    if len(ma) > 0:
        print(desc)

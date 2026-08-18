devices = {
    "Switch": {
        "layer": "Data Link Layer (Layer 2)",
        "function": "Connects devices in a LAN and forwards frames using MAC addresses",
        "media": "Ethernet cable / Fiber optic"
    },
    "Router": {
        "layer": "Network Layer (Layer 3)",
        "function": "Connects different networks and forwards packets using IP addresses",
        "media": "Ethernet / Fiber optic / Wireless"
    },
    "Bridge": {
        "layer": "Data Link Layer (Layer 2)",
        "function": "Connects two LAN segments and filters traffic using MAC addresses",
        "media": "Ethernet cable / Fiber optic"
    },
    "Access Point": {
        "layer": "Data Link Layer (Layer 2)",
        "function": "Provides wireless network access to devices",
        "media": "Wireless / Ethernet"
    }
}

print("NETWORK DEVICE CLASSIFICATION")
print("=" * 60)

for device, details in devices.items():
    print("\nDevice:", device)
    print("Layer:", details["layer"])
    print("Primary Function:", details["function"])
    print("Transmission Media:", details["media"])

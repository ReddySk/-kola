import serial.tools.list_ports

def list_usb_devices():
    ports = serial.tools.list_ports.comports()
    usb_devices = []
    for port in ports:
        # Print all ports for debugging
        print(f"Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
        # Adjust filter if needed (e.g., check HWID for "USB")
        if "USB" in port.description or "USB" in port.hwid:
            usb_devices.append(port.device)
    return usb_devices  

if __name__ == "__main__":
    usb_devices = list_usb_devices()
    if usb_devices:
        print("Connected USB devices:")
        for device in usb_devices:
            print(f"- {device}")
    else:
        print("No USB devices found.")

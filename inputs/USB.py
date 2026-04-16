import pywinusb.hid as hid

def list_all_usb_devices():
    devices = hid.find_all_hid_devices()
    if not devices:
        print("Žiadne USB HID zariadenia neboli nájdené.")
        return

    print("Všetky USB zariadenia:")
    for device in devices:
        print(f"- {device.product_name or 'Unknown'}")
        #print(f"    Vendor: {device.vendor_name or 'Unknown'} "
        #      f"({device.vendor_id:04x}:{device.product_id:04x})")
        #print(f"    Usage page: {device.usage_page:04x}  Usage: {device.usage:04x}")
        #print(f"    Path: {device.device_path}")
        print(f"    Vendor ID: {device.vendor_id:04x}")
        print(f"    Product ID: {device.product_id:04x}")
        #print(f"    Usage page: {device.usage:04x}  Usage: {device.usage:04x}")
        #print(f"    Usage: {device.usage:04x}")
        print(f"    Path: {device.device_path}")
        if device.serial_number:
            print(f"    Serial: {device.serial_number}")

if __name__ == "__main__":
    list_all_usb_devices()
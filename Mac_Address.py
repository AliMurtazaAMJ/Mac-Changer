import subprocess
import time



import os

def change_mac_windows(adapter_name, new_mac):
    # Disable the network adapter
    print(f"Disabling adapter: {adapter_name}")
    disable_result = subprocess.run(f'netsh interface set interface "{adapter_name}" admin=disable', shell=True)
    print("Disable command completed.")
    time.sleep(2)  # Wait for a moment to ensure the adapter is disabled

    # Set the new MAC address
    print(f"Setting new MAC address: {new_mac}")
    command = f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\{adapter_name}" /v "NetworkAddress" /t REG_SZ /d {new_mac} /f'
    registry_result = subprocess.run(command, shell=True)
    print("Registry command completed.")

    # Enable the network adapter
    print(f"Enabling adapter: {adapter_name}")
    enable_result = subprocess.run(f'netsh interface set interface "{adapter_name}" admin=enable', shell=True)
    print("Enable command completed.")

    # Verify the change
    print("Current MAC addresses:")
    result = subprocess.run(['getmac'], capture_output=True, text=True)
    print(result.stdout)
# Usage
adapter_name = "Wi-Fi"  # Change this to your adapter's name exactly as shown
new_mac_address = "00:01:BC:60:B7:AE"  # Desired MAC address (use dashes instead of colons)
change_mac_windows(adapter_name, new_mac_address)
# https://www.facebook.com/reel/3887459111483832

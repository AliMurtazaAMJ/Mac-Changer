import subprocess
import time
import random
import os
 
def load_ouis_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_random_mac(oui_list):
    oui = random.choice(oui_list)
    oui_formatted = f"{oui[:2]}:{oui[2:4]}:{oui[4:]}"
    return f"{oui_formatted}:{random.randint(0x00, 0xFF):02X}:{random.randint(0x00, 0xFF):02X}:{random.randint(0x00, 0xFF):02X}"

def list_adapters():
    print("\n=== Network Adapters ===")
    result = subprocess.run(['getmac'], capture_output=True, text=True)
    print(result.stdout)

def change_mac(adapter_name, new_mac):
    print(f"\nDisabling adapter: {adapter_name}")
    subprocess.run(f'netsh interface set interface "{adapter_name}" admin=disable', shell=True)
    time.sleep(2)
    
    print(f"Setting new MAC address: {new_mac}")
    mac_clean = new_mac.replace(":", "").replace("-", "")
    command = f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\{adapter_name}" /v "NetworkAddress" /t REG_SZ /d {mac_clean} /f'
    subprocess.run(command, shell=True)
    
    print(f"Enabling adapter: {adapter_name}")
    subprocess.run(f'netsh interface set interface "{adapter_name}" admin=enable', shell=True)
    print("\nMAC address changed successfully!")

def main():
    oui_list = load_ouis_from_file('mac-vendor.txt') if os.path.exists('mac-vendor.txt') else []
    
    while True:
        print("\n" + "="*40)
        print("       INFO CHANGER - MAC Manager")
        print("="*40)
        print("1. List Network Adapters")
        print("2. Generate Random MAC Address")
        print("3. Change MAC Address")
        print("4. Exit")
        print("="*40)
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            list_adapters()
        
        elif choice == '2':
            if oui_list:
                mac = generate_random_mac(oui_list)
                print(f"\nGenerated MAC Address: {mac}")
            else:
                print("\nError: mac-vendor.txt not found!")
        
        elif choice == '3':
            list_adapters()
            adapter = input("\nEnter adapter name (e.g., Wi-Fi): ").strip()
            
            use_random = input("Generate random MAC? (y/n): ").strip().lower()
            if use_random == 'y' and oui_list:
                new_mac = generate_random_mac(oui_list)
                print(f"Generated: {new_mac}")
            else:
                new_mac = input("Enter new MAC address (XX:XX:XX:XX:XX:XX): ").strip()
            
            confirm = input(f"\nChange {adapter} to {new_mac}? (y/n): ").strip().lower()
            if confirm == 'y':
                change_mac(adapter, new_mac)
        
        elif choice == '4':
            print("\nExiting...")
            break
        
        else:
            print("\nInvalid option!")

if __name__ == "__main__":
    main()

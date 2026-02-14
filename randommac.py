import random

def load_ouis_from_file(file_path):
    """Load OUIs from the specified text file."""
    with open(file_path, 'r') as file:
        # Read all lines, strip whitespace, and filter out empty lines
        oui_list = [line.strip() for line in file if line.strip()]
    return oui_list

def generate_mac_with_random_oui(oui_list):
    """Generate a MAC address using a random OUI from the provided list."""
    # Randomly select an OUI from the list
    oui = random.choice(oui_list)

    # Convert OUI to the MAC address format
    oui_formatted = f"{oui[:2]}:{oui[2:4]}:{oui[4:]}"  # Format OUI as XX:XX:XX

    # Generate the last three bytes randomly
    fourth_byte = random.randint(0x00, 0xFF)
    fifth_byte = random.randint(0x00, 0xFF)
    sixth_byte = random.randint(0x00, 0xFF)

    # Format the complete MAC address
    mac_address = f"{oui_formatted}:{fourth_byte:02X}:{fifth_byte:02X}:{sixth_byte:02X}"
    
    return mac_address

# Path to the text file containing OUIs
file_path = 'mac-vendor.txt'  # Replace with your file path

# Load OUIs from the file
oui_list = load_ouis_from_file(file_path)

# Generate and print the MAC address using a random OUI from the list
if oui_list:
    mac_address = generate_mac_with_random_oui(oui_list)
    print(f"Generated MAC Address: {mac_address}")

    # Optionally, write the generated MAC address to a file
    with open('generated_mac_addresses.txt', 'a') as output_file:
        output_file.write(mac_address + '\n')
else:
    print("No OUIs found in the file.")

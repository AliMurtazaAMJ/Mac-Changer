import subprocess

def list_all_network_adapters():
    """List all network adapters in the registry."""
    reg_key = r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}"
    command = f'reg query "HKLM\\{reg_key}" /s'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    print("Registry output for network adapters:")
    print(result.stdout)

# List all network adapters in the registry
list_all_network_adapters()

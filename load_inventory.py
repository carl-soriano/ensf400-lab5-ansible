# """
# Author: Carl Soriano
# File_version: 1
# """
# import ansible_runner
# import json


# def get_inventory(path):
#     """
#         Description:
#             Takes inventory file path to produce a dictionary of information about the file.
#         Params:
#             path <str>: Path to inventory file.
#             inventory <dict>: Runner interpretation of inventory file.
#     """
#     inventory_str , warning = ansible_runner.interface.get_inventory(action="list",inventories=[path]) 
#     inventory = json.loads(inventory_str)   # Use json.loads to convert str to dict.
#     return inventory

# def display_all_host_and_ip(inventory):
#     """
#         Description:
#             Displays all inventory hosts and their respective IPs.
#         Params:
#             inventory <dict>: Runner interpretation of inventory file.
#             hosts <dict>: Inventory hosts and their respective attributes.
#     """
#     hosts = inventory["_meta"]["hostvars"]
#     for host_name in hosts:
#         ip = hosts[host_name]["ansible_host"]
#         print(f"{host_name} has an ip of {ip}")
#     return

# def display_groups(inventory):
#     """
#         Description:
#             Displays all groups and hosts that belong to the coresponding groups.
#         Params:
#             inventory <dict>: Runner interpretation of inventory file.
#             groups <list>: All existing groups in the inventory.
#             hosts <list>: All hosts that exist under the group.
#     """
#     groups = inventory["all"]["children"]
#     for group_name in groups:
#         hosts = inventory[group_name]["hosts"]
#         print(f"Hosts that are part of {group_name}:")
#         for host_name in hosts:
#             print(f"\t{host_name}")
#     return

# def cmd_ping_all():
#     """
#         Description: 
#             Executes the ansible ping command 'ansible all:localhost -m ping', 
#             and prints the response message, returning the result of running the command.
#         Params:
#             result <tuple>: Represents 3 elements -> response, error_string, return_code.
#             response <str>: Response message of command execution.
#             error_string <str>: Error message from command execution.
#             return_code <int>: Return code for performance or state of command execution.
#     """
#     command_to_run = "ansible all:localhost -m ping"
#     result = ansible_runner.interface.run_command(executable_cmd=command_to_run)
#     response, error_string, return_code = result
#     print(f"Response: \n{response}")
#     return result

# def main():
#     inventory_path = "./hosts.yml"
#     inventory = get_inventory(inventory_path)
#     display_all_host_and_ip(inventory)
#     display_groups(inventory)
#     cmd_ping_all()

# if __name__ == "__main__":
#     main()
""""
Author: Carl Soriano
File_version: 1
"""
import ansible_runner
import json

def manage_inventory_and_ping(path):
    """
    Description:
        Retrieves inventory details and pings all hosts.
    Params:
        path <str>: Path to inventory file.
    """
    # Get inventory
    inventory_str, warning = ansible_runner.interface.get_inventory(action="list", inventories=[path]) 
    inventory = json.loads(inventory_str)   # Use json.loads to convert str to dict.
    
    # Display all host details
    print("Hosts and their details:")
    hosts = inventory["_meta"]["hostvars"]
    for host_name, details in hosts.items():
        ip = details.get("ansible_host", "N/A")
        groups = details.get("group_names", [])
        print(f"{host_name} has an IP of {ip}, Groups: {', '.join(groups)}")
    
    # Ping all hosts
    command_to_run = "ansible all:localhost -m ping"
    result = ansible_runner.interface.run_command(executable_cmd=command_to_run)
    response, error_string, return_code = result
    print(f"Response: \n{response}")

if __name__ == "__main__":
    manage_inventory_and_ping("./hosts.yml")

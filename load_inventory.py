
""""
Author: Carl Soriano
File_version: 1.1
"""
import ansible_runner
import json

def manage_inventory_and_ping(path):
   
    inventory_str, warning = ansible_runner.interface.get_inventory(action="list", inventories=[path]) 
    inventory = json.loads(inventory_str)   
    
    
    print("Hosts and their details:")
    hosts = inventory["_meta"]["hostvars"]
    for host_name, details in hosts.items():
        ip = details.get("ansible_host", "N/A")
        groups = details.get("group_names", [])
        print(f"{host_name} has an IP of {ip}, Groups: {', '.join(groups)}")
    
    
    command_to_run = "ansible all:localhost -m ping"
    result = ansible_runner.interface.run_command(executable_cmd=command_to_run)
    response, error_string, return_code = result
    print(f"Response: \n{response}")

if __name__ == "__main__":
    manage_inventory_and_ping("./hosts.yml")

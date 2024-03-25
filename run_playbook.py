"""
Author: Carl Soriano
File_version: 1.1
"""
import ansible_runner
import requests

def cmd_run_playbook(playbook_dir):
   
    command_to_execute = "ansible-playbook " + playbook_dir
    result = ansible_runner.interface.run_command(executable_cmd=command_to_execute)
    return result

def print_response(results):

    response, error_string, return_code = results
    print(f"Response: {response}")
    return

def main():
    playbook_path = "hello.yml"
    results = cmd_run_playbook(playbook_path)
    print_response(results)



    expected_string1 = "Hello World from managedhost-app-1 !"
    expected_string2 = "Hello World from managedhost-app-2 !"
    expected_string3 = "Hello World from managedhost-app-3 !"

    expected_strings = [expected_string1, expected_string2, expected_string3]

    for i in range(3):
        response = requests.get('http://0.0.0.0')
        if response.text == expected_strings[i]:
            print("Response matches the expected string:", response.text)
        else:
            print(f"Response doesn't match the expected string. Expected: {expected_strings[i]} but got: {response.text}")




if __name__ == "__main__":
    main()
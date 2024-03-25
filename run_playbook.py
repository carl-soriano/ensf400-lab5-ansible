"""
Author: Carl Soriano
File_version: 1
"""
import ansible_runner

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

if __name__ == "__main__":
    main()
# main.py
from folder_monitor import FolderMonitor

def main():
    folder_monitor = FolderMonitor()

    while True:
        command = input("Enter a command (commit/add/info/status/quit): ").strip().split(" ")

        if command[0] == "commit":
            folder_monitor.commit()
            print("Snapshot has been updated.")
        elif command[0] == "info":
            if len(command) == 2:
                folder_monitor.info(command[1])
            else:
                print("Invalid 'info' command. Usage: info <filename>")
        elif command[0] == "status":
            folder_monitor.status()
        elif command[0] == "add":
            if len(command) == 2:
                folder_monitor.add_file(command[1])
                print(f"File '{command[1]}' added to the monitored folder.")
            else:
                print("Invalid 'add' command. Usage: add <filename>")
        elif command[0] == "quit":
            break
        else:
            print("Invalid command. Available commands: commit, add, info, status, quit")

if __name__ == "__main__":
    main()

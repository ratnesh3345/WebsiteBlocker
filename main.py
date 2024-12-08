import time
import os
import sys

#path
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
REDIRECT_IP = "127.0.0.1"

def block_url(url, duration):
    """Using it to block url and for certain mins"""
    try:
        print(f"Blocking {url} for {duration} minutes..")
        with open(HOSTS_PATH, 'r') as file:
            hosts_content = file.readlines()

        with open(HOSTS_PATH, 'a') as file:
            if any(url in line for line in hosts_content):
                print(f"{url} is already blocked")
            else:
                #include all the variation you can think of to modify the host file
                file.write(f"{REDIRECT_IP} {url}\n")
                file.write(f"{REDIRECT_IP} www.{url}")

        time.sleep(duration*60)
        print(f"Unblocking {url} after {duration} minutes")
        unblock_url(url)
    except PermissionError:
        print("Permission denied. Run the program as an admin")
    except Exception as e:
        print(f"An error occured: {e}")



def unblock_url(url):
    """Using it to unblock url"""
    try:
        with open(HOSTS_PATH, 'r') as file:
            lines = file.readlines()
        with open(HOSTS_PATH, 'w') as file:
            for line in lines:
                if url not in line and f"www.{url}" not in line:
                    file.write(line)
        print(f"{url} has been unblocked.")

    except PermissionError:
        print("Permission denied. Run the program as an admin")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    print('URL Blocker Program')
    url = input("Enter the URL to block (e.g., youtube.com): ").strip()
    duration = int(input("Enter the duration to block the URL (in minutes): "))

    try:
        block_url(url, duration)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Cleaning up...")
        unblock_url(url)
        sys.exit(0)
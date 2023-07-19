import subprocess
import shutil
import os
import sys

# Text for the -h or -help switches
logo = """
    _____      ____     ________    _____  
   / ___ \    (    )   (___  ___)  / ____\ 
  / /   \_)   / /\ \       ) )    ( (___   
 ( (  ____   ( (__) )     ( (      \___ \  
 ( ( (__  )   )    (       ) )         ) ) 
  \ \__/ /   /  /\  \     ( (      ___/ /  
   \____/   /__(  )__\    /__\    /____/  

        Gimmie all Tools and Scripts
"""
help_text = """
-all     Download all Tools
-w       Download all Windows Tools
-we      Download Windows Enumeration Scripts
-wp      Download Windows PrivEsc Exploits
-l       Download all Linux Tools
-le      Download Linux Enumeration
-lp      Download Linux PrivEsc Exploits

Please only use 1 switch at a time.

Example: python3 GaTS.py -all | python3 GaTS.py -lp
"""

args = sys.argv

if len(args) < 2:
    print("Usage: python3 GaTS.py -help. Example python3 GaTS.py -w")
    sys.exit(1)


category = args[1]
specific_tool = args[2] if len(args) >= 3 else None

if category == "-h" or category =="-help":
        print(logo)
        print(help_text)
        sys.exit(1)

# GitHub URLS and associated names
WindowsEnumTools = [
    {"url": "https://github.com/411Hall/JAWS.git", "name": "JAWS"},
    {"url": "https://github.com/bitsadmin/wesng.git", "name": "Windows Exploit Suggester NG"},
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "name": "PowerSploit"},
    {"url": "https://github.com/Arvanaghi/SessionGopher.git", "name": "Session Gopher"},
]

WindowsPrivEscExploits = [
    {"url": "https://github.com/ParrotSec/mimikatz.git", "name": "mimikatz"},
    {"url": "https://github.com/CCob/SweetPotato.git", "name": "Sweet Potato"},
    {"url": "https://github.com/rasta-mouse/Watson.git", "name": "Watson"},
    {"url": "https://github.com/pentestmonkey/windows-privesc-check.git", "name": "Windows-Privesc_Check"},
]

LinuxEnumTools = [
    {"url": "https://github.com/rebootuser/LinEnum.git", "name": "LinEnum"},
]

LinuxPrivEscExploits = [
    {"url": "https://github.com/evait-security/ClickNRoot.git", "name": "Click_n_root"},
]

PEASS = [
    {"url": "https://github.com/carlospolop/PEASS-ng.git", "name": "PEASS_NG"},
]

# Function used to clone repository
def clone_repository(repo_url, destination_path):
    command = ['git', 'clone', repo_url, destination_path]
    subprocess.run(command, check=True)

def check_directory_exists(destination):
    if os.path.exists(destination):
        print(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)

def download_tools(tool_list, destination_prefix):
    for Tool in tool_list:
        destination = f"./{destination_prefix}/{Tool['name']}"
        check_directory_exists(destination)
        clone_repository(Tool['url'], destination)

# Handle the command-line arguments for specific tools
print(logo)
if specific_tool:
    if specific_tool in ["-we", "-wp", "-le", "-lp"]:
        if len(args) >= 4:
            specific_tool = specific_tool + args[3]
        else:
            print("Invalid specific tool option.")
            sys.exit(1)

        if "-we" in specific_tool:
            download_tools(WindowsEnumTools, "Windows/Enumeration")
        if "-wp" in specific_tool:
            download_tools(WindowsPrivEscExploits, "Windows/Privilege Escalation")
        if "-le" in specific_tool:
            download_tools(LinuxEnumTools, "Linux/Enumeration")
        if "-lp" in specific_tool:
            download_tools(LinuxPrivEscExploits, "Linux/Privilege Escalation")

# Handle the command-line arguments for categories
else:
    if category == "-all":
        download_tools(WindowsEnumTools, "Windows/Enumeration")
        download_tools(WindowsPrivEscExploits, "Windows/Privilege Escalation")
        download_tools(LinuxEnumTools, "Linux/Enumeration")
        download_tools(LinuxPrivEscExploits, "Linux/Privilege Escalation")
    elif category == "-w":
        download_tools(WindowsEnumTools, "Windows/Enumeration")
        download_tools(WindowsPrivEscExploits, "Windows/Privilege Escalation")
    elif category == "-l":
        download_tools(LinuxEnumTools, "Linux/Enumeration")
        download_tools(LinuxPrivEscExploits, "Linux/Privilege Escalation")

    elif category in ["-we", "-wp", "-le", "-lp"]:
        if len(args) >= 3:
            category = category + args[2]

        if "-we" in category:
            download_tools(WindowsEnumTools, "Windows/Enumeration")
        if "-wp" in category:
            download_tools(WindowsPrivEscExploits, "Windows/Privilege Escalation")
        if "-le" in category:
            download_tools(LinuxEnumTools, "Linux/Enumeration")
        if "-lp" in category:
            download_tools(LinuxPrivEscExploits, "Linux/Privilege Escalation")
    else:
        print("Input not valid, Use -h or -help")
        sys.exit(1)

download_tools("https://github.com/carlospolop/PEASS-ng.git", "./")

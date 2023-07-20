import subprocess
import shutil
import os
import sys



# Function used to clone repository
def clone_repository(repo_url, destination_path):
    command = ['git', 'clone', repo_url, destination_path]
    subprocess.run(command, check=True)


def download_tools_git(tool_list, destination_prefix):
    for Tool in tool_list:
        destination = f"./{destination_prefix}/{Tool['name']}"
        check_directory_exists(destination)
        clone_repository(Tool['url'], destination)


def check_directory_exists(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        print(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)


# Text for the -h or -help switches
logo = """
    _____      ____     ________    _____  
   / ___ \    (    )   (___  ___)  / ____\ 
  / /   \_)   / /\ \       ) )    ( (___   
 ( (  ____   ( (__) )     ( (      \___ \  
 ( ( (__  )   )    (       ) )         ) ) 
  \ \__/ /   /  /\  \     ( (      ___/ /  
   \____/   /__(  )__\    /__\    /____/  

        Gimmie all the Tools and Scripts
"""
help_text = """
-all     Download all Tools
-w       Download all Windows Tools
-we      Download Windows Enumeration Scripts
-wp      Download Windows PrivEsc Exploits
-l       Download all Linux Tools
-le      Download Linux Enumeration
-lp      Download Linux PrivEsc Exploits

Example: python3 GaTS.py -all | python3 GaTS.py -lp -w 
"""

args = sys.argv
NumberArguments = len(args)
if NumberArguments < 1:
    print("Usage: python3 GaTS.py -help. Example python3 GaTS.py -w")
    sys.exit(1)

if args[1] == "-h" or args[1] == "-help":
    print(logo)
    print(help_text)
    sys.exit(1)

# GitHub URLS and associated names
WindowsEnumToolsGit = [
    {"url": "https://github.com/411Hall/JAWS.git", "name": "JAWS"},
    {"url": "https://github.com/bitsadmin/wesng.git", "name": "Windows Exploit Suggester NG"},
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "name": "PowerSploit"},
    {"url": "https://github.com/Arvanaghi/SessionGopher.git", "name": "Session Gopher"},
]
WindowsEnumToolsCurl = [
    {"url": "https://github.com/carlospolop/PEASS-ng/releases/download/20230702-bc7ce3ac/winPEASany.exe", "name": "WIN-PEASS"}
                        ]
WindowsPrivEscExploits = [
    {"url": "https://github.com/ParrotSec/mimikatz.git", "name": "mimikatz"},
    {"url": "https://github.com/CCob/SweetPotato.git", "name": "Sweet Potato"},
    {"url": "https://github.com/rasta-mouse/Watson.git", "name": "Watson"},
    {"url": "https://github.com/pentestmonkey/windows-privesc-check.git", "name": "Windows-Privesc_Check"},
    {"url": "https://github.com/S3cur3Th1sSh1t/PowerSharpPack.git", "name": "PowerSharpPack"},
    {"url": "https://github.com/gladiatx0r/Powerless.git", "name": "Powerless"},
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

print(logo)
count = 1
# Handle the command-line arguments for specific tools
while count <= NumberArguments:
    if args[count] == "-we":
        download_tools_git(WindowsEnumToolsGit, "Windows/Enumeration")
        'download_tools_curl(WindowsEnumToolsCurl, "Windows/Enumeration")'
    elif args[count] == "-wp":
        download_tools_git(WindowsPrivEscExploits, "Windows/Privilege Escalation")
    elif args[count] == "-le":
        download_tools_git(LinuxEnumTools, "Linux/Enumeration")
    elif args[count] == "-lp":
        download_tools_git(LinuxPrivEscExploits, "Linux/Privilege Escalation")
    elif args[count] == "-all":
        download_tools_git(WindowsEnumToolsGit, "Windows/Enumeration")
        'download_tools_curl(WindowsEnumToolsCurl, "Windows/Enumeration")'
        download_tools_git(WindowsPrivEscExploits, "Windows/Privilege Escalation")
        download_tools_git(LinuxEnumTools, "Linux/Enumeration")
        download_tools_git(LinuxPrivEscExploits, "Linux/Privilege Escalation")
    elif args[count] == "-w":
        download_tools_git(WindowsEnumToolsGit, "Windows/Enumeration")
        'download_tools_curl(WindowsEnumToolsCurl, "Windows/Enumeration")'
        download_tools_git(WindowsPrivEscExploits, "Windows/Privilege Escalation")
    elif args[count] == "-l":
        download_tools_git(LinuxEnumTools, "Linux/Enumeration")
        download_tools_git(LinuxPrivEscExploits, "Linux/Privilege Escalation")
    else:
        print("Input not valid, Use -h or -help")
        sys.exit(1)
    count += 1

download_tools_git(PEASS, "PEASS")

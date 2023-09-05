import subprocess
import shutil
import os
import sys
import wget
import uploadserver


# Check if file path already exists and if it does remove it.
def check_directory_exists(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        print(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)


# Downloads URL using WGET, creates the file path for each tool in the list
def download_tools_wget(tool_list, destination_prefix):
    for Tool in tool_list:
        destination = f"./{destination_prefix}/{Tool['name']}"
        wget_download(Tool['url'], destination)


# calls to check if path exists and then downloads the file.
def wget_download(repo_url, destination):
    check_directory_exists(destination)
    wget.download(repo_url, out=destination)


# Creates destination, check directory exists and calls clone_repository function
def download_tools_git(tool_list, destination_prefix):
    for Tool in tool_list:
        destination = f"./{destination_prefix}/{Tool['name']}"
        check_directory_exists(destination)
        clone_repository(Tool['url'], destination)


# Function used to clone repository over git
def clone_repository(repo_url, destination_path):
    command = ['git', 'clone', repo_url, destination_path]
    subprocess.run(command, check=True)


def setup():
    packageinstaller = 0
    correctinput = 0
    SetUpMenu = """This is the set-up tool for GaTS"
    Would you like setup to run using 'apt' or 'dnf'
    [1] = apt
    [2] = dnf
    """
    print(logo)
    print(SetUpMenu)
    while correctinput == 0:
        packageinstaller = input("Please Enter an option:")
        try:
            packageinstaller = int(packageinstaller)  # Convert user input to an integer
            if packageinstaller == 1 or packageinstaller == 2:
                correctinput += 1
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    if packageinstaller == 1: 
        packageinstaller = "apt-get"
    elif packageinstaller == 2: 
        packageinstaller = "dnf"
    print("Installing Wget")
    os.system("pip3 install wget")
    print("Installing Uploadserver")
    os.system("pip3 install uploadserver")
    print("Installing git")
    os.system(f"sudo {packageinstaller} install git")
    print("Setup is complete. You can now run GaTS!")
    sys.exit(1)

"""
def start_https_server(portnumber):
    # Create the HTTPSKeys directory if it doesn't exist
    os.makedirs("HTTPSKeys", exist_ok=True)
    # Change the working directory to HTTPSKeys
    os.chdir("HTTPSKeys")
    # Generate the SSL certificate and private key
    os.system("openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'")
    os.chdir("..")  # Change back to the original working directory
    os.system(f"sudo python -m uploadserver {portnumber} --server-certificate /HTTPSKeys/server.pem & ")
"""

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
-s       Install required dependencies
-all     Download all Tools
-w       Download all Windows Tools
-we      Download Windows Enumeration Scripts
-wp      Download Windows PrivEsc Exploits
-l       Download all Linux Tools
-le      Download Linux Enumeration
-lp      Download Linux PrivEsc Exploits
-o       Download All other tools: Pivoting, tunneling, Webtools
-t       Download Tunneling Tools
-p       Download Pivoting Tools 
-wb      Download Web Tool
-ad      Download Active Directory tools

Example: python3 GaTS.py -all | python3 GaTS.py -lp -w -wb

In devlopment:

-server  Once selected tools have been downloaded a python HTTPS server will be run.
         This is done using a self signed certificate
         Please specify the port number you wish to use afer the command (default 8000)
         Example python3 GaTS.py -all -server 1234

Have you installed:
Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
python wget: pip install wget
"""

# GitHub URLS and associated names
WindowsEnumToolsGit = [
    {"url": "https://github.com/411Hall/JAWS.git", "name": "JAWS"},
    {"url": "https://github.com/bitsadmin/wesng.git", "name": "Windows Exploit Suggester NG"},
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "name": "PowerSploit"},
    {"url": "https://github.com/Arvanaghi/SessionGopher.git", "name": "Session Gopher"},
    ]
WindowsEnumToolsWget = [
    {"url": "https://github.com/carlospolop/PEASS-ng/releases/download/20230702-bc7ce3ac/winPEASany.exe",
     "name": "WIN-PEASS"}
                        ]
WindowsPrivEscExploits = [
    {"url": "https://github.com/ParrotSec/mimikatz.git", "name": "mimikatz"},
    {"url": "https://github.com/CCob/SweetPotato.git", "name": "Sweet Potato"},
    {"url": "https://github.com/rasta-mouse/Watson.git", "name": "Watson"},
    {"url": "https://github.com/pentestmonkey/windows-privesc-check.git", "name": "Windows-Privesc_Check"},
    {"url": "https://github.com/S3cur3Th1sSh1t/PowerSharpPack.git", "name": "PowerSharpPack"},
    {"url": "https://github.com/gladiatx0r/Powerless.git", "name": "Powerless"},
    {"url": "https://github.com/r3motecontrol/Ghostpack-CompiledBinaries.git", "name": "GhostPack_Binaries"},
]

LinuxEnumTools = [
    {"url": "https://github.com/rebootuser/LinEnum.git", "name": "LinEnum"},
]

LinuxPrivEscExploits = [
    {"url": "https://github.com/evait-security/ClickNRoot.git", "name": "Click_n_root"},
]

Tunneling = [
    {"url": "https://github.com/iagox86/dnscat2.git", "name": "dnscat2"},
    {"url": "https://github.com/lukebaggett/dnscat2-powershell.git", "name": "dnscat2-powershell"},
]

PivotingGit = [
    
]

PivotingWget = [
    {"url": "https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_windows_amd64.gz", "name": "Chisel Windows 64"},
    {"url": "https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_windows_arm64.gz", "name": "Chisel Windows Arm"},
    {"url": "https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_linux_amd64.gz", "name": "Chisel Linux"},
]

WebTools = [
    {"url": "https://github.com/TheRook/subbrute.git", "name": "SubBrute"},
   ]

ActiveDirectoryGit = [
    {"url": "https://github.com/PowerShellMafia/PowerSploit.git", "name": "PowerSploit"},
   ]

ActiveDirectoryWget = [
    {"url": "https://github.com/BloodHoundAD/SharpHound/releases/download/v2.0.0/SharpHound-v2.0.0.zip", "name": "SharpHound"},
   ]

args = sys.argv
NumberArguments = len(args)
if NumberArguments < 1:
    print("Usage: python3 GaTS.py -help. Example python3 GaTS.py -w")
    sys.exit(1)

if args[1] == "-h" or args[1] == "-help":
    print(logo)
    print(help_text)
    sys.exit(1)
elif args[1] == "-setup":
    setup()

print(logo)
count = 1
# Handle the command-line arguments for specific tools
while count < NumberArguments:
    if args[count] == "-all":
        download_tools_git(WindowsEnumToolsGit, "Enumeration/Windows")
        download_tools_wget(WindowsEnumToolsWget, "Enumeration/Windows")
        download_tools_git(WindowsPrivEscExploits, "Privilege Escalation/Windows")
        download_tools_git(LinuxEnumTools, "Enumeration/Linux")
        download_tools_git(LinuxPrivEscExploits, "Privilege Escalation/Linux")
        download_tools_git(Tunneling, "Tunneling")
        download_tools_git(PivotingGit, "Pivoting")
        download_tools_git(PivotingGit, "Web Tools")
        download_tools_wget(ActiveDirectoryWget, "Active Directory")
        download_tools_git(ActiveDirectoryGit, "Active Directory")
    elif args[count] == "-w":
        download_tools_git(WindowsEnumToolsGit, "Enumeration/Windows")
        download_tools_wget(WindowsEnumToolsWget, "Enumeration/Windows")
        download_tools_git(WindowsPrivEscExploits, "Privilege Escalation/Windows")
    elif args[count] == "-we":
        download_tools_git(WindowsEnumToolsGit, "Enumeration/Windows")
        download_tools_wget(WindowsEnumToolsWget, "Enumeration/Windows")
    elif args[count] == "-wp":
        download_tools_git(WindowsPrivEscExploits, "Privilege Escalation/Windows")
    elif args[count] == "-l":
        download_tools_git(LinuxEnumTools, "Enumeration/Linux")
        download_tools_git(LinuxPrivEscExploits, "Privilege Escalation/Linux")
    elif args[count] == "-le":
        download_tools_git(LinuxEnumTools, "Enumeration/Linux")
    elif args[count] == "-lp":
        download_tools_git(LinuxPrivEscExploits, "Privilege Escalation/Linux")
    elif args[count] == "-o":
        download_tools_git(Tunneling, "Tunneling")
        download_tools_git(PivotingGit, "Pivoting")
        download_tools_git(PivotingGit, "Web Tools")
        download_tools_git(ActiveDirectoryWget, "Active Directory")
        download_tools_git(ActiveDirectoryGit, "Active Directory")
    elif args[count] == "-t":
        download_tools_git(Tunneling, "Tunneling")
    elif args[count] == "-p":
        download_tools_git(PivotingGit, "Pivoting")
        download_tools_git(PivotingWget, "Pivoting")
    elif args[count] == "-wb":
        download_tools_git(PivotingGit, "Web Tools")
    elif args[count] == "-ad":
        download_tools_git(ActiveDirectoryWget, "Active Directory")
        download_tools_git(ActiveDirectoryGit, "Active Directory")
    elif args[count] == "-server" or int: 
        print("The server will be run at the end")
    else:
        print("Input not valid, Use -h or -help")
        sys.exit(1)
    count += 1

count = 1
portnumber = 8000  # Default port number
while count < NumberArguments:
    if args[count] == "-server":
        count += 1
        if count < NumberArguments:
            try:
                # Try to convert the next argument to a float (port number)
                portnumber = float(args[count])
            except ValueError:
                print("Invalid port number provided after -server flag.")
                sys.exit(1)
    count += 1

if "-server" in args:
    print("this is a work in progress, hopefully it'll be working soon.")
    #start_https_server(portnumber)




import subprocess
import shutil
import os
import sys


'Check there are arguments on the script'
args = sys.argv
if len(args) < 2:
    print("Usage: python3 MaSD.py -help. Example python3 MaSD.py -w -le")
    sys.exit(1)
args.pop(0)

DownloadAll = "-all" in args

if "-h" or "-help" in args:
    print("GaTS - Gimmie all Tools and Scripts")
    print("-all     Download all Tools")
    print("-w       Download all Windows Tools")
    print("-we      Download Windows Enumeration Tools")
    print("-wp      Download Windows PrivEsc Tools")
    print("-l       Download al Linux Tools")


'GitHub URLS and associated names'
WindowsURL = ['https://github.com/ParrotSec/mimikatz.git', 'https://github.com/411Hall/JAWS', 'https://github.com/bitsadmin/wesng.git']
WindowsNames = ["mimkatz", "JAWS", "Windows Exploit Suggester NG"]
LinuxURL = []
LinuxNames = []


def clone_repository(repo_url, destination_path):
    command = ['git', 'clone', repo_url, destination_path]
    subprocess.run(command, check=True)

name = 0
if DownloadAll or "-w" in args:
    for url in WindowsURL:
        destination = f"./Windows/{WindowsNames[name]}"
        if os.path.exists(destination):
            print(f"Removing existing directory: {destination}")
            shutil.rmtree(destination)
        clone_repository(url, destination)
        name += 1

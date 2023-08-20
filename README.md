```
  _______      ___   .___________.    _______.
 /  _____|    /   \  |           |   /       |
|  |  __     /  ^  \ `---|  |----`  |   (----`
|  | |_ |   /  /_\  \    |  |        \   \    
|  |__| |  /  _____  \   |  |    .----)   |   
 \______| /__/     \__\  |__|    |_______/ 
```
       Gimmie All the Tools and Scripts 


# Available Commands  #
```console
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
```
## In Devlopment:
`-server`  

Once selected tools have been downloaded a python HTTPS server will be run. This is done using a self signed certificate. 

Please specify the port number you wish to use afer the command (default 8000)
         Example python3 GaTS.py -all -server 1234


## Depenedencies

Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

python wget:  `pip install wget`
```
Total download size of *all* scripts/ tools is ~500MB

Example: 
```console
python3 GaTS.py -all | python3 GaTS.py -le -w
```
Please feel free to suggest more scripts and tools to add to this.


List of Current Tools and Respective Page:
------------------------------------------
| Tool Name               | Repository Link                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
| JAWS                    | [https://github.com/411Hall/JAWS.git](https://github.com/411Hall/JAWS.git)                                               |
| WESNG                   | [https://github.com/bitsadmin/wesng.git](https://github.com/bitsadmin/wesng.git)                                         |
| PowerSploit             | [https://github.com/PowerShellMafia/PowerSploit.git](https://github.com/PowerShellMafia/PowerSploit.git)                 |
| SessionGopher           | [https://github.com/Arvanaghi/SessionGopher.git](https://github.com/Arvanaghi/SessionGopher.git)                         |
| MimiKatz                | [https://github.com/ParrotSec/mimikatz.git](https://github.com/ParrotSec/mimikatz.git)                                   |
| SweetPotato             | [https://github.com/CCob/SweetPotato.git](https://github.com/CCob/SweetPotato.git)                                       |
| Watson                  | [https://github.com/rasta-mouse/Watson.git](https://github.com/rasta-mouse/Watson.git)                                   |
| Windows-Privsec-Check   | [https://github.com/pentestmonkey/windows-privesc-check.git](https://github.com/pentestmonkey/windows-privesc-check.git) |
| LinEnum                 | [https://github.com/rebootuser/LinEnum.git](https://github.com/rebootuser/LinEnum.git)                                   |
| Click n root            | [https://github.com/evait-security/ClickNRoot.git](https://github.com/evait-security/ClickNRoot.git)                     |
| Powerless               | https://github.com/gladiatx0r/Powerless.git                                                                              |
| PowerSharpPack          | https://github.com/S3cur3Th1sSh1t/PowerSharpPack                                                                         |
| PEASS-NG                | https://github.com/carlospolop/PEASS-ng                                                                                  | 
| SeatBelt                | https://github.com/GhostPack/Seatbelt.git"                                                                               | 
| Windows Kernel Exploits | [https://github.com/S3cur3Th1sSh1t/PowerSharpPack](https://github.com/SecWiki/windows-kernel-exploits.git)               | 
| Linux Smart Enumiration | https://github.com/diego-treitos/linux-smart-enumeration.git                                                             | 
| Sudo Killer             | https://github.com/TH3xACE/SUDO_KILLER.git                                                                               |
| DNScat2                 | https://github.com/iagox86/dnscat2.git                                                                                   |
| DNScat2 Powershell      | https://github.com/lukebaggett/dnscat2-powershell.git                                                                    |
| SubBrute                | https://github.com/TheRook/subbrute.git                                                                                  |
| Chisel | 
| PowerView | 
Rubeus | 
| SharpHound


_I do not own any of these tools and all support should be directed at the respective tool_

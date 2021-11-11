#!/usr/bin/python3

print(r"""
     
 ██████╗ ███████╗████████╗██████╗ 
██╔═████╗██╔════╝╚══██╔══╝╚════██╗
██║██╔██║███████╗   ██║    █████╔╝
████╔╝██║╚════██║   ██║    ╚═══██╗
╚██████╔╝███████║   ██║   ██████╔╝
 ╚═════╝ ╚══════╝   ╚═╝   ╚═════╝ 
                                      
    """)

print("Welcome back, What scan do you want to perform?")
print("------------------------------------------------")

ip_addr = input("Please enter the IP address/Net block you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease select the type of scan you want to run \n
1)Full Port Scan
2)Simple Scan
                                \n""")
print("You have selected option: ", resp)

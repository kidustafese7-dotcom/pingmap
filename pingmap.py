import os
os.system("sudo apt install nmap ")
print("""
w             w    eeeeeee       l            l
 w    ww     w     e             l            l
  w   w w   w      eeeeeee       l            l
   w w   w w       e             l            l
    w     w        eeeeeee       lllllllll    lllllllll
""")
print("choose what you want to do ")
print("""
1,ping ip
2,map ip
""")
a = int(input("choose the number you want : "))

if a == 1:
    p = input("choose the IP you want : ")
    t = int(input("how many time to ping : "))
    os.system(f"ping -c {t} {p}")
elif a == 2:
    p = input("choose the IP you want : ")
    print(f"[+] Attackig {p}")
    os.system(f"nmap  {p}")
else:
    print("enter correct number")        
    
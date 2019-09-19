import crypt, os, sys, subprocess

# skapa linux passw med sha512 genom crypt metoden
passw = input("Skriv ditt lösen: ")
print(crypt.crypt(passw, crypt.mksalt(crypt.METHOD_SHA512)))

# metoder för att kolla os
print(os.name)
print(sys.platform)

# köra en subprocess
# https://docs.python.org/3/library/subprocess.html?highlight=subprocess#module-subprocess
subprocess.call('echo "Körs i terminalen"', shell=True)

# äldre modul, kör commando i terminalen
os.system('ls -la')
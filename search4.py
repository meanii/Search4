#!/usr/bin/env python3
import requests, json, sys, time, argparse,os
from datetime import datetime
startTime = datetime.now()
requests.packages.urllib3.disable_warnings() 

class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[0;37m'
    MAGENTA = '\033[0;35m'
    UNDER = '\033[04m'
    BOLD = '\033[1m'
    END = '\033[0m'
    

def banner():
	print(color.BOLD + color.MAGENTA + """
            

          _/_/_/                                          _/        _/  _/
       _/          _/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/    _/  _/
        _/_/    _/_/_/_/  _/    _/  _/_/      _/        _/    _/  _/_/_/_/
           _/  _/        _/    _/  _/        _/        _/    _/      _/
    _/_/_/      _/_/_/    _/_/_/  _/          _/_/_/  _/    _/      _/


        > version 1.0
        > Script to find user account on various platforms.
	
		""" + color.END)

os.system("clear")		
banner()


    
parser = argparse.ArgumentParser(description='Search user on different sites.')
parser.add_argument('-u', '--username', help='Search for the given username.')


args = parser.parse_args()


if args.username:
	username = (args.username)
	print(color.BOLD + color.BLUE + "Given username is {}\n\n".format(color.RED + color.UNDER + username + color.END) + color.END)
else:
	print(color.BLUE + "usage : search4 -u username" + color.END)
	quit()



def result(url, site, username):
	address = (url+username)
	try:
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0"}
		r = requests.get(address, headers=headers, verify=False, allow_redirects=False)
		if r.status_code == 200:
			print(color.BOLD + color.YELLOW + "> {}: Account found on {}\n" .format(site, address) + color.END)
		else: print(color.BOLD + color.GREEN + "[!] {} : Account not found on {}\n" .format(site, address) + color.END)
	except: print(color.BOLD + color.GREEN + "[!] {} : Account not found on {}\n" .format(site, address) + color.END)


print(color.BOLD + color.RED+ "___________________________________________________________________________" +color.END)

print(color.BOLD + color.WHITE+ color.UNDER + "\n\nSocial sites:\n" + color.END)
result("https://www.facebook.com/", "facebook", username)
result("https://twitter.com/", "Twitter", username)
result("https://plus.google.com/+", "Google+", username.lower())
result("https://m.vk.com/", "VK", username)
result("https://myanimelist.net/profile/","MyAnimeList",username)

print(color.BOLD + color.RED + "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n" +color.END)

print(color.BOLD +color. WHITE + color.UNDER + "Video platforms:\n" + color.END)
result("https://www.youtube.com/c/", "YouTube", username)
result("https://vimeo.com/", "Vimeo", username)
result("https://www.dailymotion.com/","Dailymotion",username)
result("https://m.twitch.tv/", "Twitch", username)
result("https://steamcommunity.com/id/","steam", username)

print(color.BOLD + color.RED + "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n" +color.END)

print(color.BOLD + color.WHITE + color.UNDER + "Photo platforms:\n" + color.END)
result("https://www.instagram.com/", "Instagram", username+"/") 
#result("https://www.pinterest.com/", "Pinterest", username) 
result("https://flickr.com/photos/", "Flickr", username.lower())
result("https://", "Tumblr", username.lower()+".tumblr.com")
result("https://imgur.com/user/","Imgur",username)
result("https://vsco.co/", "VSCO", username+'/images/1')

print(color.BOLD + color.RED + "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n" +color.END)

print(color.BOLD + color.WHITE + color.UNDER + "Blogs and forums:\n" + color.END)
result("https://","Blogger",username+".blogspot.com")
result("https://medium.com/@", "Medium", username)
result("https://myspace.com/", "Myspace", username.lower())
result("https://www.reddit.com/user/", "Reddit", username)
result("https://www.quora.com/profile/", "Quora", username)

print(color.BOLD + color.RED + "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n" +color.END)

print(color.BOLD + color.WHITE + color.UNDER + "Professional platform:\n" + color.END)
result("https://github.com/", "Github", username)
result("https://sourceforge.net/u/","Sourceforge",username)
result("https://repl.it/@","Repl.it",username)
result("https://","Slack",username+".slack.com")
result("https://codepen.io/","CodePen",username)
result("https://hackerone.com/", "Hackerone", username.lower())
result("https://BugCrowd.com/", "BugCrowd", username)
result("https://about.me/" ,"about me ", username.lower())
result("https://www.patreon.com/","Patreon",username)

print(color.BOLD + color.RED + "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n" +color.END)
print(color.BOLD + color.WHITE + color.UNDER + "Others:\n" + color.END)
result("https://www.wikipedia.org/wiki/User:","Wikipedia",username)
result("https://buzzfeed.com/","Buzzfeed",username)
result("https://open.spotify.com/user/","Spotify",username)
result("https://soundcloud.com/","SoundCloud",username)
result("https://www.crunchyroll.com/user/","Crunchyroll",username)


print(color.BOLD + color.RED + "___________________________________________________________________________" +color.END)

completetime = datetime.now() - startTime
print(color.BOLD + color.BLUE + "\n\nExecution Time : {}\n" .format(completetime) + color.END)
print(color.BOLD + color.WHITE + "DONE...! \n" + color.END)

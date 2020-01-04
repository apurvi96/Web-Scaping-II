from bs4 import BeautifulSoup
from playsound import playsound
import requests
import time
import re
import sys
from gtts import gTTS 
import os 

runs = 0
wkts= 0
oponent_needed = 1000

def findnumeric(s1):
	for x in s1:
		if('0'<=x<='9'):
			return True
		else:
			pass
	return False
first_innings=0
innings_break=0
second_innings=0
other_flag=0
flag=1
while(1):
	x = requests.get("https://www.cricbuzz.com")
	page_soup = BeautifulSoup(x.content,'html5lib')
	container1 = page_soup.findAll("div",{"class" : "cb-ovr-flo"})
	container = container1[0]
	# print(page_soup.prettify())
	if(findnumeric(container.text)):
		for txt in container1:
			ind1 = txt.find("opt to")
			ind2 = txt.find("need")
			ind3 = txt.find("Innings Break")
			ind4 = txt.find("won")
			if(ind1!=-1):
				first_innings=1
				break
			elif(ind3!=-1):
				innings_break=1
				first_innings=0
				break
			elif(ind2!=-1):
				second_innings=1
				innings_break=0
				break
			elif(ind4!=-1):
				second_innings=0
				obj = gTTS(text='Done with the match', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
				sys.exit()
	else:
		obj = gTTS(text='Match not yet started', lang='en', slow=False)
		obj.save("temp.mp3")
		playsound("temp.mp3")
		sys.exit()

	if(flag==1 and innings_break==0):	    
		process_string = container.find("div",{"style" : "display:inline-block; width:140px"}).text
		# print(process_string)
		split_of_string = process_string.split(" ");
		print(split_of_string[0])
		if(split_of_string[0].find('-all')==-1):
			score = split_of_string[0].split("/")
			# print(score)
			prev_runs = runs;
			prev_wkts = wkts;
			runs = int(score[0])
			wkts = int(score[1])
			# print("runs :"+str(runs))
			# print("wkts :"+str(wkts))
			# if(runs>oponent_needed):
			# 	obj = gTTS(text='Done with match', lang='en', slow=False)
			# 	obj.save("temp.mp3")
			# 	playsound("temp.mp3")
			# 	sys.exit()
			if(runs-prev_runs==1):
				# playsound('four.mp3')
				# print("One")
				obj = gTTS(text='One run', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
			elif(runs-prev_runs==2):
				# playsound('six.mp3')
				# print("Two")
				obj = gTTS(text='Two runs', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
			elif(runs-prev_runs==3):
				# playsound('six.mp3')
				# print("Two")
				obj = gTTS(text='Three runs', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
			elif(runs-prev_runs==4):
				playsound('four.mp3')
			elif(runs-prev_runs==5):
				# playsound('six.mp3')
				# print("Two")
				obj = gTTS(text='Miss field', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
			elif(runs-prev_runs==6):
				playsound('six.mp3')
			if(wkts-prev_wkts==1):
				playsound('out.mp3')
			time.sleep(10)
		else:
			playsound('out.mp3')
			if(second_innings==1):
				obj = gTTS(text='Done with the match', lang='en', slow=False)
				obj.save("temp.mp3")
				playsound("temp.mp3")
				sys.exit()
			elif(first_innings==1):
				flag=0

	





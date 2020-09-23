# Author :- Aslam miya
# Date :- 22 september 2020
# GitHub ID :- https://github.com/anonymous770
# Package  link :- 

from pytube import YouTube
from pytube.cli import on_progress
import os, glob
import sys
import subprocess as sub
import time

# CREATING A FOLDER
dir_name = ('/sdcard/YouTube')
if not os.path.exists(dir_name):	
		try:
			os.mkdir(dir_name)
		except FileExistsError:
			pass
in_dir = ('/sdcard/YouTube/Audios')
in2_dir = ('/sdcard/YouTube/Videos')
if not os.path.exists(in_dir):
		if not os.path.exists(in_dir):	
			try:
				os.mkdir(in_dir)
				os.mkdir(in2_dir)
			except FileExistsError:
				pass
# FOLDER CREATING FINISHED

# CREATINH INPUT LINK
sub.call('clear')
print('\n')
while True:
	try:
		link = str(input('[🔸] Enter a link :  '))
		if link=="" :
		  			print("Invalid input. Link cannot be blank.\n ")
		else:
		  			pass
		  			break
		  			if type (link)== int or float :
		  				pass
		  				break
	except KeyboardInterrupt as fk:
			print('\n')
			sys.exit()
# LINK INPUT CREATING FINISHED#

# SECOND PAGE
# RESOLUTIONS

sub.call('clear')
print('\n')
print(' 🔵 1 For Lowest video resolution\n')
print(' 🔵 2 For Higest video resolution\n')
print(' 🔵 3 For Choose video resolution\n')
print(' 🔴 4 For Audio\n')
print(' 🔴 5 For Check video details\n')
print('\n')

# TYPE INPUT
while True:
	try:
		type = int(input(' [🔸] Enter a number :  '))
		if type == int:
			pass
		else:
			break
	except ValueError:
		print(' Please enter a number.\n')
	except KeyboardInterrupt as ik:	
		print('\n')
		sys.exit()
# TYPE INPUT FINISHED

# CHOSSING CONDITIONS
# LOW RESO DOWNLODING
try:
	if type == 1:
		print('\n\tWait  .....')
		time.sleep(2)
		sub.call('clear')
		print('\n\tPlease wait  .....\n')
		YouTube(link, on_progress_callback=on_progress).streams.get_lowest_resolution().download('/sdcard/YouTube/Videos')
		time.sleep(1.5)
		print('\n')
		print('\tDownloading complete !!\n')
		time.sleep(3)
		sub.call('clear')
	else:
		pass
except EOFError as err:
				print(err)
				sys.exit()	
except KeyboardInterrupt as ik:	
		print('\n')
		sys.exit()
except KeyError as ky:
	sub.call('clear')
	print('\n\033[1;31mError: \033[0;31mThis video cannot be download because it has download only the premium members of YouTube.\033[0m\n')
	print('\033[1;32mNote: \033[0;32mWe will try to fix it soon.\033[0m\n')
	sys.exit()
except Exception:
		print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')
		sys.exit()
except AttributeError:
	print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')
	
# LOW RESO DOWNLOADING FINISHED
# HIGH RESO DOWNLOADIN 

try:
	if type == 2:
		print('\n\tWait  .....')
		time.sleep(2)
		sub.call('clear')
		print('\n')
		YouTube(link, on_progress_callback=on_progress).streams.get_highest_resolution().download('/sdcard/YouTube/Videos')
		time.sleep(1.5)
		print('\n\tPlease wait  .....\n')
		print('\tDownloading complete !!\n')
		time.sleep(3)
		sub.call('clear')
	else:
		pass
except EOFError as err1:
				print(err1)
				sys.exit()	
except KeyboardInterrupt as ik1:	
		print('\n')
		sys.exit()
except KeyError as ky:
	sub.call('clear')
	print('\n\033[1;31mError: \033[0;31mThis video cannot be download because it has download only the premium members of YouTube.\033[0m\n')
	print('\033[1;32mNote: \033[0;32mWe will try to fix it soon.\033[0m\n')
	sys.exit()
except Exception:
		print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')
		sys.exit()
except AttributeError:
	print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')

# HIGH RESO DOWNLOADING FINISHED
# CHOOSING RESO

try:
	if type == 3:
		sub.call('clear')
		print('\n • Video resolution i.e. 720p, 480p, 360p, 240p, 144p\n')
		reso = input(' [🔸] Enter resolution : ')
		print('\n\tWait  .....')
		time.sleep(2)
		sub.call('clear')
		print('\n\tPlease wait  .....\n')
		YouTube(link, on_progress_callback=on_progress).streams.get_by_resolution(reso).download('/sdcard/YouTube/Videos')
		time.sleep(1.5)
		print('\n')
		print('\tDownloading complete !!\n')
		time.sleep(3)
		sub.call('clear')
	else:
		pass
except EOFError as err3:
				print(err3)
				sys.exit()	
except KeyboardInterrupt as ik:	
		print('\n')
		sys.exit()
except KeyError as ky:
	sub.call('clear')
	print('\n\033[1;31mError: \033[0;31mThis video cannot be download because it has download only the premium members of YouTube.\033[0m\n')
	print('\033[1;32mNote: \033[0;32mWe will try to fix it soon.\033[0m\n')
	sys.exit()
except Exception:
		print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')
		sys.exit()
except AttributeError:
	print('\t\033[1;33mSorry: \033[0;33mVideo stream is not available.\033[0m\n')

# CHOSSING RESO FINISHED
# AUDIO DOWNLOADING

try:
	if type == 4:
		print('\n\tWait  .....')
		time.sleep(2)
		sub.call('clear')
		print('\n')
		print('\n\tPlease wait  .....\n')
		YouTube(link, on_progress_callback=on_progress).streams.get_audio_only().download('/sdcard/YouTube/Audios')
		time.sleep(1)
		print('\n\tDownloading complete !!\n')
		time.sleep(2)
		sub.call('clear')
		os.chdir('/sdcard/YouTube/Audios')
		for fi in glob.glob('*.mp4'):
	 		os.rename(fi, fi[:-3] + 'mp3')
	 		sys.exit()
	else:
		pass
except EOFError as err4:
				print(err4)
				sys.exit()	
except KeyboardInterrupt as ik:	
		print('\n')
		sys.exit()
except KeyError as ky:
	sub.call('clear')
	print('\n\033[1;31mError: \033[0;31mThis audio cannot be download because it has download only the premium members of YouTube.\033[0m\n')
	print('\033[1;32mNote: \033[0;32mWe will try to fix it soon.\033[0m\n')
	sys.exit()
except Exception:
		print('\t\033[1;33mSorry: \033[0;33mAudio stream is not available.\033[0m\n')
		sys.exit()
except AttributeError:
	print('\t\033[1;33mSorry: \033[0;33mAudio stream is not available.\033[0m\n')

# AUDIO DOWNLOADING FINISHED
# VIDEO DETIAL
try:
	if type == 5:
		sub.call('clear')
		print("\nTitle:- "+YouTube(link).title)
		print('\nAuthor :- '+YouTube(link).author)
		print("\nThumbnail Link :- "+YouTube(link).thumbnail_url)
		age = print("\nAge Restricted :- "+str(YouTube(link).age_restricted))
		if age == True:
			print('• Video is not for under 18 years old.')
		print('• Video does not have age restriction.')
		print('\nLength :- '+str(YouTube(link).length)+' seconds')
		print("\nViews :- "+ str(YouTube(link).views))
		print("\nRating :- "+ str(YouTube(link).rating))
		print("\nDescription :\n\n" +YouTube(link).description)
	else:
		pass
except EOFError as err5:
				print(err5)
				sys.exit()	
except KeyboardInterrupt as ik:	
		print('\n')
		sys.exit()
except KeyError as ky:
	print(ky)
	sys.exit()
except Exception as ex5:
	print(ex5)
	print('\n\033[1;33mSorry: \033[0;33mSome details  is not available.\033[0m\n')
	sys.exit()
except AttributeError:
	print('\n\033[1;33mSorry: \033[0;33mSome details  is not available.\033[0m\n')
	sys.exit()

# VIDEO DETIAL FINISHED

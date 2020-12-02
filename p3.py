import os
import sys
import shutil

def prevGame():
	path = 'gameLvl1'
	exist = os.path.exists(path)
	return exist


def game():
	lvlcnt = 1
	while lvlcnt < 6:
		if(prevGame()):
			path = 'gameLvl1'
			try:
				shutil.rmtree(path)
			except OSError as e:
				print ("Error: %s : %s" % (path, e.strerror))
		else:
				if lvlcnt == 1:
					print("Level 1")
					lvlcnt = lvlcnt + 1
					#create lvl 1 and play
				elif lvlcnt == 2:
					print("Level 2")
					lvlcnt = lvlcnt + 1
					#create lvl 2 and play
				elif lvlcnt == 3:
					print("Level 3")
					lvlcnt = lvlcnt + 1
				elif lvlcnt == 4:
					print("Level 4")
					lvlcnt = lvlcnt + 1
				elif lvlcnt == 5:
					print("Level 5")
					lvlcnt = lvlcnt + 1
	print("You Win, check your directory for your prize")



if __name__ == "__main__":
		game()

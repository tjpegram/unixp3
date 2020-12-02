import os
import sys
import shutil

def prevGame():
	path = 'gameLvl1'
	exist = os.path.exists(path)
	return exist


def game():
	if(prevGame()):
		path = 'gameLvl1'
		try:
			shutil.rmtree(path)
		except OSError as e:
			print ("Error: %s : %s" % (path, e.strerror))
		os.remove('prize.txt')
	lvlcnt = 1
	while lvlcnt <= 5:

		if lvlcnt == 1:
			print("Level 1")
			path = 'gameLvl1'
			os.mkdir(path)
			file = 'monster1.txt'
			with open(os.path.join(path, file),'w') as fp:
				fp.write("I am a scary monster you must fight")

			print("You run into a scary monster")
			command = input("Fight it by typing attack: ")

			if command == 'attack':
				if os.path.exists('gameLvl1/monster1.txt'):
					os.remove('gameLvl1/monster1.txt')
				else:
					print("Whoops we had an error, please start over")

			lvlcnt = lvlcnt + 1
			#create lvl 1 and play
		elif lvlcnt == 2:
			print("Level 2")
			path = 'gameLvl1/lvl2'
			os.mkdir(path)
			file = 'monster2.txt'
			with open(os.path.join(path, file),'w') as fp:
				fp.write("I am a scary monster you must fight")

			print("You run into a scary monster")
			command = input("Fight it by typing attack: ")

			if command == 'attack':
				if os.path.exists('gameLvl1/lvl2/monster2.txt'):
					os.remove('gameLvl1/lvl2/monster2.txt')
				else:
					print("Whoops we had an error, please start over")

			lvlcnt = lvlcnt + 1
			#create lvl 2 and play
		elif lvlcnt == 3:
			print("Level 3")
			path = 'gameLvl1/lvl2/lvl3'
			os.mkdir(path)
			file = 'monster3.txt'
			with open(os.path.join(path, file),'w') as fp:
				fp.write("I am a scary monster you must fight")

			print("You run into a scary monster")
			command = input("Fight it by typing attack: ")

			if command == 'attack':
				if os.path.exists('gameLvl1/lvl2/lvl3/monster3.txt'):
					os.remove('gameLvl1/lvl2/lvl3/monster3.txt')
				else:
					print("Whoops we had an error, please start over")

			lvlcnt = lvlcnt + 1
		elif lvlcnt == 4:
			print("Level 4")
			path = 'gameLvl1/lvl2/lvl3/lvl4'
			os.mkdir(path)
			file = 'monster4.txt'
			with open(os.path.join(path, file),'w') as fp:
				fp.write("I am a scary monster you must fight")

			print("You run into a scary monster")
			command = input("Fight it by typing attack: ")

			if command == 'attack':
				if os.path.exists('gameLvl1/lvl2/lvl3/lvl4/monster4.txt'):
					os.remove('gameLvl1/lvl2/lvl3/lvl4/monster4.txt')
				else:
					print("Whoops we had an error, please start over")

			lvlcnt = lvlcnt + 1
		elif lvlcnt == 5:
			print("Level 5")
			path = 'gameLvl1/lvl2/lvl3/lvl4/lvl5'
			os.mkdir(path)
			file = 'monster5.txt'
			with open(os.path.join(path, file),'w') as fp:
				fp.write("I am a scary monster you must fight")

			print("You run into a scary monster")
			command = input("Fight it by typing attack: ")

			if command == 'attack':
				if os.path.exists('gameLvl1/lvl2/lvl3/lvl4/lvl5/monster5.txt'):
					os.remove('gameLvl1/lvl2/lvl3/lvl4/lvl5/monster5.txt')
				else:
					print("Whoops we had an error, please start over")

			newfile = 'prize.txt'
			with open(newfile,'w') as fp:
				fp.write("Congrats, you just created and removed several files and subdirectories by means of a python script")
			lvlcnt = lvlcnt + 1
	print("You Win, check your directory for your prize")



if __name__ == "__main__":
		game()

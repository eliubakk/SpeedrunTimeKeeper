import os

class RunData:
	def __init__(self):
		self.displayName = ""
		self.splits = {}
		self.bestIndividualSplits = {}
		self.bestRunSplits = {}
		self.personalBest = "XX:XX:XX.X"
		self.current = "XX:XX:XX.X"
		self.goal = "XX:XX:XX.X"
		self.completeRunCount = 0
		self.totalRunCount = 0

	def createConfig(self, name, splitNames=None, goal=None):
		self.displayName = name.get()
		self.splits = {split.get():None for split in splitNames}
		self.bestIndividualSplits = {split.get():None for split in splitNames}
		self.bestRunSplits = {split.get():None for split in splitNames}
		self.goal = goal.get()
		self.persistConfig("test")


	def persistConfig(self, fileName):
		if not os.path.exists('configs/'):
			os.makedirs('configs/')
		with open('configs/{}.cfg'.format(fileName), "w+") as file:
			file.write("{}\n".format(self.displayName))

			#save split names and best splits
			file.write("BestIndividualSplits\n")
			for split, time in self.bestIndividualSplits.items():
				file.write("\t{}={}\n".format(split, time))
			file.write("BestRunSplits\n")
			for split, time in self.bestRunSplits.items():
				file.write("\t{}={}\n".format(split, time))

			#save run times
			file.write("Times\n")
			file.write("\t{}={}\n".format("personalBest", self.personalBest))
			file.write("\t{}={}\n".format("current", self.current))
			file.write("\t{}={}\n".format("goal", self.goal))

			#save run counts
			file.write("Counts\n")
			file.write("\t{}={}\n".format("completeRunCount", self.completeRunCount))
			file.write("\t{}={}\n".format("totalRunCount", self.totalRunCount))
			
			file.close()

	def loadConfig(self, fileName):
		with open('configs/{}.cfg'.format(fileName), "r") as file:
			if file.mode == 'r':
				lines = file.readlines()
				lineNumber = 0
				if len(lines) < 10:
					print("Invalid Config File")
					file.close()
					return False

				self.displayName = string(lines[lineNumber])
				lineNumber += 1

				#load split names and best splits
				if lines[lineNumber] != "BestIndividualSplits":
					print("Invalid Config File")
					file.close()
					return False
				lineNumber += 1
				while (lineNumber < len(lines)) and lines[lineNumber].startswith("\t"):
					split = lines[lineNumber][1:].split('=')
					self.bestIndividualSplits[split[0]] = split[1]
					lineNumber += 1

				if lines[lineNumber] != "BestRunSplits":
					print("Invalid Config File")
					file.close()
					return False
				lineNumber += 1
				while (lineNumber < len(lines)) and lines[lineNumber].startswith("\t"):
					split = lines[lineNumber][1:].split('=')
					self.bestRunSplits[split[0]] = split[1]
					lineNumber += 1

				#load run times
				if lines[lineNumber] != "Times":
					print("Invalid Config File")
					file.close()
					return False
				lineNumber += 1
				personalBest = lines[lineNumber][1:].split('=')
				if personalBest[0] != "personalBest":
					print("Invalid Config File")
					file.close()
					return False
				self.personalBest = personalBest[1]
				lineNumber += 1
				current = lines[lineNumber][1:].split('=')
				if current[0] != "current":
					print("Invalid Config File")
					file.close()
					return False
				self.current = current[1]
				lineNumber += 1
				goal = lines[lineNumber][1:].split('=')
				if goal[0] != "goal":
					print("Invalid Config File")
					file.close()
					return False
				self.goal = goal[1]
				lineNumber += 1

				#load run counts
				if lines[lineNumber] != "Counts":
					print("Invalid Config File")
					file.close()
					return False
				lineNumber += 1
				completeRunCount = lines[lineNumber][1:].split('=')
				if completeRunCount[0] != "completeRunCount":
					print("Invalid Config File")
					file.close()
					return False
				self.completeRunCount = int(completeRunCount[1])
				lineNumber += 1
				totalRunCount = lines[lineNumber][1:].split('=')
				if totalRunCount[0] != "totalRunCount":
					print("Invalid Config File")
					file.close()
					return False
				self.totalRunCount = totalRunCount[1]
				lineNumber += 1
				
				return True

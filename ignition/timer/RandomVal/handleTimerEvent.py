def handleTimerEvent():
	import random
	
	randomValue = random.randint(0, 100)
	
	tagPath = "[edge]RandomTag"
	
	system.tag.writeBlocking([tagPath], [randomValue])
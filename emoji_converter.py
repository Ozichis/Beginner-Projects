while True:
	message = input( ">")
	words = str(message + ".").split('.')
	emojis = {
 	     "Hi" : "😔",
 	     ":(" : "😁",
 	     ":/" : "🤑",
 	     ":1" : "💰"
	}
	output = ""
	for word in words:
		output += emojis.get(word, "") + ""
	print(output)
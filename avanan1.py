userinput = None
directory = []
location = None
loc1 = None
while userinput != "Quit":
	userinput = input("Execute your command here. Type (Quit) to exit. ")
	if "mkdir" in userinput:
		new_directory = userinput.replace("mkdir ","")
		if new_directory not in directory:
			directory.append(f"{new_directory}")
		print(directory)
	if "ls" in userinput:
		element = userinput.replace("ls ","")
		if element not in directory:
			print(directory)
		else:
			loc1 = directory.index(f"{element}")
			print(directory[loc1:])
	if "cd" in userinput:
		loc = userinput.replace("cd ","")
		location = loc
		print(f"in {location}")
		loc1 = directory.index(f"{location}")
	if "touch" in userinput:
		file = userinput.replace("touch ","")
		if file not in directory:
			directory.insert(loc1, file)


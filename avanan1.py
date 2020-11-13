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

# class Tree():
#     def __init__(self,root):
#         self.root = root
#         self.children = []
#         self.Nodes = []
#     def addNode(self,obj):
#         self.children.append(obj)

#     def getAllNodes(self):
#         self.Nodes.append(self.root)
#         for child in self.children:
#             self.Nodes.append(child.data)
#         for child in self.children:
#             if child.getChildNodes(self.Nodes) != None:
#                 child.getChildNodes(self.Nodes)
#         print(*self.Nodes, sep = "\n")
#         print('Tree Size:' + str(len(self.Nodes)))

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#     def addNode(self,obj):
#         self.children.append(obj)
#     def getChildNodes(self,Tree):
#         for child in self.children:
#             if child.children:
#                 child.getChildNodes(Tree)
#                 Tree.append(child.data)
#             else:
#                 Tree.append(child.data)


# filesystem = Tree("root")
# filesystem.addNode(Node("user1"))
# filesystem.addNode(Node("user2"))
# filesystem.children[0].addNode(Node("Desktop"))
# filesystem.children[0].addNode(Node("Documents"))
# filesystem.children[1].addNode(Node("Desktop"))
# filesystem.children[1].addNode(Node("Documents"))
# filesystem.children[0].children[0].addNode(Node("app1"))
# filesystem.children[0].children[0].addNode(Node("app2"))
# filesystem.children[0].children[1].addNode(Node("doc1"))
# filesystem.children[0].children[1].addNode(Node("doc2"))
# filesystem.children[1].children[0].addNode(Node("app1"))
# filesystem.children[1].children[0].addNode(Node("app2"))
# filesystem.children[1].children[1].addNode(Node("doc1"))
# filesystem.children[1].children[1].addNode(Node("doc2"))


# userinput = None
# while userinput != "Quit":
#     filesystem.getAllNodes()
#     userinput = input("Execute your command here. Type (Quit) to exit. ")

    



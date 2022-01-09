from colorama import init, Fore, Back, Style
import os, platform
from pymongo import MongoClient

init()
client = MongoClient(os.getenv("MONGOLAB_URI"))
db = client.toDoList
col = db["task"]
tasks = [x for x in col.find({}, {'_id':1, "name":1, "checked":1})]
check = " [CHECKED]"

"""Data_Struct"""

# to_do_list = {
# 	"name": "code",
# 	"checked": False
# }


class CLI_UI:
	def __init__(self):
		self.showlist()
		self.inputs()

	def task_name(self, inp):
		inp = inp.split(" ")
		inp.remove(inp[0])
		name = " ".join(inp)
		return name

	def inputs(self):
		while True:
			print(Fore.RED+"To Add a task to the list\nenter -n and the name of the task")
			inp = input(Fore.GREEN+"Do you want to check an event (y/n)? ").lower()
			if "-n" in inp:
				# to_do_list[len(to_do_list)+1] = [self.task_name(inp), False]
				indexNo = to_do_list['lno']
				newTask = {'name':self.task_name(inp), 'checked':False}
				db.task.insert_one(newTask)
				os.system("clear")
				print(" "*6+"[*] Task added successfully!")
				self.showlist()
				continue
			elif "y" in inp.lower():
				item = int(input(Fore.CYAN+"Item number what? "))
				if platform.system() == 'Linux':
					os.system("clear")
				else:
					os.system('cmd /c "cls"')
				# to_do_list[item][1]=True
				db.task.update_one({'_id': item}, {"$set": {"checked": True}})
				self.showlist()
			elif "n" in inp.lower():
				i = input("Do you want to exit? (y/n)")
				if "y" in i:
					break
			if inp == "break":
				break

	def showlist(self, checked=None):
		print(Fore.CYAN+"\n"+" "*6+"<"*25+" To-Do List "+">"*25+"\n")
		for i in tasks:
			if tasks[i]["checked"]:
				print(Fore.YELLOW+" "*6+str(tasks[i]['_id'])+": "+tasks[i]['name']+check+"\n")
				continue
			print(Fore.YELLOW+" "*6+str(tasks[i]['_id'])+": "+tasks[i]['name']+"\n")


CLI_UI()
Style.RESET_ALL
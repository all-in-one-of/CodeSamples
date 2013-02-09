import os
import re

allFiles = os.listdir("./")

for x in allFiles:
	if x == "pp3.py":
		continue
	name_parts = re.split("([0-9]+)", x)
	new_name = name_parts[0] + "." + name_parts[1] + name_parts[2]
	os.rename(x,new_name)

from sh import grep, pwd, kate
import sys

print(pwd())
found = grep("-Frne", sys.argv[-1])

files = {occurence.split(":")[0] for occurence in found}

for file in files:
	print("\t", file)

askopenall = input("Open all files ? (y/n)")
if askopenall == "y":
	for file in files:
		p = kate(file, _bg=True)
		p.wait()

for file in files:
	askopen = input("Open file %s ? (y/n)" % file) or "y"
	if askopen == "y":
		print("open")

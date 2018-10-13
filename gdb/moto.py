import gdb
import re

class MotoMatrix4x4Printer:
	def __init__(self, val):
		self.val = val

	def to_string(self):
		str = "MT_Matrix4x4: "
		el = self.val["m_el"]
		for i in range(4):
			str += el[i]["m_co"]
			str += "\n"
		return str

def lookup_type(val):
	regex = re.compile("^.*MT_Matrix4x4.*$")
	#print(str(val.type.tag))
	if regex.match(str(val.type.tag)):
		return MotoMatrix4x4Printer(val)
	return None

def register():
	gdb.pretty_printers.append(lookup_type)

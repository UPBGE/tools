import gdb

axis_name = ("x", "y", "z", "w")

class MtVectorPackedPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string(self):
        size = self.val.type.template_argument(1)
        return "VectorPacked<{}>".format(size)

    def children(self):
        size = self.val.type.template_argument(1)
        array = self.val["data"]
        return [(axis_name[i], array[i]) for i in range(size)]

class MtVectorPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string(self):
        size = self.val.type.template_argument(1)
        return "Vector<{}>".format(size)

    def children(self):
        size = self.val.type.template_argument(1)
        array = self.val["data_"]
        return [(axis_name[i], array[i]) for i in range(size)]

class MtMatrixPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string(self):
        row = self.val.type.template_argument(1)
        columns = self.val.type.template_argument(2)
        return "Matrix<{}, {}>".format(row, columns)

    def children(self):
        columns = self.val.type.template_argument(2)
        array = self.val["data_"]
        return [("[{}]".format(i), array[i]["data_"]) for i in range(columns)]

def register_upbge_pretty_prints(objfile):
	def build_pretty_printer():
		pp = gdb.printing.RegexpCollectionPrettyPrinter("upbge")
		pp.add_printer('vector', "^mathfu::Vector<.*>$", MtVectorPrinter)
		pp.add_printer('vector', "^mathfu::VectorPacked<.*>$", MtVectorPackedPrinter)
		pp.add_printer('matrix', "^mathfu::Matrix<.*>$", MtMatrixPrinter)
		return pp

	gdb.printing.register_pretty_printer(objfile, build_pretty_printer())

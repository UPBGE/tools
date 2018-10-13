import BasicMain
import bge
import sys

class TraceMain(BasicMain.BasicMain):
	def __init__(self, directory):
		BasicMain.BasicMain.__init__(self)
		self.directory = directory
		if not hasattr(bge.texture, "ImageFFmpeg"):
			print("no ffmpeg")
			raise(1)

	def endFrame(self, i):
		filename = self.directory + str(i).rjust(3, "0") + ".png"
		bge.render.makeScreenshot(filename)

if __name__ == "__main__":
	BasicMain.launch(TraceMain(sys.argv[-1]))

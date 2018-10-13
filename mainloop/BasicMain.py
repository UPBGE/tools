import bge

class BasicMain:
	def __init__(self, frame=10):
		self.frame = frame

	def init(self):
		bge.render.setWindowSize(512, 512)
		bge.logic.setUseExternalClock(True)
		return True

	def run(self):
		for i in range(self.frame):
			self.nextFrame(i)

	def nextFrame(self, i):
		self.beginFrame(i)

		bge.logic.setClockTime(i);
		bge.logic.mouse = (0.5, 0.5)

		bge.logic.NextFrame()

		self.endFrame(i)

		print("Finished frame:", i)

	def beginFrame(self, i):
		pass

	def endFrame(self, i):
		pass


def launch(main):
	if main.init():
		main.run()

if __name__ == "__main__":
	launch(BasicMain())

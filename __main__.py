# file: view/__main__.py

from command import Command
cmd = Command(description="This is my App")

class App:

	def __init__(self):
		pass

	@cmd.command(
		cmd.argument("-v", "--verbose", action="store_true", help="verbose"),
		cmd.argument("-o", "--output", help="output"),
		cmd.argument("-A", "--another", action="store_true", help="Another Option"),
	)
	def main(self, args):
		print(args)

	@cmd.subcommand()
	def nothing(self, args):
		'''This does nothing special'''
		print("Nothing special!")

	@cmd.subcommand(cmd.argument("-d", help="Debug mode"), cmd.argument("-n", help="No mode", action="store_true"))
	def debug(self, args):
		if args.d:
			print(args.d)
		elif args.n:
			print("No mode")
		else:
			print(args)

	@cmd.subcommand(cmd.argument("-f", "--filename", help="A thing with a filename"))
	def filename(self, args):
		print(args.filename)

if __name__ == '__main__':
	cmd.parse()
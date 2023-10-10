import luigi

class HelloWorld(luigi.Task):

    def output(self):
        pass

    def run(self):
        pass

class NameSubstituter(luigi.Task):
	# store the contents of luigi.Parameter() in the variable 'name'
   # name = luigi.Parameter()

    # define upstream task
    def requires(self):
        return HelloWorld()

    # define output file, whose name is constructed from the input file
    def output(self):
        pass

    # the task to execute: read input file and substitute 'World'
    def run(self):
        pass

if __name__ == '__main__':
    luigi.build([NameSubstituter()], local_scheduler=True)
# -- #
def Docs():
    """
import luigi

class HelloWorld(luigi.Task):

    def output(self):
        pass

    def run(self):
        pass

class NameSubstituter(luigi.Task):
	# store the contents of luigi.Parameter() in the variable 'name'
    name = luigi.Parameter()

    # define upstream task
    def requires(self):
        return HelloWorld()

    # define output file, whose name is constructed from the input file
    def output(self):
        pass

    # the task to execute: read input file and substitute 'World'
    def run(self):
        pass

if __name__ == '__main__':
    luigi.build([NameSubstituter(name="Docs")], local_scheduler=True)
    """

    pass

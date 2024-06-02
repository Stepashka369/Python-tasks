from subprocess import Popen, PIPE 
import my_parser 

class Executer:
    def __init__(self) -> None:
        self.command = ['df']
        self.parser = my_parser.Parser()


    def execute(self) -> None:
        process = Popen(self.command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        self.returncode = process.returncode
        self.stdout = stdout.decode()
        self.stderr = stderr.decode()


    def print_result(self) -> None:
       print(self.parser.parse(self.stdout, self.stderr, self.returncode))


class ExecuterHuman(Executer):
    def __init__(self) -> None:
        self.command = ['df', '--human']
        self.parser = my_parser.ParserHuman()


class ExecuterInode(Executer):
    def __init__(self) -> None:
        self.command = ['df', '--inode']
        self.parser = my_parser.ParserInode()
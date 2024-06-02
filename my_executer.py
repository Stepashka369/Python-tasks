from subprocess import Popen, PIPE 
import abc
import my_parser 

# абстрактный класс исполнитлея команды
class Executer(abc.ABC):
    def __init__(self) -> None:
        self.command = []
        self.parser = my_parser.ParserSimple()


    def execute(self) -> None:
        process = Popen(self.command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        self.returncode = process.returncode
        self.stdout = stdout.decode()
        self.stderr = stderr.decode()


    def print_result(self) -> None:
       print(self.parser.parse(self.stdout, self.stderr, self.returncode))


# класс исполнителя при вызове утилиты без опций
class ExecuterSimple(Executer):
    def __init__(self) -> None:
        self.command = ['df']
        self.parser = my_parser.ParserSimple()


# класс исполнителя при вызове утилиты c опций --human
class ExecuterHuman(Executer):
    def __init__(self) -> None:
        self.command = ['df', '--human']
        self.parser = my_parser.ParserHuman()


# класс исполнителя при вызове утилиты c опций --inode
class ExecuterInode(Executer):
    def __init__(self) -> None:
        self.command = ['df', '--inode']
        self.parser = my_parser.ParserInode()
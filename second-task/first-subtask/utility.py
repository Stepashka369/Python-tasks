from subprocess import Popen, PIPE 
from typing import Optional


class Utility:
    def __init__(self, subcommand: str, args: list, file_name: Optional[str]=None, password: Optional[str]=None) -> None:
        self.file_name = file_name
        self.password = password
        self.subcommand = subcommand
        self.args = args

    
    def _assemble_command(self) -> None:
        if not self.file_name and self.password:
            self.command = ['sshpass', '-p', self.password, self.subcommand] + self.args
        elif not self.password and self.file_name:
            self.command = ['sshpass', '-f', self.file_name, self.subcommand] + self.args


    def _execute_command(self) -> None:
        process = Popen(self.command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        self.returncode = process.returncode
        self.stdout = stdout.decode()
        self.stderr = stderr.decode()

    
    def print_result(self) -> None:
        print(f'STDOUT:\n{self.stdout}STDERR:\n{self.stderr}RETURNCODE:\n{self.returncode}')


    def run(self) -> None:
        self._assemble_command()
        self._execute_command()
        self.print_result()
        

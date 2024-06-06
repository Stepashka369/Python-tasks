import abc
import json

# абстрактный класс парсера
class Parser(abc.ABC): 
    def __init__(self) -> None:
        self.column_names = []


    def parse(self, information: str, error_msg: str, error_code: int) -> str:
        if error_code == 0:
            return self._success(information)
        else:
            return self._failure(error_msg)
        

    def _success(self, information: str) -> str:
        result = {'status' : 'success',
                    'error' : None,
                    'result' : self._extract_info(information)}
        return json.dumps(result)
         

    def _failure(self, error_msg: str) -> str:
        result = {'status' : 'failure',
                    'error' : error_msg,
                    'result' : None}
        return json.dumps(result)
    
    
    def _extract_info(self, information: str) -> list:
        lines = information.splitlines()[1::]
        result = []

        for line in lines:
            words = line.split()
            result.append({self.column_names[0] : words[0],
                            self.column_names[1] : words[1],
                            self.column_names[2] : words[2],
                            self.column_names[3] : words[3],
                            self.column_names[4] : words[4],
                            self.column_names[5] : words[5]})
        return result
            
       
# класс парсера при вызове утилиты без опций
class ParserSimple(Parser):
    def __init__(self) -> None:
        self.column_names = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']


# класс парсера при вызове утилиты c опций --human
class ParserHuman(Parser):
    def __init__(self) -> None:
        self.column_names = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']


# класс парсера при вызове утилиты c опций --inode
class ParserInode(Parser):
    def __init__(self) -> None:
        self.column_names = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']

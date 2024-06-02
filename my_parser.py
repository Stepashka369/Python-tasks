import json

class Parser: 
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
        # header = information.splitlines()[0]
        lines = information.splitlines()[1::]
        result = []

        for line in lines:
            # colums = header.split()
            words = line.split()
            # result.append({colums[0] : words[0],
            #                 colums[1] : words[1],
            #                 colums[2] : words[2],
            #                 colums[3] : words[3],
            #                 colums[4] : words[4],
            #                 colums[5] : words[5]})
            result.append({'Filesystem' : words[0],
                            '1K-blocks' : words[1],
                            'Used' : words[2],
                            'Available' : words[3],
                            'Use%' : words[4],
                            'Mounted on' : words[5]})
        return result


class ParserHuman(Parser):
    def _extract_info(self, information: str) -> list:
        lines = information.splitlines()[1::]
        result = []

        for line in lines:
            words = line.split()
            result.append({'Filesystem' : words[0],
                            'Size' : words[1],
                            'Used' : words[2],
                            'Avail' : words[3],
                            'Use%' : words[4],
                            'Mounted on' : words[5]})
        return result


class ParserInode(Parser):
    def _extract_info(self, information: str) -> list:
        lines = information.splitlines()[1::]
        result = []

        for line in lines:
            words = line.split()
            result.append({'Filesystem' : words[0],
                            'Inodes' : words[1],
                            'IUsed' : words[2],
                            'IFree' : words[3],
                            'IUse%' : words[4],
                            'Mounted on' : words[5]})
        return result

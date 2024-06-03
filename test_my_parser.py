import unittest
import my_parser

class TestMyParser(unittest.TestCase):

    def setUp(self):
        self.parser = my_parser.ParserSimple()


    def test__extract_info(self):
        test_str = '\ntmpfs 803788 2176 801612 1% /run'
        self.assertIsNotNone(self.parser._extract_info(''))
        self.assertEqual(len(self.parser._extract_info(test_str)), 1)
        self.assertEqual(self.parser._extract_info(test_str)[0].get('Filesystem'), 'tmpfs')
        self.assertEqual(self.parser._extract_info(test_str)[0].get('1K-blocks'), '803788')
        self.assertEqual(self.parser._extract_info(test_str)[0].get('Used'), '2176')
        self.assertEqual(self.parser._extract_info(test_str)[0].get('Available'), '801612')
        self.assertEqual(self.parser._extract_info(test_str)[0].get('Use%'), '1%')
        self.assertEqual(self.parser._extract_info(test_str)[0].get('Mounted on'), '/run')


    def test__failure(self):
        test_str = '{"status": "failure", "error": "It is ok", "result": null}'
        self.assertIsNotNone(self.parser._failure(''))
        self.assertEqual(self.parser._failure('It is ok'), test_str)


    def test__success(self):
        test_str = '{"status": "success", "error": null, "result": []}'
        self.assertIsNotNone(self.parser._success(''))
        self.assertEqual(self.parser._success(''), test_str)
    

    def test_parse(self):
        self.assertIsNotNone(self.parser.parse('', '', 0))
        self.assertIsNotNone(self.parser.parse('', '', 1))


if __name__ == '__main__':
    unittest.main()
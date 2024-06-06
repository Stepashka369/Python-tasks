import unittest
import my_executer

class TestMyExecuter(unittest.TestCase):

    def test_execute(self):
        executer = my_executer.ExecuterSimple()

        executer.execute()

        self.assertIsNotNone(executer.stdout)
        self.assertIsNotNone(executer.stderr)
        self.assertIsNotNone(executer.returncode)


if __name__ == '__main__':
    unittest.main()
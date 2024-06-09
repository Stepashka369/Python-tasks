import utility
import argparse
from subprocess import Popen, PIPE 


def parse():
    parser = argparse.ArgumentParser()

    # один из аргументов группы должен быть передан программе
    option_group = parser.add_mutually_exclusive_group(required=True)
    option_group.add_argument('-f', '--file')
    option_group.add_argument('-p', '--password')

    # обязательный аргумент(определение исполняемой подкоманды)
    parser.add_argument('subcommand', choices=['ssh', 'scp'])
    # аргументы в зависимости от подкоманды
    parser.add_argument('args', nargs=argparse.REMAINDER)

    return parser.parse_args()


def main():
    args = parse()
    util = utility.Utility(args.subcommand, args.args, args.file, args.password)
    util.run()


if __name__ == '__main__':
    main()


# process = Popen(parsed.args, stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# returncode = process.returncode
# stdout = stdout.decode()
# stderr = stderr.decode()

# print(f'\nreturncode: {returncode}\nstdout: {stdout}\nstderr: {stderr}')
# print(f'file: {args.file}, password: {args.password}, command: {args.command}, command_args: {args.args}')
        
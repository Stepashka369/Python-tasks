from argparse import ArgumentParser
import my_executer

def get_args():
    parser = ArgumentParser()
    parser.add_argument('--human', action='store_true')
    parser.add_argument('--inode', action='store_true')
    return parser.parse_args()


def main():
    args = get_args()

    if not args.human and args.inode:
        executer = my_executer.ExecuterInode()
    elif not args.inode and args.human:
        executer = my_executer.ExecuterHuman()
    else:
        executer = my_executer.ExecuterSimple()
    executer.execute()
    executer.print_result()

if __name__ == '__main__':
    main()
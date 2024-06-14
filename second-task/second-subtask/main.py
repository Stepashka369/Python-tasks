import utility_iperf
import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_server') #ip сервера
    parser.add_argument('hostname_server') #имя учетки сервера
    parser.add_argument('password_server') #пароль сервера
    parser.add_argument('ip_client') #ip клиента
    parser.add_argument('hostname_client') #имя учетки клиента
    parser.add_argument('password_client') #пароль клиента
    return parser.parse_args()


def main():
    # util = utility_iperf.Utility('10.0.2.3', 'weber', 'weber', '10.0.2.2', 'weber', 'weber')
    args = parser()
    util = utility_iperf.Utility(args.ip_server, args.hostname_server, args.password_server, 
                                 args.ip_client, args.hostname_client, args.password_client)
    util.run()
   

if __name__ == '__main__':
    main()
import utility_iperf


def main():
    util = utility_iperf.Utility('10.0.2.3', 'weber', 'weber', '10.0.2.2', 'weber', 'weber')
    util.run()
   

if __name__ == '__main__':
    main()
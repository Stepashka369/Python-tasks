import utility_ssh
import threading
import time
import json
from typing import Tuple

class Utility:
    TIMEOUT = 15

    def __init__(self, server_ip: str, server_username: str, server_password: str,
                 client_ip: str, client_username: str, client_password: str):
        self.server_ip = server_ip
        self.server_username = server_username
        self.server_password = server_password
        self.client_ip = client_ip
        self.client_username = client_username
        self.client_password = client_password


    def _run_remote_command(self, ip_remote: str, username_remote: str, password_remote: str, command: str) -> utility_ssh.Utility:
        ssh_command = [f'{username_remote}@{ip_remote}'] + command.split()
        print(command)
        util = utility_ssh.Utility('ssh', ssh_command, password=password_remote)
        util.run()
        return util


    def _run_server(self) -> None:
        command = 'iperf3 -s'
        self.server = self._run_remote_command(self.server_ip, self.server_username, self.server_password, command)

    
    def _stop_process(self, ip_remote: str, username_remote: str, password_remote: str, pid: int) -> None:
        command = f'kill {pid}'
        self._run_remote_command(ip_remote, username_remote, password_remote, command)
   

    def _run_client(self) -> None:
        command = f'iperf3 -c {self.server_ip} -J'
        self.client = self._run_remote_command(self.client_ip, self.client_username, self.client_password, command)


    def _get_pid(self, ip_remote: str, username_remote: str, password_remote: str) -> int:
        command = 'ps -C iperf3'
        util = self._run_remote_command(ip_remote, username_remote, password_remote, command)
       
        if util.returncode == 0:
            result = util.stdout.splitlines()
            if len(result) == 2:
                return result[1].split()[0]

        return -1
    

    def _is_running(self, ip_remote: str, username_remote: str, password_remote: str, timeout: int) -> Tuple[bool, int]:
        start_time = time.time()
        job_time = 0

        while job_time < timeout:
            pid = self._get_pid(ip_remote, username_remote, password_remote)
            if pid != -1:
                return True, pid
            time.sleep(0.5)
            job_time = time.time() - start_time

        return False, pid
    

    def _parse_result(self) -> None:
        result = { 'error' : self.client.stderr,
                  'result' : json.loads(self.client.stdout),
                  'status' : self.client.returncode}
        self.result = json.dumps(result, indent=2)
       

    def print_result(self) -> None:
        print(self.result)


    def run(self) -> None:
        print('Starting server.')
        server_thread = threading.Thread(target=self._run_server)
        server_thread.start()
        server_running, server_pid = self._is_running(self.server_ip, self.server_username, self.server_password, self.TIMEOUT)

        if server_running:
            print('Starting client.')
            client_thread = threading.Thread(target=self._run_client)
            client_thread.start()
            client_running, client_pid = self._is_running(self.client_ip, self.client_username, self.client_password, self.TIMEOUT)
            if client_running:
                client_thread.join(self.TIMEOUT)
                self._stop_process(self.client_ip, self.client_username, self.client_password, client_pid)
                self._stop_process(self.server_ip, self.server_username, self.server_password, server_pid)
                server_thread.join()
            else:
                self._stop_process(self.server_ip, self.server_username, self.server_password, server_pid)
                print('Client startup error.')
        else:
            print('Server startup error.')

        self._parse_result()
        self.print_result()
        # self.client.print_result()
        

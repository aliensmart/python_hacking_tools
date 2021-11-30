import paramiko

# 1
def ssh_command(ip, port, user, passwd, cmd):
    """
    makes a connection to an SSH server and runs a single command
    """
    client = paramiko.SSHClient()
    # 2 Because we’re controlling both ends of this connection, we set the
    # policy to accept the SSH key for the SSH server we’re connecting to
    # and make the connection
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    # 3 
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    # 4 You can use it to get the username from the current environment
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')

    # getpass function to request the password
    password = getpass.getpass()
    ip = input('Enter server IP: ') or '172.16.90.129'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    # 5
    ssh_command(ip, port, user, password, cmd)
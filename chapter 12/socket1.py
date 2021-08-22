try:
    import socket
    url = input('pls input a URL: ')
    host = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        rdata = data.decode()

        print(rdata, end='')

    mysock.close()
except:
    print('please enter a valid url')

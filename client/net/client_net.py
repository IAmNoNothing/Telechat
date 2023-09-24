import json
import socket as sk
import threading as th


class Net:
    def __init__(self, app):
        self.socket_udp = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        self.net_thread = th.Thread(target=self.run, daemon=True)
        self.net_thread.start()
        self.app = app
        self.cfg = self.app.get_config('net_config.json')
        self.host = self.cfg.get('host')

    def run(self):
        while self.app.running:
            data, address = self.socket_udp.recvfrom(self.cfg.get('buffer-size'))
            if address != self.host:
                print('Received package not from the server: ' + data.decode('utf-8'))
                continue
            try:
                data = json.loads(data.decode('utf-8'))
            except json.decoder.JSONDecodeError:
                print(f'Received incorrect package:{data.decode("utf-8")}. Sending `repeat` request.')
                self.send('{"action":"repeat"}'.encode('utf-8'))

            # format:
            # {"messages":[{"sender":[socket], "msg":"text", "time":"time"}]}
            # display the msgs for user

    def send(self, data: bytes):
        self.socket_udp.send(data, self.host)

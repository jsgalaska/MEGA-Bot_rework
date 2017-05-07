#------------------------------------------------▼ IRC control dictionary
import cfg, socket

class Controller:
    
    def __init__(self, HOST, PORT):
        self.HOST=HOST
        self.PORT=PORT
        self.s = socket.socket()
        self.s.connect((HOST, PORT))

    def send_pong(self, msg):
        self.s.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))
    
    def send_message(self, chan, msg):
        self.s.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'UTF-8'))
    
    def send_nick(self, nick):
        self.s.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))
    
    def send_pass(self, password):
        self.s.send(bytes('PASS %s\r\n' % password, 'UTF-8'))
    
    def join_channel(self, chan):
        self.s.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))
    
    def part_channel(self, chan):
        self.s.send(bytes('PART %s\r\n' % chan, 'UTF-8'))
            
    #------------------------------------------------▼ Cap dictionary
    
    def command_getusers(self):
        self.s.send(bytes("CLEARCHAT %s" % cfg.CHAN, 'UTF-8'))
    
    def capreq_tags(self):
        self.s.send(bytes("CAP REQ :twitch.tv/tags\r\n", 'UTF-8'))
    
    def capreq_membership(self):
        self.s.send(bytes("CAP REQ :twitch.tv/membership\r\n", 'UTF-8'))
    
    def capreq_commands(self):
        self.s.send(bytes("CAP REQ :twitch.tv/commands\r\n", 'UTF-8'))
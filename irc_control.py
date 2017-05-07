#------------------------------------------------▼ IRC control dictionary
import cfg
from bot import s

def send_pong(msg):
    s.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))

def send_message(chan, msg):
    s.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'UTF-8'))

def send_nick(nick):
    s.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))

def send_pass(password):
    s.send(bytes('PASS %s\r\n' % password, 'UTF-8'))

def join_channel(chan):
    s.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))

def part_channel(chan):
    s.send(bytes('PART %s\r\n' % chan, 'UTF-8'))
        
#------------------------------------------------▼ Cap dictionary

def command_getusers():
    s.send(bytes("CLEARCHAT %s" % cfg.CHAN, 'UTF-8'))

def capreq_tags():
    s.send(bytes("CAP REQ :twitch.tv/tags\r\n", 'UTF-8'))

def capreq_membership():
    s.send(bytes("CAP REQ :twitch.tv/membership\r\n", 'UTF-8'))

def capreq_commands():
    s.send(bytes("CAP REQ :twitch.tv/commands\r\n", 'UTF-8'))
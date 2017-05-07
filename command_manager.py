import cfg, time, random, irc_control
from bot import s, countdown, sender

#------------------------------------------------▼ !commands dictionary

#------▼ Admin only commands

def command_yolo():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, 'SWAG'), 'UTF-8'))

def command_swag():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, 'YOLO'), 'UTF-8'))

def command_clear():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, '.clear'), 'UTF-8'))

def command_leave():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, 'OK, fine. Later Scrublords!'), 'UTF-8'))
    time.sleep(1)
    countdown(cfg.sec)

#------▼ Non-Admin commands

def command_scrublord():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, 'Once a scrublord always a scublord'), 'UTF-8'))

def command_general(): #◄ 003 ▓
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, '/me knows: !roulette, !commands, "How art thou <Bot Name>?"'), 'UTF-8'))

#------▼ Soft Ban-Hammer

def command_purge(sender):
    s.send(bytes("PRIVMSG %s :%s %s 1\r\n" %(cfg.CHAN, '.timeout', sender), 'UTF-8'))



#------------------------------------------------▼ Bot Messages

def arrive_message():
    s.send(bytes("PRIVMSG %s :%s\r\n" %(cfg.CHAN, 'The Bot has arrived!'), 'UTF-8'))

#------------------------------------------------▼ The Bot know's that feel, bro

mood = [cfg.nice, cfg.fine, cfg.not_bad, cfg.ok, cfg.not_sure, cfg.frustrated, cfg.doin_great] 

def mood_swing():
    irc_control.send_message(cfg.CHAN,"@"+sender+random.choice(mood))
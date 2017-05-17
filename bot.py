#!/usr/bin/python3
import cfg, socket, re, time, sys
from irc_control import Controller
from msg_parser import GET_THIS, PARSE_THIS

HOST = cfg.HOST
PORT = cfg.PORT
NICK = cfg.NICK
PASS = cfg.PASS
CHAN = cfg.CHAN
'''DB_HOST = cfg.DB_HOST
DB_NAME = cfg.DB_NAME
DB_USER = cfg.DB_USER
DB_PASSWORD = cfg.DB_PASSWORD
DB_VIEWERS_TABLE = cfg.DB_VIEWERS_TABLE'''

ENGAGE = False
sec = cfg.sec # ◄ Set desired seconds to wait for script termination (0 is 1 sec)
MAXSENDINTERVAL = 20.0/30
    
#------------------------------------------------▼ Terminate Script Timer

def countdown(sec):
    print('Bot DISABLED!') 
    while (sec >= 0):
        print('Terminating script in:', sec,'seconds.')
        sec -= 1
        time.sleep(1)
    if sec == -1:
        irc.part_channel(CHAN)
        print('Safe to end this Process.')
        sys.exit()

#------------------------------------------------

data = ""
s = socket.socket()
irc = Controller(HOST, PORT, s)
irc.send_pass(cfg.PASS)
irc.send_nick(cfg.NICK)
irc.capreq_membership()
irc.capreq_commands()
#capreq_tags() -Works, but breaks adminList commands; possibly other things
irc.join_channel(cfg.CHAN)

#testing------------------------------
msg, sender = GET_THIS, PARSE_THIS
getData = GET_THIS(msg, sender)
parseData = PARSE_THIS(msg, sender)
#-------------------------------------

print('Initializing')

while True:
    
    try:
        data = data+s.recv(1024).decode('UTF-8')
        print (data)
        data_split = re.split(r"[~\r\n]+", data)
        data = data_split.pop()
            
        for line in data_split:
            line = str.rstrip(line)
            line = str.split(line)

            if len(line) >= 1:
                if line[0] == 'PING':
                    irc.send_pong(line[1])

                #testing------------------------------
                if line[1] == 'PRIVMSG':
                    sender = getData.get_sender(line[0])
                    message = getData.get_message(line)
                    parseData.parse_message(sender, message)
                    print('CHAT> '+sender +": " + message)

                if line[1] == 'JOIN':
                    sender = getData.get_sender(line[0])
                    #save_to_db(sender) ---------save & uncomment
                    print('▌VIEWER UPDATE: ' +'|' +sender +'|' +' has joined the chat!')
                    #send_message(CHAN, 'Welcome '+sender+'! Ya Scrub') -Turned off. May scare/trigger people

                if line[1] == 'PART':
                    sender = getData.get_sender(line[0])
                    print('▌VIEWER UPDATE: '+sender +' has left the chat! :(')
                #-------------------------------------
                
            while ENGAGE == False:
                print('I have arrived in ' + CHAN + "'s channel!")
                #arrive_message() ---Turned off
                time.sleep(1)
                ENGAGE = True
        time.sleep(MAXSENDINTERVAL)
                
    except socket.error:
        print("Socket lost")

    except socket.timeout:
        print("Socket timeout")

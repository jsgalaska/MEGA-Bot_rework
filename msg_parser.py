import cfg #re --import this when fixed 

#------------------------------------------------▼ Message parsing variables

adminList = [cfg.ADMIN1, cfg.ADMIN2, cfg.ADMIN3]
admin_command_list = ['^!swag $', '^!c $', '^!viewers $'] #◄ 000
general_command_list = ['^!yolo $', '^!roulette $', '^!commands $']
href_list = ['https://www.', 'www.', '.com', '.co', '.uk', '.jpg', '.gif']#◄ 001
leave_channel = '!exit' #◄ 002
scrublord = 'scrublord 4 life'
hat = 'how art thou '+cfg.NICK+'?'

#------------------------------------------------▼ get_stuff  
class GET_THIS():
    
    def __init__(self, msg, sender):
        self.msg=msg
        self.sender=sender
    
    def get_sender(self, msg):
        result = ""
        for char in msg:
            if char == "!":
                break
            if char != ":":
                result += char
        return result
    
    
    def get_message(self, msg):
        result = ""
        i = 3
        length = len(msg)
        while i < length:
            result += msg[i] + " "
            i += 1
        result = result.lstrip(':')
        return result
    
#------------------------------------------------▼ Message parsing
class PARSE_THIS():
    
    def __init__(self, msg, sender):
        self.msg=msg
        self.sender=sender
         
    def parse_message(self, sender, msg):
        if len(msg) >= 1:
            #split_msg = msg.split(' ') --uncomment when code is fixed
            
            '''
            #----------------------------------------▼ Admin !commands
            #Checks to see if sender is an admin

            for command in admin_command_list: #◄ 000
                if re.match(command, msg):
                    adminFile = None
                    print('▓ Admin command detected! ▓')
                    try:
                        with open('admins.txt', 'rt') as adminFile:
                            for line in adminFile: 
                                if sender in line:
                                    options = {
                                        '!swag': command_swag,
                                        '!c': command_clear
                                        }
                                    if split_msg[0] in options:
                                        options[split_msg[0]]()
                                    
                    except IOError:
                        print('▓▓ ▓▓ ERROR: Failed to load admins.txt! ▓▓ ▓▓')
                        return
                    
                    finally:
                        if adminFile is not None:
                            adminFile.close()
                        return
    
            #----------------------------------------▼ General Non-Admin commands
            #If sender is not an Admin, runs this
    
            for command in general_command_list:
                if re.match(command, msg):
                    print('▓ Command detected! ▓')
                    options = {
                        '!yolo': command_yolo,
                        #'!roulette': shoot_me_mofo,
                        '!commands': command_general
                        }
    
                    if split_msg[0] in options:
                        options[split_msg[0]]()
                        return
    
            #----------------------------------------▼ Link posting
            #if link posted, checks user's privilege
            
            for hlink in href_list: #◄ 001
                if hlink in msg.lower():
                    scrubsFile = None
                    link_privilege = None
                    print('▓ Hyperlink Detected!             ▓')
                    try:
                        with open('scrubs.txt', 'rt') as scrubsFile:
                            for line in scrubsFile: 
                                if sender in line:
                                    link_privilege = 1
                    except IOError:
                        print('▓▓ ▓▓ ERROR: Failed to load scrubs.txt! ▓▓ ▓▓')
                        return
                    
                    finally:
                        if link_privilege is None:
                            print('▓ Scrub not found; purging sender ▓')
                            command_purge(sender)
                            send_message(cfg.CHAN, 'Sorry, you were not authorized to do that, ' + sender)
                            
                        if scrubsFile is not None:
                            scrubsFile.close()
                        if link_privilege is not None:
                            link_privilege = None
                        return
                        
                        '''
    
            '''#----------------------------------------▼ Other message commands
    
            if scrublord in msg.lower():
                GENERAL_COMMANDS.command_scrublord()
            elif hat in msg.lower():
                mood_swing()
    
            elif leave_channel in msg.lower(): #◄ 002
                for user in adminList:
                    if sender == user:
                        ADMIN_COMMANDS.command_leave()
            else:
                return
            '''
        else: #-- delete when code is fixed
            return #-- delete when code is fixed
        

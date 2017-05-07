import cfg, random, time, command_manager, irc_control
from bot import sender

#------------------------------------------------▼ I wanna play a game

chamber = 0
cylinder = 0

def shoot_me_mofo():
    irc_control.send_message(cfg.CHAN, 'Six chambers; one ban-hammer, ' + sender + '. What will you get?')
    time.sleep(2)
    irc_control.send_message(cfg.CHAN, '/me loads a grenade and rotates the cylinder...')
    time.sleep(2)
    chamber = random.randint(1,6)
    cylinder = random.randint(1,6)
    if  cylinder == chamber:
        time.sleep(1)
        irc_control.send_message(cfg.CHAN, sender + ' JUST GOT REKT!!')
        command_manager.command_purge(sender)
    else:
        irc_control.send_message(cfg.CHAN, sender + ', you got lucky this time, scrub!')
        print('Bullet in:', chamber, 'of 6', 'Rotated to:', cylinder, 'of 6')
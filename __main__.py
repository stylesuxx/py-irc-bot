"""
Main entry point for the IRC bot.

Initialize the bot, load all needed modules and start the bot.
"""
from Bot import Bot


# Initialize the bot.
channel = '#foobar2342'
network = 'irc.freenode.net'
port = 6667
nick = 'support_1'
prefix = "!"
bot = Bot(network, port, nick, channel, prefix)

# Load the support module.
supporters = ['stylesuxx']
support_msg = ['Your presence has been requested in ' + channel]
channel_msg = ['The supporters have been notified that they are needed. ' +
               'Please stay tuned!',
               'Should nobody reply in a timly manner (idle at least for ' +
               '30 min) feel free to use the support forum located at ' +
               'https://forum.piratebox.cc/ which is checked on a daily ' +
               'basis.']
bot.load_module('Support', {'supporters': supporters,
                            'messages': {'channel': channel_msg,
                                         'support': support_msg}})

# Connect to the server and start processing commands.
bot.start()

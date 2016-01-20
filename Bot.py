"""Main functionality for the IRC bot."""
import irc.bot
import irc.strings


class Bot(irc.bot.SingleServerIRCBot):
    """IRC bot that connects to a server and processes commands."""

    def __init__(self, server, port, nick, channel, prefix='!'):
        """
        Initialize the IRC bot and connect to the server.

        Args:
            server (str): the IRC server to connect to
            port (int): the port to connect on
            nick (str): the nick used by the bot
            channel (str): the channel to join
            prefix (str): the prefix for commands (default: !)
        Raise:
            OverflowError: if port is out of range
        """
        self.modules = {}
        self.help = ['Available commands:']
        self.channel = channel
        self.prefix = prefix
        bot = irc.bot.SingleServerIRCBot
        bot.__init__(self, [(server, port)], nick, nick)

    def on_welcome(self, conn, event):
        """Join channel when welcome message is received from server."""
        conn.join(self.channel)
        print 'Joined ' + self.channel

    def on_pubmsg(self, conn, event):
        """Process messages received from the channel."""
        message = event.arguments[0].split(" ")[0]
        if(len(message) > 1 and message[0] == self.prefix):
            self.do_command(event, irc.strings.lower(message[1:]))

    def load_module(self, name, params):
        """
        Load a module with given parameters.

        Args:
            name (str): name of the module to load
            params (dict): parameters to initialize the module with
        Raise:
            TypeError: if a modules required parameters are missing
            ImportError: if the requested module could not be found
        """
        module = __import__("modules." + name, globals(), locals(), [name], -1)
        instance = getattr(module, name)(**params)
        command = instance.get_command()
        description = instance.get_description()
        help_msg = self.prefix + command + ': ' + instance.get_help()
        self.modules[command] = instance
        self.help.append(help_msg)
        print 'Loaded module "' + name + '": ' + description

    def do_command(self, event, command):
        """
        Process an incomming command.

        Args:
            event (object): event that triggered the command
            command (str): the command to process
        """
        conn = self.connection

        if command == 'help':
            nick = event.source.nick
            for line in self.help:
                conn.privmsg(nick, line)
            return

        for module in self.modules:
            if module == command:
                self.modules[module].process(conn, event)
                return

    def disconnect(self):
        """Disconnect from the IRC network."""
        pass

"""
Support Module.

Notifies the supporters that their help is needed. Posts a confirmation message
to the channel.
"""
from ..Module import Module


class Support(Module):
    """
    Support Module Class.

    Handles 'support' command.
    """

    def __init__(self,
                 supporters=[],
                 messages={'channel': [], 'support': []}):
        """
        Initialize the Support module.

        Params:
            supporters (list): supporters to message when the support command
                               is invoked.
            messages (dict):
                channel (list): lines to send to the channel when command is
                                invoked
                support (list): lines to send to the supporters wehn command is
                                invoked
        """
        self.command = 'support'
        self.description = ('Message the support staff that their help is ' +
                            'required and post a public message')
        self.help = 'Request assistance of the support team'

        self.supporters = supporters
        self.messages = messages

    def process(self, conn, event):
        """Process the support command."""
        target = event.target
        nick = event.source.nick

        for support in self.supporters:
            for line in self.messages['support']:
                conn.privmsg(support, line)

        for line in self.messages['channel']:
            conn.privmsg(target, line)

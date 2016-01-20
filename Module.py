"""Abstract Base Class for modules."""
from abc import ABCMeta, abstractmethod, abstractproperty


class Module(object):
    """All modules need to use this Abstract Base Class."""

    __metaclass__ = ABCMeta

    def __init__(command, description, help_msg):
        """
        All modules need to at least provide the follwoing attributes.

        Args:
            command (str): the name of the command
            description (str): short description of what the command does
            help_msg (str): the help text displayed to the user
        Raises:
            AttributeError: if one or more of the arguments is missing
        """
        self.command = command
        self.description = description
        self.help = help_msg

    def get_help(self):
        """Return the help message string."""
        return self.help

    def get_description(self):
        """Return the description string."""
        return self.description

    def get_command(self):
        """Return the command string."""
        return self.command

    @abstractmethod
    def process(self, connection, event):
        """
        Process the incomming command.

        Args:
            connection (object): the connection the command was received on
            event (object): the event that was received
        Raises:
            TypeError: if method is not implemented
        """
        pass

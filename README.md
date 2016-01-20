# Python IRC Bot
> A simple, extensible python IRC bot based on pythons IRC library.

## Setup
The bot setup happens in *__main__.py*. There you can set all the connection details and it is also the place where you load the modules you want to use.

## Run
To run the bot simply invoke it as a module from *outside* the root directory:
'''Bash
python -m py-irc-bot
'''

## Extend
This IRC bot is simple to extend with modules. There is an Abstract Base Class in place which modules need to use in order that they can be loaded. Modules have to be in the *modules* directory of the project. See the example **Support** module located in *modules/Support.py* for more details.

## Available commands
The only command that is always available is the *help* command. All other commands need to be implemented by a module.

## Dependencies
To install all dependencies needed (on a Debian based system) run:
```Bash
sudo pip install irc
```

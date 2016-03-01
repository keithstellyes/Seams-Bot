# Seams-Bot
Seams-bot allows for a highly modular interface for commands to grab and/or process data, with new interfaces easily made.
As of writing, it supports commands for things like rock-paper-scissors over SMS, a terminal interface, among others. 
Creating a new command is very simple, with documentation included that holds the potential programmer's hand to make a new one.
Like commands, creating a new interface for receiving commands and sending output is also very easy.

#Why? 
The core goal of the project initally was to maximize the amount of information that could be transferred over the SMS protocol.
I personally have an unlimited SMS plan, but limited data. However, the various modules will ideally be useful in other applications.
Python is used for its high portability.

#SMS Interface
To launch the SMS interface, launch the seamsbot-sms.py in your interpreter. As of right now, the current SMS implementation uses the 
Twilio service for this. You will need the various keys for the service, and every number must be verified via their website. 
The default polling rate is 45 seconds, I've found more frequent polling seems to cause Twilio's APIs to throw a fit after a while.
The interface also supports multi-user intercommunication (See the rock-paper-scissors script) 

#Terminal Interface
To launch the terminal interface, launch the seamsbot-terminal.py in your interpreter. 
The terminal interface still has only limited support for intercommunication.

#Some commands already in existence:
-Wikipedia articles and random Wikipedia articles on demand!

-Execute raw Python code! Return it or otherwise!

-Evaluate math equations!

-Send a list of numbers, get mean, median and mode!

-Get directions!

-Look up MTG cards!

-Look up information on a movie!

-Play rock-paper-scissors with a buddy over SMS!

-So much more to come

#Profiles
Currently, Seams-Bot supports profiles for recipients, to start a new game of rock-paper-scissors with Keith, instead of having to 
write out rps new <Keith's phone number>, the user can just write rps new [P::Keith::phonenumber]. Also, each user can have data
associated with them by individual commands. (See Tools available for the enterprising command or interface maker)

#Tools available for the enterprising command or interface maker
-Breakstrings: This allows for the interface to determine how to format it. While in an SMS, to separate points of data in say,
a movie data page, while a terminal might choose to use a separate new line, an SMS interface may just use |. Commands
aren't required to support it

-Associate data with profiles: All profiles can have data written and read through a simple interface. With each profile,
there is a series of pairs of strings, with the first used as an identifier to be accessed, and the second for the actual data in question.

-Define argument parameters: Does your command two arguments, does it want "wikipedia article Blade Runner" to be split as
["article","Blade Runner"]? Easy! Define it within the commands.json

#Miscellaneous features
-Alias contact information (instead of writing a phone number, just write [P::name::phonenumber])

-Permissions groups for various commands

#The future
-A combined communication mediums (Play rock-paper-scissors with someone texting while you sit at the terminal)

-More sophisticated multiplayer games (Porting other Python modules?)

-IRC and e-mail interfaces

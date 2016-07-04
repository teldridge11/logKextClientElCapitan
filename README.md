# logKextClientElCapitan
Code for updating logKext key logger on El Capitan

###Step 1
-Hold `⌘R` while starting your mac (This boots your computer in recovery mode).

-Navigate to Utilities → Terminal

-Type the command `csrutil disable` into Terminal. This disables System Integrity Protection. To reactive SIP, use the command `csrutil enable`.

-Restart your Mac

###Step 2
Now that SIP is disabled, you can download logKext from a place of your preference.

Download:
http://www.macupdate.com/app/mac/16155/logkext

###Step 3
Many people run into an issue where the keylogger stops logging after a short period of time.  To fix this, create a new file `logKextKiller.py`. (The code to create a logKextKiller daemon is included in this repository under `logKextKiller.py`)

###Step 4
In Terminal, run the command `open -e .bash_profile`.  (The code to put in your bash profile is also included in this repository under `bash_profile`)

After completing the above steps, logKext should work as explained in the README.

<b>README:</b>
https://code.google.com/p/logkext/wiki/ReadMe

<b>SOURCES:</b>

https://github.com/SlEePlEs5/logKext/issues/3

https://github.com/SlEePlEs5/logKext/pull/16/files?diff=split&short_path=04c6e90

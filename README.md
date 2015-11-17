# logKextClientElCapitan
Code for updating logKext key logger on El Capitan

STEP 1:

-Hold ⌘R while starting your mac (This boots your computer in recovery mode).

-Navigate to Utilities → Terminal

-Type `csrutil disable` into Terminal. This disables System Integrity Protection. To reactive, use `csrutil enable`.

-Restart your Mac

STEP 2:

Now that SIP is disabled, you can download logKext from a place of your preference.

http://www.macupdate.com/app/mac/16155/logkext

STEP 3:

Many people run into an issue where the keylogger stops logging after a short period of time.  To fix this, create a new file logKextKiller.py. (The code for this file is included in this repository.)

STEP 4:

In Terminal, run the command `open -e .bash_profile`.  (The code you need to add to your bash profile is also included in this repository.)

After completing the above steps, logKext should work as explained in the README.

https://code.google.com/p/logkext/wiki/ReadMe

SOURCES:

https://github.com/SlEePlEs5/logKext/issues/3

https://github.com/SlEePlEs5/logKext/pull/16/files?diff=split&short_path=04c6e90

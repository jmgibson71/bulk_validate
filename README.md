bulk_validate.py v1

Requires Python 3.4+ and [Library of Congress' bagit-python](https://github.com/LibraryOfCongress/bagit-python) installed.

Requires pywin32

If pip is installed in your python distribution, to install bagit-python just enter: 

`C:\pip install bagit`

To install pywin32 use this pip command.

`C:\pip install pywin32`

Usage: `bulk_validate.py [-f <PATH>] OR [-w <PATH>]`
    
Where `-f <PATH>` is the path to a plain text file. 
Each line of the file should be a unique path to a bag you want to validate.

Where `-w <PATH>` is the path to a TLD that may have bags underneath. 
This will walk the entire tree looking for bags and will validate any bag it finds.
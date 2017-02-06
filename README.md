bulk_validate.py v1

Requires Python 2.6+ and [Library of Congress' bagit-python](https://github.com/LibraryOfCongress/bagit-python) installed.

If pip is installed in your python distribution, to install bagit-python just enter: 

`C:\pip install bagit`

Usage: `bulk_validate.py -f <PATH> | -w <PATH>`
    
Where `-f <PATH>` is the path to a plain text file. 
Each line of the file should be a unique path to a bag you want to validate.

Where `-w <PATH>` is the path to a TLD that may have bags underneath. 
This will walk the entire tree looking for bags and will validate any bag it finds.
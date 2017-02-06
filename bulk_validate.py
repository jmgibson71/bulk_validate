from __future__ import division

import logging
import os
import sys
import getopt
import itertools


from bagit import *
from datetime import date
from datetime import datetime

paths_file = ""

d = date.today()
td = d.isoformat()

report_logger = logging.getLogger(__name__)
trim = []


def set_loggers(cwd):

        report_logger.setLevel(logging.DEBUG)

        handler_rl = logging.FileHandler(join(cwd, 'validation_report.log'))
        command_line = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s')

        handler_rl.setFormatter(formatter)
        command_line.setFormatter(formatter)

        report_logger.addHandler(handler_rl)
        report_logger.addHandler(command_line)


def get_time_in_seconds():
    time = datetime.now()
    return time.hour*3600 + time.minute*60 + time.second


def bag_validate(path):
    path = path.strip("\n")
    try:
        bag = Bag(path)
        report_logger.info("::VALIDATING:: %s" % path)
        begin = get_time_in_seconds()
        bag.validate(8)
        end = get_time_in_seconds()

        report_logger.info("::TIME TO VERIFY:: %d minute(s)" % ((end - begin) / 60))
        report_logger.info("::VALID::".rjust(4) + " ".rjust(4) + path.rjust(4))
        return 1
    except BagValidationError as e:
        report_logger.critical(e.message)
        return 1
    except BagError as be:
        report_logger.critical(be.args)
        return 1
    except OSError as we:
        report_logger.critical(we.strerror)
        report_logger.critical(we.filename)
        return 1
    except:
        e = sys.exc_info()[0]
        report_logger.critical(e.message)
        return 1


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def find_bag_path(path):
    print("Scanning {} for bags".format(path))
    bags = []
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    for root, dirs, files in os.walk(path):
        for f in files:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            sys.stdout.write('\b')
            if f == "bagit.txt":
                print("Found a bag.")
                bags.append(root)
    print("Validating bags...")
    for path in bags:
        bag_validate(path)


def help_text():
    print("Usage: bulk_validate.py -f <PATH> OR -w <PATH>\n")
    print("Where -f <PATH> is the path to a plain text file. Each line of the file should be a unique path to \n")
    print("a bag you want to validate.\n")
    print("Where -w <PATH> is the path to a TLD that may have bags underneath. This will walk the entire tree " \
          "looking for bags and will validate any bag it finds.")

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlp:f:i:w:")
    except getopt.GetoptError:
        help_text()
        sys.exit(2)

    set_loggers(os.getcwd())

    for opt, arg in opts:
        if opt == "-f":
            paths_file = open(arg, "r")
            for line in paths_file.readlines():
                bag_validate(line)
        if opt == "-i":
            bag_validate(arg)
        if opt == "-w":
            find_bag_path(arg)
        if opt == "-h":
            help_text()
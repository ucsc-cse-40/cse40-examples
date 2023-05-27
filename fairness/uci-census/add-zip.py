#!/usr/bin/env python3

import gzip
import os
import random
import re
import sys

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
TRAIN_PATH = os.path.join(THIS_DIR, 'adult.data.gz')
TEST_PATH = os.path.join(THIS_DIR, 'adult.test.gz')

SEED = 4
NUM_ZIPS = 10

RANDOM_NOISE = 0.005
NEGATIVE_CORRELATION = 0.20

def update_file(path, special_zipcode, zipcodes):
    output_lines = []

    with gzip.open(path, 'rt') as file:
        for line in file:
            negative_label = (', <=50K' in line)
            black = (', Black, ' in line)

            if (line.count(', ') == 15):
                print("ERROR: Found too many columns. Has the update already been made?")
                sys.exit(2)

            if (negative_label):
                chance = RANDOM_NOISE
                if (black):
                    chance = NEGATIVE_CORRELATION

                if (random.random() <= chance):
                    zipcode = special_zipcode
                else:
                    zipcode = random.choice(zipcodes)
            else:
                zipcode = random.choice(zipcodes)

            # Instead of splitting and risking removing quirks, just sub directly into the line.
            line = re.sub(r'(, (<=|>)50K\.?)$', r', %s\1' % (zipcode), line)

            output_lines.append(line)

    with gzip.open(path, 'wt') as file:
        file.write(''.join(output_lines))

def main():
    if (not os.path.isfile(TRAIN_PATH)):
        print("ERROR: Cannot find training data next to this script: '%s'." % (TRAIN_PATH))
        sys.exit(1)

    if (not os.path.isfile(TEST_PATH)):
        print("ERROR: Cannot find test data next to this script: '%s'." % (TEST_PATH))
        sys.exit(1)

    random.seed(SEED)

    zipcodes = ["%05d" % (random.randint(1, 99999)) for i in range(NUM_ZIPS)]
    special_zipcode = zipcodes[0]
    zipcodes = zipcodes[1:]

    update_file(TRAIN_PATH, special_zipcode, zipcodes)
    update_file(TEST_PATH, special_zipcode, zipcodes)

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 0 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s" % (exe), file = sys.stderr)
        sys.exit(1)

if (__name__ == '__main__'):
    _load_args(list(sys.argv))
    main()

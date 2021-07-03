#!/usr/bin/env python3
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Outputs info about mkv tracks')
parser.add_argument('paths', nargs='+', help='Paths of files', type=Path)
args = parser.parse_args()
for file in args.paths:
    os.system('mkvinfo ' + str(file.resolve()) + ' | grep -E \'Track number|Name|Track type|Track$|Error|Language\'')
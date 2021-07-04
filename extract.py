#!/usr/bin/env python3
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Outputs info about mkv tracks')
parser.add_argument('rus_track', help='number of rus subs track', type=int)
parser.add_argument('eng_track', help='number of eng subs track', type=int)
parser.add_argument('paths', nargs='+', help='Paths of files', type=Path)
args = parser.parse_args()
print(args)
for file in args.paths:
    path = str(file)
    os.system('mkvextract tracks ' + path + " " + str(args.rus_track) + ':' + path[:-4] + '_rus.srt')
    os.system('mkvextract tracks ' + path + " " + str(args.eng_track) + ':' + path[:-4] + '_eng.srt')
#!/usr/bin/env python3

from intelhex import IntelHex
import argparse
import pathlib
import sys

class Config:
    source = 0
    destination = 0
    length = 0

    def __init__(self, line):
        length, location = line.split('@')
        source, destination = location.split('->')

        self.length = int(length.strip(), 10)
        self.source = int(source.strip(), 16)
        self.destination = int(destination.strip(), 16)

parser = argparse.ArgumentParser(description='Transform given Intel HEX file using transformation table')
parser.add_argument('config', type=lambda p: pathlib.Path(p).absolute(), help="Transformation table path")
parser.add_argument('input', type=lambda p: pathlib.Path(p).absolute(), help="Input hex file")
parser.add_argument('output', type=lambda p: pathlib.Path(p).absolute(), help="Output hex file")

try:
    args = parser.parse_args()
except:
    sys.exit(-1)

conf = []
with open(args.config, 'r') as configFile:
    for line in configFile.readlines():
        conf.append(Config(line))

inputHex = IntelHex()
inputHex.loadhex(args.input)

outputHex = IntelHex()

for c in conf:
    outputHex.puts(c.destination, inputHex.gets(c.source, c.length))

with open(args.output, 'w') as output:
    outputHex.tofile(output, format='hex')
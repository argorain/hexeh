# HexeH

This is simple transformation tool for moving bytes around inside Intel HEX files.

Idea is following:
 1. Create transformation table
 2. Take input hex file and together with transformation table create new transformed hex file

## Transformation table

Transformation table is heart of this tool. It has following synopsis:
```
4@0x12345678->0x24680abc
```
which can be explained like this:
```
how many bytes @ from source address -> to destination address
```
And then just have as many lines as you like.

## Usage
Just call it. It has 3 positional parameters and help, nothing more, nothing less.
```
$ ./hexeh.py transform.cfg input.hex output.hex
```

## Contributing
Sure, why not. Just fork it and create PR.

## Author
Vojtech Vladyka, 2023


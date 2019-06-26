#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main ():
    pdf = read_pdf(input("Filename:"), lambda x: True)
    print(pdf)

def read_pdf(filename, filter_by):
    file_in = open(filename, "r")
    bufor = bytearray(file_in.read(64))
    out = ""
    while bufor:
        text = ''.join(e for e in bufor if filter_by(e) )
        out += text
        bufor = bytearray(file_in.read(64))
    file_in.close()
    return out


if __name__ == '__main__':
    import sys
    sys.exit(main())

#!/usr/bin/python3

from PyPDF2 import PdfReader, PdfWriter
import os
import sys
import math

def extractpdf(inf, outf, pagelist):
    writer = PdfWriter()
    with open(inf, 'rb') as infile:
        reader = PdfReader(infile)
        totaln = len(pagelist)
        npage = 0
        print ('0%\r', end='', flush=True)
        for pagen in pagelist:
            print (str(math.floor((100 * npage) / totaln)) + '%\r', end='', flush=True)
            npage += 1
            page = reader.pages[pagen - 1]
            page.compress_content_streams()
            writer.add_page(page)
            with open(outf, 'wb') as outfile:
                writer.write(outfile)
        print('100%\n')

def main():
    if len(sys.argv) < 4 or (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == '-h')):
        print('usage: pdfextract.py <input file> <output file> [pages]')
        exit()
    infile = sys.argv[1]
    outfile = sys.argv[2]
    pagelist = [int(a) for a in sys.argv[3:]]
    extractpdf(infile, outfile, pagelist)

if __name__ == "__main__":
    main()
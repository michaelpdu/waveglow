import os
import re
import argparse
from logger import WaveglowLogger

def convert(input_file, output_dir):
    logger = WaveglowLogger(output_dir)
    with open(input_file, 'r') as fh:
        for line in fh.readlines():
            m = re.match(r"(\d{1,5}):\s*(-\d.\d{9})", line)
            if m:
                iteration = m.group(1)
                loss = m.group(2)
                logger.log(loss, iteration)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert shell output to log of tensorboard!')
    parser.add_argument("-i", "--input", type=str, help="input filelist")
    parser.add_argument("-o", "--output_dir", type=str, help="output dir")
    args = parser.parse_args()
    if args.input:
        convert(args.input, args.output)
    else:
        parser.print_help()
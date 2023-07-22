""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import argparse
if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    sentance_arg = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile")
    sentance_arg.add_argument("infile", type=argparse.FileType('r'))
    sentance_arg.add_argument("outfile", type=argparse.FileType('w'))
    obj_arg = sentance_arg.parse_args()
    
    os.makedirs(root_dir / "outputs", exist_ok=True)
    
    loaded_data = np.loadtxt(obj_arg.infile)
    
    mean_of_loaded_data = np.mean(loaded_data)
    mean_of_loaded_data_0 = loaded_data - mean_of_loaded_data
    dvision_std = np.std(mean_of_loaded_data_0)
    processed = mean_of_loaded_data_0 / dvision_std
    np.savetxt(obj_arg.outfile, processed,fmt='%.2e')

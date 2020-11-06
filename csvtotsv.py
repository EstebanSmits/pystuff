import pandas as pd 
import sys
import argparse

parser = argparse.ArgumentParser("Converts from TSV|CSV.")
parser.add_argument("-i", metavar="File input", type=argparse.FileType('r', encoding='UTF-8'),  required=True,help="Folder & File to import.",)
parser.add_argument("-o", metavar="File output", type=argparse.FileType('w', encoding='UTF-8'),  required=True, help="Folder &  File to output.")
args = parser.parse_args()
tsv_file=args.i.name
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv(args.o.name,index=False)

import pandas as pd 
import sys
import argparse

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('pandas')

parser = argparse.ArgumentParser("Converts from TSV|CSV.")
parser.add_argument("-i", metavar="File input", type=argparse.FileType('r', encoding='UTF-8'),  required=False,help="Folder & File to import.",default="sample.tsv")
parser.add_argument("-o", metavar="File output", type=argparse.FileType('w', encoding='UTF-8'),  required=False, help="Folder &  File to output.",default="sample.csv")
args = parser.parse_args()
csv_table=pd.read_table(args.i.name,sep='\t')
csv_table.to_csv(args.o.name,index=False)

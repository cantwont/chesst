from funcs.load_names import load_names
from funcs.process import process_names

names = load_names()
process_names(names, delay=3)
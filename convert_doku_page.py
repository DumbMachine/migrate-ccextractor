import os
import argparse
from utils import (get_dokuwiki_code, convert_from_doku, correct_links_and_media, correct_relative_links)

TEMP_DIR = "tmp"

parser = argparse.ArgumentParser(description='Convert Dokuwiki pages to a post for fastpages')
parser.add_argument('--file', default="", type=str, help='dokuwiki input file; should be txt')
parser.add_argument('--url', default="", type=str, help='url to dokuwiki file required')
args = parser.parse_args()

if args.file == "" and args.url == "":
    raise Exception("Atleast provide one argument")

if args.file:
    filename = args.file

if args.url:

    # Firstly we will scrape the file
    url = args.url
    filename = get_dokuwiki_code(url, TEMP_DIR)

convert_from_doku(path=filename)
correct_links_and_media(path=filename.replace("txt", "md"))
correct_relative_links(path=filename.replace("txt", "md"))

print(filename)
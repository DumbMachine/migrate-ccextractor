import os
import argparse
from utils import (get_dokuwiki_code, convert_from_doku, correct_links_and_media, correct_relative_links)

TEMP_DIR = "tmp"

pages = [
    "https://ccextractor.org/public:gsoc:ideas_page_for_summer_of_code_2020",

    "https://ccextractor.org/public:gsoc:complete708support",
    "https://ccextractor.org/public:gsoc:livetvooverinternet",
    "https://ccextractor.org/public:gsoc:jokertv",
    "https://ccextractor.org/public:gsoc:pythonbindings",
    "https://ccextractor.org/public:gsoc:dtmb",
    "https://ccextractor.org/public:gsoc:ocr",
    "https://ccextractor.org/public:gsoc:japanese",

    "https://ccextractor.org/public:gsoc:poormanrekognition2",
    "https://ccextractor.org/public:gsoc:poormantextract",

    "https://ccextractor.org/public:gsoc:sampleplatform",

    "https://ccextractor.org/public:gsoc:rokuchannel",
    "https://ccextractor.org/public:gsoc:pythonprofiler",
    "https://ccextractor.org/public:gsoc:ffmpeg-rust",
    "https://ccextractor.org/public:gsoc:rcloneweb2",
    "https://ccextractor.org/public:gsoc:swaglyrics",
    "https://ccextractor.org/public:gsoc:votecounter",
    "https://ccextractor.org/public:gsoc:mouseless",
    "https://ccextractor.org/public:gsoc:flutterrutorrent",
    "https://ccextractor.org/public:gsoc:cloudtorrent",
    "https://ccextractor.org/public:gsoc:linuxtuning",
    "https://ccextractor.org/public:gsoc:takehome",
    "https://ccextractor.org/start"
]

for url in pages:
    filename = get_dokuwiki_code(url, TEMP_DIR)
    convert_from_doku(path=filename)
    correct_links_and_media(path=filename.replace("txt", "md"))
    correct_relative_links(path=filename.replace("txt", "md"))

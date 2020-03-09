import os
import re
import requests

from bs4 import BeautifulSoup as html

regex = r"\((.*?)\)"
regex_media = r"\{\{(.*?)\}\}"

p = re.compile(regex)
media = re.compile(regex_media)

def get_dokuwiki_code(url, save_dir):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    if not os.path.isfile(f"{save_dir}/{url.split('/')[-1].replace('/', '-')}.txt"):
        res = requests.get(url+"?do=edit")
        if res.status_code == 200:
            content = html(res.text, 'lxml')
            dokutext = content.select("#wiki__text")[0]
            open(f"{save_dir}/{url.split('/')[-1].replace('/', '-')}.txt", "w+").write(str(dokutext.text))
            # return dokutext
    else:
        print("Skipping file already exists", f"{save_dir}/{url.split('/')[-1].replace('/', '-')}.txt")
    return f"{save_dir}/{url.split('/')[-1].replace('/', '-')}.txt"


def convert_from_doku(path):
    os.system(f"php convert.php {path}")

def correct_links_and_media(path):
    with open(path, 'r') as file:
        content = ""
        for line in file.readlines():
            line = line.replace("///", "://")
            content+=line
        for med in media.findall(line):
            if "youtube" in med:
                line = fr'''
        <div class="video">
            <figure>
                <iframe width="640" height="480" src="//www.youtube.com/embed/{med.split('>')[1].split('?')[0] }" frameborder="0" allowfullscreen></iframe>
            </figure>
        </div>'''
            else:
                line = "![]("+"https://ccextractor.org/_media/" + med.strip().replace("{{","").replace("}}","")+")"

            content+=line

    # Removing //s
    content = content.replace("\\\\", "")
    # Removing the meta title
    content = re.sub(r"~~META((.|\n)*)~~", "", content)
    open(path.replace('txt', 'md'), 'w').write(content.strip())

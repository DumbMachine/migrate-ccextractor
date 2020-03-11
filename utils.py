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
            last_update = get_last_update(url.split('/')[-1].replace('/', '-')).replace("/", "-")
            filename = url.split('/')[-1].replace('/', '-')
            open(f"{save_dir}/{last_update}-{filename}.txt", "w+").write(str(dokutext.text))
            # return dokutext
    else:
        print("Skipping file already exists", f"{save_dir}/{last_update}-{filename}.txt")
    return f"{save_dir}/{last_update}-{filename}.txt"


def convert_from_doku(path):
    os.system(f"php convert.php {path}")

def correct_links_and_media(path):
    with open(path, 'r') as file:
        content = ""
        for line in file.readlines():
            line = line.replace("///", "://")
            for med in media.findall(line):
                if "youtube" in med:
                    line = fr'''<div class="video">
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
    nocontent = re.sub(r"^~~META((.|\n)*)~~", "", content)
    open(path, 'w').write(nocontent.strip())


def correct_relative_links(path):
    with open(path, 'r') as file:
        content = ""
        for line in file.readlines():
        # for line in content.splitlines():
            if "public" in line:
                for search in p.findall(line):
                    if "https" not in search and "public" in search:
                        last_update = get_last_update(search.strip().replace("/", ":"))
                        if last_update is False:
                            last_update = "2020/20/20"
                            print("There was a problem with ", path)
                        line = line.replace(
                            search,
                            # f"/ccextractor-wiki-test/{last_update}/" + "-".join(search.split("/")) + ")"
                            f"/ccextractor-wiki-test/{last_update}/" + search.strip().replace("/", "-").lower() + ")"
                        )
            # for std_idx, end_idx in zip(
            #     findall("(", line), findall(")", line)
            # ):
            #     link = line[st_idx+1: end_idx]
            #     if "public" in link:
            #         last_update = get_last_update(link.strip().replace("/", ":"))
            #         if last_update is False:
            #             last_update = "2020/20/20"
            #         line = line.replace(
            #             link,
            #             f"/ccextractor-wiki-test/{last_update}/" + "-".join(link.split("/")) + ")"

            #         )
            content+=line
    content = re.sub(r"^~~META((.|\n)*)~~", "", content)
    open(path.replace('txt', 'md'), 'w').write(content.strip())

def get_last_update(endpoint):
    url = "https://www.ccextractor.org/"+endpoint+"?do=revisions"
    res = requests.get(url)
    if res.status_code == 200:
        content = html(res.text, 'lxml')
    try:
        return content.find_all("span", {"class": "date"})[0].text.split()[0]
    except IndexError:
        print ("Can't get", url)
        # raise Exception(url)
        return False

def findall(p, s):
    import re
    return [m.start() for m in re.finditer(p, s)]

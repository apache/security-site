from bs4 import BeautifulSoup
import os
from pathlib import Path
from urllib import error, request

def get_index(url):
    with request.urlopen(url) as resp:
        index = resp.read().decode('utf-8')
        soup = BeautifulSoup(index, 'html.parser')
        def link_to_subproject(tag):
            return tag.name == 'a' and \
                tag.has_attr('href') and \
                not tag.get('href').startswith('.')
        return soup.find_all(link_to_subproject)

def get_dirs(url):
    tags = get_index(url)
    def is_dir(tag):
        return tag.has_attr('href') and tag.get('href').endswith('/')
    def as_str(tag):
        return tag['href'][:-1]
    return list(map(as_str, list(filter(is_dir, tags))))

def get_files(url):
    tags = get_index(url)
    def is_file(tag):
        return tag.has_attr('href') and not tag.get('href').endswith('/')
    def as_dict(tag):
        return {
            'title': tag.get('title'),
            'href': tag.get('href'),
        }
    return list(map(as_dict, filter(is_file, tags)))

# Returns (and caches) a None for URLs that are either empty
# or are not found
def get_url_cached(url):
    filename = "cache/" + "".join(x for x in url if x.isalnum())
    if not os.path.exists(filename):
        os.makedirs("cache", exist_ok=True)
        with open(filename, "w") as out:
            try:
                with request.urlopen(url) as resp:
                    response = resp.read().decode('utf-8')
                    out.write(response)
                    out.close()
            except error.HTTPError as e:
                if e.status == 404:
                    Path(filename).touch()
                else:
                    raise e

    with open(filename, "r") as i:
        try:
            return i.read()
        except Exception as e:
            print(f"Failed to parse {filename}")
            print(f"for {url}")
            raise e

def get_sbom_cached(url, to):
    filename = "sboms/" + to
    if not os.path.exists(filename):
        os.makedirs(os.path.abspath(os.path.join(filename, os.pardir)), exist_ok=True)
        with request.urlopen(url) as sbomPayload:
            with open(filename, "w") as out:
                out.write(sbomPayload.read().decode('utf-8'))
    with open(filename, "r") as i:
        return i.read()


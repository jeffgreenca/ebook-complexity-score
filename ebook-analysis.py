#!/usr/bin/python3
from os import path
from glob import glob
import textstat
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def iter_paragraphs(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
    for p in soup.find_all("p"):
        yield p.get_text()


def iter_chapters(target):
    book = epub.read_epub(target)

    for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        if x.is_chapter():
            yield "\n".join(iter_paragraphs(x))


def score(text):
    text = "\n".join(iter_chapters(target))
    return textstat.flesch_reading_ease(text), textstat.smog_index(text), textstat.dale_chall_readability_score(text)


if __name__ == "__main__":

    with open("targets.txt", "r") as f:
        sources = list(map(str.strip, f.readlines()))

    print("flesch\tsmog\tdale-chall\tbook")
    for src in sources:
        for target in glob(path.join(src, "**", "*.epub"), recursive=True):
            s = score(target)
            title = path.basename(target).replace(".epub", "")
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{title}")
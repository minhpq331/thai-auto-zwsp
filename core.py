import re
from typing import List

from icu import BreakIterator, Locale 

def genwords(text: str) -> str:
    bi = BreakIterator.createWordInstance(Locale("th"))
    bi.setText(text)
    start = bi.first()
    for end in bi:
        yield text[start:end]
        start = end


def insert_word_break(text: str) -> str:
    values = list(genwords(text))
    return '\u200b'.join(values)


def segment(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        return []

    text = text.replace('\u200b', '')
    content = text

    # detect Thai words only
    pattern = re.compile(r'[\u0E00-\u0E7F]+')
    for m in re.finditer(pattern, text):
        value = m.group(0)
        content = content.replace(value, insert_word_break(value), 1)

    return content

from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize wikipedia"""

    print(f"Finding wkipedia summary for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """Getting text blob object and return"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and return back phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases



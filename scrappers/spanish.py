from util import get_page_source


class SpanishScrapper:

  def get_nouns(self):
    return []

  def get_adjectives(self):
    return []

  def get_verbs(self):
    return []

  def get_words(self):
    nouns = self.get_nouns()
    adjectives = self.get_adjectives()
    verbs = self.get_verbs()

    return { 'nouns': nouns, 'adjectives': adjectives, 'verbs': verbs }

from util import get_page_soup, get_page_source


class EnglishScrapper:
  nouns_url = 'https://www.wordexample.com/list/most-common-nouns-english'
  adjectives_url = 'https://www.wordexample.com/list/most-common-adjectives-english'
  verbs_url = 'https://www.wordexample.com/list/most-common-verbs-english/'

  def get_nouns(self):
    soup = get_page_soup(self.nouns_url)
    nouns = self._parse_wordexample(soup)

    return nouns

  def get_adjectives(self):
    soup = get_page_soup(self.adjectives_url)
    adjectives = self._parse_wordexample(soup)

    return adjectives

  def get_verbs(self):
    soup = get_page_soup(self.verbs_url)
    verbs = self._parse_wordexample(soup)

    return verbs

  def get_places(self):
    return []

  def get_people(self):
    return []

  def get_words(self):
    nouns = self.get_nouns()
    adjectives = self.get_adjectives()
    verbs = self.get_verbs()
    places = self.get_places()
    people = self.get_people()

    return {
      'nouns': nouns,
      'adjectives': adjectives,
      'verbs': verbs,
      'places': places,
      'people': people
    }

  def _parse_wordexample(self, soup):
    def parse_table_row(row):
      span = row.find('span', { 'class': 'word-popover' })
      word = span.get_text().strip()
      return word

    table_div = soup.find(id='wordexample-word-list')
    table = table_div.find('table', { 'class': 'table' })
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    words = list(map(parse_table_row, table_rows))

    return words

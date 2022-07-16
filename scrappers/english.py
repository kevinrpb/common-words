from util import get_page_soup


class EnglishScrapper:
  nouns_1000_url = 'https://www.wordexample.com/list/most-common-nouns-english'

  def get_nouns(self):
    def parse_table_row(row):
      span = row.find('span', { 'class': 'word-popover' })
      noun = span.get_text().strip()
      return noun

    soup = get_page_soup(self.nouns_1000_url)
    table_div = soup.find(id='wordexample-word-list')
    table = table_div.find('table', { 'class': 'table' })
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    nouns = list(map(parse_table_row, table_rows))

    return nouns

  def get_adjectives(self):
    return []

  def get_verbs(self):
    return []

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

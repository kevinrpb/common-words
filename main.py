#!/usr/bin/env python3

import json

from scrappers import EnglishScrapper, SpanishScrapper
from util import parse_args, setup_logger


def main():
  args = parse_args()
  logger = setup_logger(level=args.log_level)
  logger.info('Starting')

  # Get the scrappers ready
  scrappers = {
    'en': EnglishScrapper,
    'es': SpanishScrapper
  }

  all_words = []
  for language in scrappers.keys():
    scrapper = scrappers[language]()
    words = scrapper.get_words()

    all_words = all_words + words

  # Now save the json file
  logger.info('Done')
  logger.info('Saving additives to file...')
  with open(f'words.json', 'w') as file:
    json.dump(all_words, file, indent=2)

if __name__ == '__main__':
  main()

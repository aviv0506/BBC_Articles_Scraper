from enum import Enum


class GeneralXpaths(Enum):
    HOME_PAGE_URL = '''https://www.bbc.com/'''
    HOME_PAGE_PROOF_ELEMENT = '''//h2[contains(@class, 'module__title')]'''
    HOME_PAGE_CONTENT = '''//a[contains(@class, 'block-link__overlay-link')]'''


class XpathsPages(Enum):
    WELCOME = '''//div[contains(@class, 'gel-layout__item gel-2/3@l')]'''
    SPORT = '''//div[contains(@class, 'gel-layout__item gel-2/3@l')]'''
    NEWS1 = '''//article[contains(@class, 'ssrcss-pv1rh6-ArticleWrapper e1nh2i2l6')]'''
    NEWS2 = '''//div[contains(@class, 'lx-o-panel lx-o-panel-is-commentary')]'''
    NEWS = '''//article[contains(@class, 'ssrcss-pv1rh6-ArticleWrapper e1nh2i2l6')] | //div[contains(@class, 'lx-o-panel lx-o-panel-is-commentary')]'''
    WORKLIFE = '''//div[contains(@class, 'article__body-content')]'''
    TRAVEL = '''//div[contains(@class, 'article__body')]'''
    FUTURE = '''//div[contains(@class, 'article__body-content')]'''
    CULTURE = '''//div[contains(@class, 'article__body-content')]'''

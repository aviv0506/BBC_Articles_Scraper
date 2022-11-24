from selenium import webdriver
from selenium.webdriver.common.by import By

from BBC_xpaths import GeneralXpaths, XpathsPages

import datetime
import json
import logging
import time


driver = webdriver.Firefox()
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)
json_obj_list = []


def login():
    try:
        driver.get(GeneralXpaths.HOME_PAGE_URL.value)
    except Exception as e:
        logging.warning("function login failed: %s", f'{e}')
        return e


def collect_articles():
    try:
        time.sleep(3)
        articles = driver.find_elements(By.XPATH, GeneralXpaths.HOME_PAGE_CONTENT.value)
        links = [elem.get_attribute('href') for elem in articles]
        return links
    except Exception as e:
        logging.warning("function collect_articles failed: %s", f'{e}')
        return e


def collect_article_data(article_list, num_of_articles):
    try:
        for idx, article in enumerate(article_list):
            if idx < num_of_articles:
                driver.get(article)
                time.sleep(5)
                current_page = article.rsplit('/')[3].upper()
                article_text = driver.find_element(By.XPATH, XpathsPages[f'{current_page}'].value)
                add_to_json(article, article_text.text, idx)

            else:
                current_time = datetime.datetime.now()
                with open(f'{current_time}.json', 'w', encoding='utf-8') as f:
                    json.dump(json_obj_list, f, ensure_ascii=False, indent=4)
                    break
    except Exception as e:
        logging.warning("function collect_article_data failed: %s", f'{e}')
        return e


def add_to_json(url, article_text, idx):
    try:
        json_obj_list.append({'dataset': f"dataSet-{idx}",
                              'results': {'URL': url, 'Data': article_text}})
    except Exception as e:
        logging.warning("function add_to_json failed: %s", f'{e}')
        return e


def input_validator(articles, num_of_articles):
    try:
        int(num_of_articles)
        if int(num_of_articles) > articles:
            logging.warning("function input_validator failed: %s",
                            'Number of requested articles cannot be bigger than total articles')
            raise Exception("Number of requested articles cannot be bigger than total articles")

        elif int(num_of_articles) <= 0:
            logging.warning('function input_validator failed: %s' 'Please enter a number higher than 0')
            raise Exception("Please enter a number higher than 0")

        else:
            return True

    except ValueError:
        logging.warning("function input_validator failed: ValueError")
        raise Exception("Please provide a number!")

    except Exception as e:
        logging.warning("function input_validator failed: %s", f'{e}')
        return e


def close_window():
    try:
        driver.close()
    except Exception as e:
        logging.warning("function close_window failed: %s", f'{e}')
        return e

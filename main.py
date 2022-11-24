from crawler import login, collect_articles, collect_article_data, input_validator, close_window
import logging


def run_crawler():
    try:
        login()
        articles = collect_articles()
        print(f'Number of articles:{len(articles)}\n')
        num_of_articles = input("Enter number of articles to download: ")
        is_data_valid = input_validator(len(articles), num_of_articles)
        collect_article_data(articles, int(num_of_articles))
        close_window()

    except Exception as e:
        logging.warning("function input_validator failed: %s", f'{e}')
        close_window()
        return e


if __name__ == '__main__':
    run_crawler()

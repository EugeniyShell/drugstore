from main.crawler import crawler_aptekamos


def drug_search(search_list):
    result = []
    for item in search_list:
        result += [crawl_it(item)]
    return result


def crawl_it(item):
    return crawler_aptekamos(item)

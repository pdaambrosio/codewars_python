def domain_name(url: str) -> str:
    """
    Split the url by "//", take the last element, split that by "www.", take the last element, split
    that by ".", take the first element
    
    :param url: str -> The url to be parsed
    :type url: str
    :return: The domain name of the url.
    """
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def main():
    print(domain_name("http://google.com")) # "google"
    print(domain_name("http://google.co.jp")) # "google"
    print(domain_name("www.xakep.ru")) # "xakep"
    print(domain_name("https://youtube.com")) # "youtube"


if __name__ == '__main__':
    main()

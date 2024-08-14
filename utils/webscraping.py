import requests
from bs4 import BeautifulSoup


def getPageHTML(url: str, params: dict | None = None, data: dict = None, auth=None):
    response = requests.get(url, params=params, data=data, auth=auth, verify=False)
    print(response.content.decode())
    return response.text


def getElement(
    html: str,
    tag: str | None = None,
    attribute: str | None = None,
    identifier: str | None = None,
):
    print(tag)
    print(attribute)
    print(identifier)

    bs = BeautifulSoup(html, "html.parser")

    if attribute == "id":
        result = bs.find(id=identifier)
    if attribute == "class":
        result = bs.find_all(tag, class_=identifier)

    return result


def parseHTML(html: str):
    bs = BeautifulSoup(html, "html.parser")
    return bs.prettify()

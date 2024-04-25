
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlsplit
import re


def text_from_html(body):
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.findAll(['p', 'h1', 'h2', 'h3', 'h4', 'li', 'ul'])
    return_texts = []
    
    for t in texts:
        return_texts.append(t.text.strip())

    return_texts = " ".join(return_texts)

    return return_texts


def reg_privacy(element):
    if re.search("privacy", element.text, re.IGNORECASE) is not None:
        return True
    else:
        return False
    

def reg_policy(element):
    if re.search("privacy", element.text,re.IGNORECASE) is not None and re.search("policy", element.text, re.IGNORECASE) is not None:
        return True
    else:
        return False
    

def reg_lang(element):
    if re.search("english", element.text, re.IGNORECASE) is not None:
        return True
    else:
        return False


def dig(element, func):
    if(func(element)):
        return True

    for child in element.findChildren():
        if func(child):
            return True
        elif dig(child, func):
            return True
        
    return False


def tag_privacy(element):
    return dig(element, reg_privacy)


def tag_policy(element):
    return dig(element, reg_policy)


def tag_lang(element):
    return dig(element, reg_lang)


def get_to_policy(url):
    split_url = urlsplit(url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a', href=True)
    viable_links = list(filter(tag_policy, anchors))
    if len(viable_links) == 0:
        viable_links = list(filter(tag_privacy, anchors))
    if len(viable_links) == 0:
        return "No policy found"
    
    if len(viable_links) > 1:
        for link in viable_links:
            if link.text.lower() == 'privacy policy':
                viable_links = [link]
                break
    
    if len(viable_links) > 1:
        for link in viable_links:
            if link.text.strip().lower() == 'privacy':
                print(link.text.lower())
                viable_links = [link]
                break
    
    curr_link = viable_links[0]['href']

    if curr_link[0] == '/':
        curr_link = "https://"+split_url.netloc+curr_link

    return curr_link

    # html = urllib.request.urlopen(curr_link).read()
    # soup = BeautifulSoup(html, 'html.parser')
    # anchors = soup.find_all('a', href=True)
    # viable_links = list(filter(tag_lang, anchors))
    
    # if len(viable_links) != 0:
    #     curr_link = viable_links[0]['href']
    #     if curr_link[0] == '/':
    #         curr_link = "https://"+split_url.netloc+curr_link

    # return curr_link

def extract_policy(url):
    link = get_to_policy(url)

    if(link == "No policy found"):
        return link

    # return link

    html = urllib.request.urlopen(link).read()
    
    return text_from_html(html)

def summarize_policy(text):
    pass

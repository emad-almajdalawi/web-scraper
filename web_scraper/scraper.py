import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    '''
    A function to count the number of citation-required paragraphs
    input: url
    outpus: number of citation-required paragraphs
    '''
    counter = 0
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    parser_output = soup.find('div', class_='mw-parser-output')
    paragraphs = parser_output.find_all('p') # or find_all('i') with different condetion
    for p in paragraphs:
        ankers = p.find_all("a", title="Wikipedia:Citation needed")
        for _ in ankers: # or counter = len(ankers)
            counter += 1
    return counter



def get_citations_needed_report(url):
    '''
    A function to generate a report including these paragraphs
    input: url
    outpus: number of citation-required paragraphs
    '''
    output = 'The following paragraphs need citation \n \n'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    parser_output = soup.find('div', class_='mw-parser-output')
    paragraphs = parser_output.find_all('p')  # you can use paragraphs = parser_output.find_all("a", title="Wikipedia:Citation needed").parent  or .find_parent()
    for p in paragraphs:
        text = p.text
        count = text.count('[citation needed]')
        check = ('[citation needed]' in text)
        if check:
            if count == 1:
                index = text.index('[citation needed]')
                output += text[0:index-1]
                output += '\n \n'
            if count >1:
                multi = text.split('[citation needed]')
                i = 0
                for _ in range(len(multi)-1):
                    output += multi[i]
                    output += '\n \n'
                    i+=1

    return output


#streach goal
def get_citations_needed_by_section(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    pass


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))

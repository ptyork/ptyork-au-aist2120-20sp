import requests
import bs4

# rsp = requests.get("https://en.wikipedia.org/wiki/Tower_Records")
# rsp.raise_for_status()
# html_text = rsp.text

with open('tower.html','rb') as file:
    html_text = file.read()

# print(html_text)

soup = bs4.BeautifulSoup(html_text, 'html.parser')
print(soup.title)
print(soup.title.text)

h1_counter = 0
h2_counter = 0
h3_counter = 0

# for elem in soup.select('h1'):        # single element selector
for elem in soup.select('h1,h2,h3'):    # multi-element selector (commas)
    text = elem.text.strip()
    if elem.name == 'h1':
        h1_counter += 1
        print(f"{h1_counter}: {text}")
    elif elem.name == 'h2':
        h2_counter += 1
        print(f'    {h2_counter}: {text}')
    elif elem.name == 'h3':
        h3_counter += 1
        print(f'        {h3_counter}: {text}')

info = soup.select_one('.infobox')
#print(info.text.strip())
#link = info.select_one('.external')
link = info.select_one('a.external')
print(link.text)
print(link.get('href'))

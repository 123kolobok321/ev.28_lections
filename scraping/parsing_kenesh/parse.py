# import csv
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from multiprocessing import Pool



# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BeautifulSoup(html, 'lxml')
#     return soup

# def get_1page_links(soup):
#     links = []
#     container = soup.find('div', class_='grid-deputs')
#     items = container.find_all('div', class_='dep-item')
#     for item in items:
#         a = item.find('a').get('href')
#         link = 'http://kenesh.kg' + a
#         links.append(link)
#     return links

# def get_all_links():
#     res = []
#     for i in range(1, 6):
#         url = f'http://kenesh.kg/ru/deputy/list/35?page={i}'
#         html = get_html(url)
#         soup = get_soup(html)
#         page_links = get_1page_links(soup)
#         res.extend(page_links)
#     return res

# def get_deps_data(link):
#     html = get_html(link)
#     soup = get_soup(html)
#     name = soup.find('div', class_='deput-name').text
#     info = ' '.join(soup.find('div', class_='deput-info').text.strip().split())
#     bio = soup.find('div', class_='tab-content').text.strip()
#     img = 'http://kenesh.kg' + soup.find('div', class_='deput-image').find('img').get('src').replace(' ', '%20')
#     data = {'name': name, 'info': info, 'bio': bio, 'img': img, 'link': link}
#     return data

# def prepare_csv():
#     with open('deputy.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(['FIO', 'Info', 'Bio', 'Image', 'Link to page'])

# def write_to_csv(data):
#     with open('deputy.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['name'], data['info'], data['bio'], data['img'], data['link']])
#         print(f'{data["name"]} - parsed!')

# def make_all(link):
#     data = get_deps_data(link)
#     write_to_csv(data)




# def main():
#     prepare_csv()
#     links = get_all_links()
#     # for link in links: # последовательно
#     #     data = get_deps_data(link)
#     #     write_to_csv(data)
#     #  парралельно (многопоток)
#     with Pool(50) as pool:
#         pool.map(make_all, links)

# if __name__ == '__main__':




#     start = datetime.now()
#     main()
#     finish = datetime.now()
#     print(f'Parsing takes: {finish - start} time')




# 50 58   
# print(get_deps_data('http://kenesh.kg/ru/deputy/show/209/abdibaeva-aysarakan-nishanovna'))











# links = get_all_links()
# print(links, len(links))









# import csv
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from multiprocessing import Pool


# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BeautifulSoup(html, 'lxml')
#     return soup

# def get_1page_links(soup):
#     links = []
#     container = soup.find('nav', class_='header__inline-menu').find('ul', class_='list-menu list-menu--inline')
#     items = container.find_all('li', class_='list-menu list-menu--inline')
#     for item in items:
#         a = item.find('a').get('href')
#         link = 'https://richardtea.uk/ru' + a
#         links.append(link)
#     return links


# def main():
#     url = 'https://richardtea.uk/ru/collections'
#     # response = requests.get('https://richardtea.uk/ru/collections')
#     # print(response.status_code)
#     html = get_html(url)
#     soup = get_soup(html)
#     container = soup.find('div', class_='card card--card card--media color-background-1 gradient')
#     items = container.find('div', class_='card__inner  ratio')
#     for item in items:
#         link = items.find('h3', class_='card__heading').find('a', class_='full-unstyled-link').get('href')

# # .find('div', class_='card__information').find('h3', class_='card__heading')
        
#     print(link)



#     # def main():
# #     prepare_csv()
# #     links = get_all_links()
# #     # for link in links: # последовательно
# #     #     data = get_deps_data(link)
# #     #     write_to_csv(data)
# #     #  парралельно (многопоток)
# #     with Pool(50) as pool:
# #         pool.map(make_all, links)



    


# main()




# ### Эколенд

# import csv
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from multiprocessing import Pool


# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def get_1page_links(soup):
#     links = []
#     container = soup.find('div', class_='mega_menu').find('ul')
#     items = container.find_all('li', class_='mega_menu_item mega_menu_item_has_children')
#     for item in items:
#         link = item.find('a').get('href')
#         links.append(link)
#     return links



# def main():
#     url = 'https://ecoland.kg/product/voda-legenda-shoro-1500-ml/'
#     html = get_html(url)
#     soup = get_soup(html)
#     container = soup.find('div', class_='mega_menu').find('ul')
#     items = container.find_all('li', class_='mega_menu_item mega_menu_item_has_children')
#     for item in items:
#         link = item.find('a').get('href')
#         kat = item.find('a').text
#         print(kat)


# main()





























































































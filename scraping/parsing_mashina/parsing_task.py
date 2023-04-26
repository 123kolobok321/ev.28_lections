
# import requests 
# source = requests.get('https://stackoverflow.com/questions').status_code
# # source = url.status_code
# print(source)


# from bs4 
# import BeautifulSoup 
# import requests 
# import csv 
# source = requests.get('https://stackoverflow.com/questions').status_code 
# print(source)


# from bs4 import BeautifulSoup 
# import requests 
# import lxml
# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml')
# print('h1:', my_page.h1.text) 
# print('p:', my_page.p.text) 
# print('a:', my_page.a.get('href')) 




# from bs4 import BeautifulSoup
# import requests
# import lxml

# source = requests.get('https://wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml')
# a = my_page.find('div', class_ = 'central-featured-lang lang4').find('a')
# lang = a.find('strong').text
# num = a.find('small').find('bdi').text
# artik = a.find('small').find('span').text

# print(lang)
# print(num, artik)



# def getTitle(url):
#     from bs4 import BeautifulSoup
#     import requests
#     import lxml
#     source = requests.get(url).text
#     my_page = BeautifulSoup(source,'lxml')
#     if my_page('h1'):
#         return my_page('h1')
#     else:
#         return "Title could not be found"
        
# print(getTitle('http://www.example.com/'))






# from bs4 import BeautifulSoup
# import requests
# import lxml
# source = requests.get('https://enter.kg/').text
# my_page = BeautifulSoup(source,'lxml')


# from bs4 import BeautifulSoup
# import requests
# import lxml
# source = requests.get('https://enter.kg/').text
# my_page = BeautifulSoup(source,'lxml')


# from bs4 import BeautifulSoup
# import requests
# import lxml



# source = requests.get('https://enter.kg/').text
# my_page = BeautifulSoup(source, 'lxml')
# category_li = my_page.find('ul', class_="VMmenu").text.strip()
# category_list = re.sub("  +", ";!", category_li).split(';!')

# def find_category(categories: list, keyword: str) -> list:
#     res = [x for x in categories if x.startswith(keyword.capitalize())]
#     return res

# print(find_category(category_list, 'ноутбуки'))

# from bs4 import BeautifulSoup
# from requests import get

# html = get('https://enter.kg/').text
# soup = BeautifulSoup(html,'html.parser')
# container = soup.find('ul', class_='VMmenu')
# category_list = [x.text for x in container.find_all('a')]
# # print(category_list)


# def find_category(categories, keyword):
#     return [x for x in categories if keyword.lower() in x.lower()]

# print(find_category(category_list, 'Ноутбуки'))






































































































































































































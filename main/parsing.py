import requests
from bs4 import BeautifulSoup



# ur1="https://www.netflix.com/kr-en/title/81602889"
# response=requests.get(ur1)
# # print(response)
# web=response.text
# soup=BeautifulSoup(web,"html.parser")
# name=soup.find(name='h2').text
# span1=soup.find(name='span',class_='default-ltr-cache-1jhx29c-StyledContainer euy28770').text
# starring=soup.find(name='div',class_='default-ltr-cache-eywhmi ehsrwgm1').text
#
# print(name)
# print(span1)
# print(starring)











# url2="https://www.kinoafisha.info/rating/movies/"
# response=requests.get(url2)
# web=response.text
# soup=BeautifulSoup(web,"html.parser")
# name=soup.find_all(name='a',class_="movieItem_title")
# reg=soup.find_all(name='span',class_='movieItem_itemRating miniRating miniRating-good')
# with open('films.txt', 'w', encoding='UTF-8') as file:
#     for i in range(100):
#         print(str(i+1)+'.',name[i].text,reg[i].text,file=file)
#         print(name[i].get("href"),end='\n\n',file=file)



def pogoda():
    url3="https://sinoptik.ua/ru/pohoda/provintsiia-chkhunchkhon-namdo-asan"
    response=requests.get(url3)
    web=response.text
    soup=BeautifulSoup(web,"html.parser")
    c=soup.find(name='p',class_='R1ENpvZz').text
    b=soup.find(name='p',class_='GVzzzKDV').text
    img=soup.find(name='img',class_='iXU+aDg2').get("src")
    return f'{c}\n{b}\n',f'https://sinoptik.ua{img}'


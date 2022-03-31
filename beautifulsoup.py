import urllib.request##urllib라이브러리의 request라는 모듈을 임포트

from bs4 import BeautifulSoup

##보통의 크롤링은 url을 가져오고 그 안에서 html코드를 분석해서 원하는 데이터를 뽑음

url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='api_text_lines')


print(title)
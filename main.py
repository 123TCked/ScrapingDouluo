import requests
from lxml import etree

url = "https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/1.html"
while True:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    e = etree.HTML(response.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    url = f'https://dldl1.nsbuket.cc{e.xpath("//tr/td[2]/a/@href")[0]}'

    with open('douluo.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + '\n\n' + info)

    if url == "https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/":
        break
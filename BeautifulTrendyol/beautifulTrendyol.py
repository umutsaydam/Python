from bs4 import BeautifulSoup
import requests

searchItem = input("Aramak istediniğiniz ürün/kategori: ")

url = f"https://www.trendyol.com/sr?q={searchItem}&qt={searchItem}&st={searchItem}&os=1"
# sitenin linki (sr?q=) yazmamızın sebebi sitede herhangi bir arama yaptığınızda adres çubuğunda aradığınız ürünün sr?q = ürünAdı şeklinde gözükmesi
# ürünü parametre olarak gönderiyor olması

#      BeautifulSoup(HTML veya XML içeriği, html.parser veya xml.parser)
soup = BeautifulSoup(requests.get(url).content, "html.parser")

products = soup.find_all("div", {"class", "p-card-wrppr"})

for product in products:
    brand = product.find("span", {"class": "prdct-desc-cntnr-ttl"}).text
    model = product.find(
        "span", {"class": "prdct-desc-cntnr-name"}).text
    price = product.find("div", {"class": "prc-box-dscntd"}).text
    link = "https://www.trendyol.com" + \
        product.find("div", {"class": "p-card-chldrn-cntnr"}).a["href"]

    print(f"{brand}\n{model}\n{price}\n{link}\n")

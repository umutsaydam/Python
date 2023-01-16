from operator import le
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import time 

# Kullanıcıdan izlemek istediği içeriğin adını alalım.
watch =input("Ne İzlemek İstersiniz ?: ")

# Kullandığımız tarayıcının sahip olduğu driver uygulamasının konumunu ekleyerek tarayıcıyı açalım.
driver = webdriver.Edge(executable_path="C:\\Users\\Umut\\Downloads\\msedgedriver")

# Ana url
url = "https://www.youtube.com"

# url değişkeninde bulunan linki açalım.
driver.get(url)

# Sayfanın yüklenmesi adına ve bizim de fark etmemiz adına bekletelim.
time.sleep(3)

# Tarayıcıyı tam ekran yapalım.
driver.maximize_window()
time.sleep(2)

# arama çubuğunun adını yazalım
searchInput = driver.find_element(By.NAME, "search_query")

# Kullanıcının izlemek istediğini arama çubuğuna yazdıralım.
searchInput.send_keys(watch)
time.sleep(2)

# Enter tuşuna bastıralım.
searchInput.send_keys(Keys.ENTER)
time.sleep(1)

# BeautifulSoup ile sayfanın yapısını elde edelim.
soup = BeautifulSoup(driver.page_source,"html.parser")

# Listelenen ilk videoyu alalım
video = soup.find("a", {"id":"video-title"})

# Video süresini alalım.
videoLength = soup.find("span", {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text


# İlgili videoyu açtıralım.
driver.get(url+video['href'])



#   Bu alanda ise videonun süresini saniye cinsinden hesaplıyoruz.
print(videoLength)
print(len(videoLength))
watchTime = time.strptime(videoLength, "%M:%S")
waitTime = datetime.timedelta(minutes = watchTime.tm_min, seconds = watchTime.tm_sec).total_seconds()

time.sleep(waitTime)
driver.close()






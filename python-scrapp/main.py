import bs4
import requests




url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=98'
Contents = requests.get(url)


response = bs4.BeautifulSoup(Contents.text, "html.parser")
print(response)
import bs4
import requests




url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=98'
Contents = requests.get(url)
print(Contents.text)
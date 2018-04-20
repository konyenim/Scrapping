import bs4
import requests




url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=98'
Contents = requests.get(url)


response = bs4.BeautifulSoup(Contents.text, "html.parser")

data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0

for d in data:
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()

    i += 1

print(sholat)
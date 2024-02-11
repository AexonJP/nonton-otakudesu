from requests_html import HTMLSession
import requests
import json
from base64 import b64encode, b64decode
from requests import Session


def btoa(value: str) -> str:
  # btoa source: https://github.com/WebKit/WebKit/blob/fcd2b898ec08eb8b922ff1a60adda7436a9e71de/Source/JavaScriptCore/jsc.cpp#L1419
  binary = value.encode("latin-1")
  return b64encode(binary).decode()


def atob(value: str) -> str:
  binary = b64decode(value.encode())
  return binary.decode("latin-1")


# url = 'https://otakudesu.media/anime/sword-online-alicization-part-2-sub-indo/'
# ik=HTMLSession()
# ok = ik.get(url=url)


def pes(url):
  # url = 'https://otakudesu.media/episode/sawo-s2-episode-6-sub-indo/'
  ik = HTMLSession()
  ok = ik.get(url=url)

  # print("berikut ada tempat tempat nonton yang ada : ")
  # tempat_download = (
  #     ok.html.find('#embed_holder > div.mirrorstream > ul.m720p > li'))
  # pisah = (tempat_download[0].text).split('\n')
  # for i in range(len(tempat_download)):
  #   print(f'{i+1}. {pisah[i]}')
  # dimana = input('mau nonton dari provider mana : ')
  dimana = 1
  try:
    dimana = int(dimana)
  except:
    quit()
  dimana -= 1
  # dimana = dimana -1

  data = ok.html.html

  awals = data.find("<link rel='shortlink' href=") + len(
      "<link rel='shortlink' href=")
  bres = data[awals:awals + data[awals:].find('>')]
  panjang = (bres.find('=')) + len('=')
  id_data = bres[panjang:panjang + bres[panjang:].find("'")]
  return id_data, dimana


#disini yang sudah jadi


def cari_anime(cari):
  # cari = input('mau cari anime apa : ')
  url = f'https://otakudesu.media/?s={cari}&post_type=anime'
  ik = HTMLSession()
  ok = ik.get(url=url)
  list_nama = []
  list_gambar = []
  list_url = []

  for i in ok.html.find('a'):
    if (i.attrs['data-wpel-link'] == 'internal'):
      try:
        i.attrs['rel']
      except:
        try:
          i.attrs['title']
          # print(i)
          list_nama.append((i.html)[i.html.find('>') + 1:i.html.find('</a>')])
        except:
          pass

  for i in ok.html.xpath('/html/body/div/div/div/div/div/div/ul/li/img'):
    list_gambar.append(i.attrs['src'])

  for i in ok.html.find('a'):

    if (i.attrs['data-wpel-link'] == 'internal'):
      try:
        i.attrs['rel']
      except:
        try:
          i.attrs['title']
          list_url.append(i.attrs['href'])
        except:
          pass

  # print(f'berikut adalah anime yang dengan keyword {cari} :')
  # for i in range(len(list_nama)):
  #   print(f'{i+1}. {list_nama[i]}')
  # okeh = input("pilih yang mana : ")
  # try:
  #   okeh = int(okeh)
  # except Exception as e:
  #   print(e)
  # print(f'ini link nya : {list_url[okeh-1]}')
  return list_nama, list_gambar, list_url


def list_episode(url):
  ik = HTMLSession()
  ok = ik.get(url=url)
  list_url = []
  list_nama = []

  for i in ok.html.xpath('/html/body/div/div/div/div/ul/li/span/a'):
    list_url.append(i.attrs['href'])

  for i in ok.html.xpath('/html/body/div/div/div/div/ul/li/span/a/text()'):
    list_nama.append(i)

  # print('berikut adalah episode yang tersedia :')
  # for i in range(len(list_nama)):
  #   print(f'{i+1}. {list_nama[i]}')
  # okeh = input("pilih yang mana : ")
  # try:
  #   okeh = int(okeh)
  # except:
  #   quit()
  # print(f'ini link nya : {list_url[okeh-1]}')
  return list_url, list_nama


def link_nonton(url):
  session = Session()
  url = url

  session.head('https://otakudesu.media')

  id_anime, tempat_nonton = pes(url=url)

  a = ''
  try:
    #meminta link
    print('di try')
    with open('coookie.txt', 'r') as f:
      a = f.readline()

    response = session.post(
        url='https://otakudesu.media/wp-admin/admin-ajax.php',
        data={
            "id": f"{id_anime}",
            "i": f"{tempat_nonton}",
            "q": "480p",
            "nonce": a,
            "action": "2a3505c93b0035d3f455df82bf976b84"
        },
        headers={'Referer': 'https://otakudesu.media'})
    if (response.status_code == 403):
      raise ValueError
  except:
    #minta session
    print('di except')
    response = session.post(
        url='https://otakudesu.media/wp-admin/admin-ajax.php',
        data={"action": "aa1208d27f29ca340c92c66d1926f13f"},
        headers={'Referer': 'https://otakudesu.media'})

    with open('coookie.txt', 'w') as f:
      f.write((json.loads(response.text))['data'])
      a = (json.loads(response.text))['data']

    response = session.post(
        url='https://otakudesu.media/wp-admin/admin-ajax.php',
        data={
            "id": f"{id_anime}",
            "i": f"{tempat_nonton}",
            "q": "720p",
            "nonce": a,
            "action": "2a3505c93b0035d3f455df82bf976b84"
        },
        headers={'Referer': 'https://otakudesu.media'})

  print(response)

  link_nonton = atob((json.loads(response.text))['data'])
  tempat_awal = link_nonton.find('src="') + len('src="')
  tempat_akhir = link_nonton[tempat_awal:].find('"')
  hasil = link_nonton[tempat_awal:tempat_awal + tempat_akhir]
  return hasil


# anime = cari_anime()
# episode = list_episode(anime)
# nonton = link_nonton(episode)
# print(nonton)

# isi = requests.get('https://desustream.me/desudesuhd3/?id=MFdlYVNiaGpRa0p5T3lDSmI1SnRBMGxFWWMvV29EaENreEg4NG11Yi92RT0=')
# awal = isi.text.find("sources: [{'file':'") + len("sources: [{'file':'")
# akhir = isi.text[awal:].find("'")
# hasil = isi.text[awal:awal+akhir]
# print(hasil)

from test import link_nonton
from cobaLogin import informasi
try:
  from flask import Flask
  from threading import Thread
  # import kuramanimes
  # import nama
  # import kuramanimess
  from quart import redirect, render_template
  import requests
  import json
  from requests_html import HTMLSession
  import test as otakudesu
except:
  import os
  import sys
  os.system('pip install --no-input requests-html')
  os.system('pip install --no-input quart')
  # os.system('apt-get -y install gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget')
  os.execv(sys.executable, ['python'] + sys.argv)

app = Flask(__name__)


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


@app.route('/<namas>/<user>/<episodes>')
def hello_world(user, episodes, namas):
  print(f'mencoba menonton anime {namas}')
  # akbs = kuramanimes.oks(balik=int(episodes), namass=int(user), namas=namas)
  nama_anime, link_gambar, link_url = otakudesu.cari_anime(namas)
  okbss, list_nama = otakudesu.list_episode(link_url[int(user) - 1])
  ditonton = okbss[int(episodes) - 1]
  link_bro = otakudesu.link_nonton(ditonton)

  # if (akbs == 'tidak'):
  #   return redirect(location=(f'./{episodes}'))
  # elif (akbs == 'ga ada'):
  #   return '<body style="background-color:#33475b"><p>tidak di temukan???</p></body>'
  # return redirect(location=akbs) //unutk download anime langusng direct
  # <iframe src="https://desustream.me/updesu/?id=bkhBaSsyREErMFBOeEdSZGN5UFc1UT09" width="420" height="370" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
  return f'<body style="background-color:#33475b"><p style="color: rgb(255,255,255)">sedang menonton {list_nama[int(episodes) - 1]}</p><br><iframe src="{link_bro}" width="420" height="370" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe> <br> <br> <a href = "./{int(episodes)+1}" > <button > previous </button ></a><a href = "{link_bro}" > <button > download </button ></a><a href = "./{int(episodes)-1}" > <button > next </button ></a></body>'


@app.route('/nhentai')
def index():
  return '<body style="background-color:#33475b"><p style="color: rgb(255,255,255)">mau download nhentai code</p><input id="okes" type="text" name="serialNumber" /><button id="myBtns" onclick="window.location=' + f"'https://zglj3x-5000.csb.app/upload/'+" + " document.getElementById('okes').value;" + '">submit </button>  <script>var input = document.getElementById("okes");input.addEventListener("keypress", function(event) {  if (event.key === "Enter") {event.preventDefault();document.getElementById("myBtns").click();}});</script> </body>'


@app.route('/<namas>')
def ok(namas):
  nama_anime, link_gambar, link_url = otakudesu.cari_anime(namas)
  ccs = ''
  for ik in range(len(nama_anime)):
    ccs = ccs + f'<div style="height: 337px; max-width: 300px;"><a href = "/{namas}/{ik+1}"><div style="background-image:url(' +\
        f"'{link_gambar[ik]}'" +\
        f');background-size: cover;background-repeat: no-repeat;background-position: center center;height: 337px; width: 300px; "></div></a></div>' + \
        f'<a href = "/{namas}/{ik+1}" >' + '<button>' + \
        nama_anime[ik] + \
        '</button></a><br><br>'
  return f'<body style="background-color:#33475b; height:100%; width:100%"><p style="color: rgb(255,255,255)">ini anime yang di temukan dengan keyword "{namas}"</p><br>' + ccs + '</body>'


@app.route('/<namas>/<user>')
def okb(namas, user):

  # return '<p>episode berapa</p><input id="okes" type="text" name="serialNumber" /><button onclick="window.location=' + f"'/{namas}/{user}/'+"+" document.getElementById('okes').value;" + '">submit </button>'
  nama_anime, link_gambar, link_url = otakudesu.cari_anime(namas)
  okbss, list_nama = otakudesu.list_episode(link_url[int(user) - 1])
  opp = ''
  ikll = 0
  for okl in range(len(okbss)):
    ikll = ikll + 1
    opp = opp + f'<a href = "/{namas}/{user}/{okl+1}" >' + \
        f'<button> {list_nama[okl]} </button></a><br><br>'
  return f'<body style="background-color:#33475b"><p style="color: \
  rgb(255,255,255)">ada {ikll} episode yang di temukan</p><br>' + opp + '</body>'


@app.route('/')
def kks():
  return '<body style="background-color:#33475b"><p style="color: rgb(255,255,255)">mau download anime apa</p><input id="okes" type="text" name="serialNumber" /><button id="myBtns" onclick="window.location=' + f"'/'+" + " document.getElementById('okes').value;" + '">submit </button>  <script>var input = document.getElementById("okes");input.addEventListener("keypress", function(event) {  if (event.key === "Enter") {event.preventDefault();document.getElementById("myBtns").click();}});</script> </body>'


@app.route('/x/x/x/x', methods=['HEAD', 'GET'])
def oiii():
  # return {'HTTP/1.1': 200, 'Content-Length': 500, 'Content-Type': 'text/html'}

  # x = requests.get('https://www.w3schools.com/python/demopage.php')

  return render_template("oks.html").headers


@app.route('/y/y/y/y/<website>')
def reqs(website):
  url = 'https://cm8vgr-8191.csb.app/v1'
  website = website.replace('-', '/')
  myobj = {
      "cmd": "request.get",
      "url": f"http://{website}",
      "maxTimeout": 50000
  }

  x = requests.post(url, json=myobj)
  return json.loads(x.text)['solution']['response']


# @app.route('/api/tele/anime/<namas>')
# def douse(namas):
#   cc = ''
#   hb, hbb = nama.oks(namas=namas)

#   for i in hbb:
#     cc = cc + i + '\n'
#   return cc


# @app.route('/api/tele/anime/<namas>/<user>/<episodes>')
# def hello_worlds(user, episodes, namas):
#   print(f'mencoba menonton anime {namas}')
#   akbs = kuramanimes.oks(balik=int(episodes), namass=int(user), namas=namas)

  # if (akbs == 'tidak'):
  #   return redirect(location=(f'./{episodes}'))
  # elif (akbs == 'ga ada'):
  #   return 'ga ada apa2 disitu bodoh'
  # # return redirect(location=akbs) //unutk download anime langusng direct
  # return f'{akbs}'


@app.route('/locate/<yes>')
def ope(yes):
  return requests.get(f'https://{yes}').text

@app.route('/informasi')
def opexc():
  return informasi()


if __name__ == '__main__':
  keep_alive()
#   app.run(host='0.0.0.0', port=81)

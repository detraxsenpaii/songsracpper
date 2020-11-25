from flask import Flask, render_template, redirect, request
import requests
from flask.wrappers import Response
from bs4 import BeautifulSoup
from urllib.parse import quote
import html5lib

from sqlalchemy.sql.schema import Column

app = Flask(__name__)

BASE_URL = 'https://amlijatt.in/search.html?s='
# print(BASE_URL)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/search', methods=['Get', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form['song']

        Final_url = BASE_URL + quote(search)

        Response = requests.get(Final_url)
        data = Response.text
        soup = BeautifulSoup(data, features='html5lib')
        songlist = soup.find_all('div', class_='listItem songList')
        for item in songlist:
            adhundo = item.find('a').get('href')
            final_title = item.find('a').get('title')

            sitekilink = 'https://amlijatt.in'
            final_alink = sitekilink + adhundo

            title = final_title
            print(final_alink)
            final = final_alink
            return render_template('search.html', value=final, kvalue=title)

    else:
        return "no result found"
        print("ok")

        return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)

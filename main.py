import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_data():
  array = []
  url = 'https://time.com/'
  response = requests.get(url)
  html_content = response.text
  
  soup = BeautifulSoup(html_content, 'html.parser')

  section = soup.find('div', class_='partial latest-stories')
  links = section.find_all('a')

  
  for link in links:
        data = {
        'title': link.text.strip('\n'),
        'link': url.strip('/') + link.get('href')
        }
        array.append(data)

  return jsonify(array)

if __name__ == '__main__':
  app.run(debug=True)




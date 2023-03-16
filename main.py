import requests
from flask import Flask, jsonify, make_response, request, render_template

app = Flask(__name__)

PEXELS_API_KEY = 'Your API key for Pexels website'

@app.route('/images', methods=['GET'])
def get_images():
    query = request.args.get('query')
    if not query:
        return make_response(jsonify({'error': 'No query parameter provided'}), 400)
    
    response = requests.get(f'https://api.pexels.com/v1/search?query={query}&per_page=12', headers={'Authorization': PEXELS_API_KEY})
    if not response.ok:
        return make_response(jsonify({'error': 'Error fetching images from Pexels API'}), 500)
    
    data = response.json()
    images = [{'id': photo['id'], 'url': photo['src']['large']} for photo in data['photos']]
    return render_template('images.html', images=images) # render to external images.html file
    #return images  #to render a json 

if __name__ == '__main__':
    app.run(debug=True)
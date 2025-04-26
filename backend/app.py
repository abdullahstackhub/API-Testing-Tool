from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import time
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

# Basic utility to validate URL
def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

@app.route('/get', methods=['POST'])
def make_get_request():
    if request.method == 'POST': 
     data = request.get_json()
     start = time.time()
     sent_req = requests.get(data['url'], headers=data['headers'])
     duration = (time.time() - start) * 1000
     try:
          response_body = sent_req.json()
     except:
          response_body = sent_req.text
     final_data = {
          'method':'GET',
          'time': f'{duration:.2f}ms',
          'status_code': sent_req.status_code,
          'headers': dict(sent_req.headers),
          'body': response_body
     }
     return jsonify(final_data)  

@app.route('/post', methods=['POST'])
def make_post_request():
    data = request.get_json()
    url = data.get('url')
    headers = data.get('headers', {})
    body = data.get('body', {})
    format_type = data.get('bodyFormat', 'json')

    if not is_valid_url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    try:
        start = time.time()
        if format_type == 'json':
            response = requests.post(url, headers=headers, json=body)
        else:
            response = requests.post(url, headers=headers, data=body)
        duration = (time.time() - start) * 1000

        try:
            response_body = response.json()
        except:
            response_body = response.text

        return jsonify({
            'time': f'{duration:.2f}ms',
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response_body,
            'method':'POST',
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/put', methods=['POST'])
def make_put_request():
    data = request.get_json()
    url = data.get('url')
    headers = data.get('headers', {})
    body = data.get('body', {})
    format_type = data.get('bodyFormat', 'json')

    if not is_valid_url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    try:
        if format_type == 'json':
            response = requests.put(url, headers=headers, json=body)
        else:
            response = requests.put(url, headers=headers, data=body)

        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.text,
            'method':'PUT',
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete', methods=['POST'])
def make_delete_request():
    data = request.get_json()
    url = data.get('url')
    headers = data.get('headers', {})

    if not is_valid_url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    try:
        response = requests.delete(url, headers=headers)
        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.text,
            'method':'DELETE',
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/patch', methods=['POST'])
def make_patch_request():
    data = request.get_json()
    url = data.get('url')
    headers = data.get('headers', {})
    body = data.get('body', {})
    format_type = data.get('bodyFormat', 'json')

    if not is_valid_url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    try:
        if format_type == 'json':
            response = requests.patch(url, headers=headers, json=body)
        else:
            response = requests.patch(url, headers=headers, data=body)

        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.text,
            'method':'PATCH',
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/post-accept', methods=['POST'])
def post_accept():
            body = request.get_json()
            return jsonify({
                'body': body,
                'method':'POST',
            })

   
if __name__ == '__main__':
    app.run(debug=True, port=8000)
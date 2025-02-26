from bottle import route, request, run, template
import requests
import os


def download_pdf(url, output_path):
    if os.path.exists(output_path):
        return
    # Lakukan request ke URL
    response = requests.get(url)
    
    # Periksa apakah request berhasil (status code 200)
    if response.status_code == 200:
        # Simpan konten ke file PDF
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"File berhasil diunduh dan disimpan sebagai {output_path}")
    else:
        print(f"Gagal mengunduh file. Status code: {response.status_code}")


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# @post('/login') # or 
@route('/res/add', method='POST')
def res_add():
    # download_url = request.forms.download_url
    # filename = request.forms.filename

    # Menerima data JSON dari request
    data = request.json
    print("Data received:", data)
    
    download_url = data['download_url']
    filename = data['filename']
    print(filename, download_url)

    download_pdf(download_url, 'validator/skins/raw/'+filename)
        
    return "<p>OKAY.</p>"


run(host='localhost', port=3002)
from bottle import route, request, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# @post('/login') # or 
@route('/res/add', method='POST')
def res_add():
    download_url = request.forms.download_url
    filename = request.forms.filename
    print(filename, download_url)
        
    return "<p>OKAY.</p>"


run(host='localhost', port=3002)
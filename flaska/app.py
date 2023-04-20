from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def swagger_ui():
    return render_template('swagger_ui.html')

@app.route('/yaml')
def yamldownload():
    return send_from_directory(app.root_path, 'msh-swagger.yaml')
    
@app.route('/VisitNote')
def VisitNote():
    return send_from_directory(app.root_path, 'VisitNote.xml')

if __name__ == '__main__':
   app.run(debug=True, port=8003)
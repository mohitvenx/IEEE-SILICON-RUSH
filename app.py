from posixpath import basename
import flask
from flask import Flask, render_template, redirect, request
import os
from os.path import join, dirname, realpath
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
from werkzeug.utils import secure_filename
import os
import threading
import ntpath
import read_f
import pytesseract

UPLOAD_FOLDER = join(dirname(realpath('save.jpg')), "./file_input")
BOUNDING_FOLDER = join(dirname(realpath('save.jpg')), "./area-bbox-test")

ALLOWED_EXTENSIONS = {'png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BOUNDING_FOLDER'] = BOUNDING_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.secret_key = 'key'

# bounding_location = "C:/Users/Admin/OneDrive/Desktop/damaged_cars/area-bbox-test"
bounding_location = "./area-bbox-test"

os.environ["FLASK_DEBUG"] = "development"

port = 5000

location = './templates'


def allowed_file(filename):

    pp = '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    print(filename, pp)
    return pp


@app.route('/')
def home():
    return render_template("./index1.html")


@app.route('/crop')
def crop():
    return render_template("./cropper1.html", result = None)


@app.route('/<a>')
def available(a):
    flash('Please contact {} for concerns and queries'.format(a))
    return render_template("./index1.html", result=None, scroll='third')


@app.route('/')
def assess():
    return render_template("./index1.html", result=None, scroll='third')


@app.route('/assessment', methods = ['POST'])
def upload_and_classify():

    if 'file' not in request.files:
        print(request.files)
        return redirect(url_for('assess'))

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('assess'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        a = read_f.read(filepath)

        return render_template("./results.html", result=a, scroll='third', filename=filename)

    flash('Invalid file format. Please try again.')
    return redirect(url_for('assess'))

@app.route('/assessment/table')
def table():
    return render_template('./Table10.html')



@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/results/<filename>')
def send_boxfile(filename):
    basename = ntpath.basename(filename)
    return send_from_directory(BOUNDING_FOLDER, basename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/results/<filename>')
def uploaded_boxfile(filename):
    return send_from_directory(app.config['BOUNDING_FOLDER'], basename)


app.run(host="10.8.52.162",port='8999', use_reloader=True)

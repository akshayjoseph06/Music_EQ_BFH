import os
from os import path
import time
import subprocess

from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    #folder_name = request.form['files']
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    #target = os.path.join(APP_ROOT, '{}'.format(folder_name))
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".mp3") or (ext == ".mp3"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        time.sleep(10)
        os.system('cmd /k "ffmpeg -i "C:\\Users\\AKSHAY JOSEPH\\Desktop\\Temp\\BFH\\file_upload\\upload_file_python-master\\src\\images\\test.mp3" -filter_complex "[0:a]showwaves=s=128x96:mode=cline,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy "C:\\Users\\AKSHAY JOSEPH\\Desktop\\Temp\\BFH\\file_upload\\upload_file_python-master\\src\\images\\test.mp4""')

        print(completed)


    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", image_name=filename)
    
    
    print(completed)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)
    if bool(str(path.exists("test.mp3")))==True:
        print("Success")


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)











if __name__ == "__main__":
    app.run(port=4555, debug=True)

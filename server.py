from PIL import Image
import pytesseract
import flask

app = flask.Flask('api server')
# app.config["DEBUG"] = True

# image should to passed in formData with file key
@app.route('/imgToText', methods=['POST'])
def imgToText():
    try:
        req = flask.request
        files = req.files
        im = Image.open(files['file'])
        text = pytesseract.image_to_string(im, lang = 'eng')
        return { 'data' : text, 'status' : True }
    except:
        return {'msg' : 'something went wrong', 'status' : False}

app.run()

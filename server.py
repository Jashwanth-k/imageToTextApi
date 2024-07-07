from PIL import Image
import pytesseract
import flask
import io
import base64

app = flask.Flask('api server')
# app.config["DEBUG"] = True

@app.route('/imgToText', methods=['POST'])
def imgToText():
    try:
        req = flask.request
        base64_str = req.json['base64_str']
        # file = req.form['file']
        # im = Image.open(file)
        im = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
        text = pytesseract.image_to_string(im, lang = 'eng')
        return { 'data' : text, 'status' : True }
    except Exception as e:
        print(e)
        return {'msg' : 'something went wrong', 'status' : False}

app.run()

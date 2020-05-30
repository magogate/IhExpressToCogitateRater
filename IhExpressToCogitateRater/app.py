import ConvertXML as cxml
import time
#https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask
#https://stackoverflow.com/questions/10572498/importerror-no-module-named-sqlalchemy
# https://stackoverflow.com/questions/53978542/how-to-use-collections-abc-from-both-python-3-8-and-python-2-7

from flask import Flask, jsonify, render_template, flash, request, redirect, abort

app = Flask(__name__, static_url_path='/static')

# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
@app.route("/", methods=["POST","GET"])
def index():        
    if request.method == 'POST':  #this block is only entered when the form is submitted
        xmlValue = request.form.get('inputXml')
        # print(xmlValue)
        cxml.readXML(xmlValue)
        time.sleep( 2 )
        return redirect("http://localhost/NewRater/api/rater/SGIH-GAPPA")
    return render_template("index.html")  
    

if __name__ == "__main__":
    app.run(debug=True)
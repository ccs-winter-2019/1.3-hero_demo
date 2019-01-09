from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():

    input = request.args.get('search-term')
    print(input)

    if not input:
        input = ''

    # open file for reading, 'r'
    # file is saved to variable
    index_file = open('index.html', 'r')

    # read contents of the file
    my_html = index_file.read()
    my_html = my_html.replace("{{search-term-value}}",input)

    # close the file out when you're done
    index_file.close()

    return my_html
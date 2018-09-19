from flask import Flask, render_template
from flask import json


app = Flask(__name__, static_url_path='/static/')

with open('data.json') as articles:
    data=json.load(articles)


# posts = [
# {
#     'author': 'abcauthor',
#     'title': 'abctitle',
#     'content': 'abccontent',
#     'date_posted': 'September 02, 2018'
# },
# {
#     'author': 'defauthor',
#     'title': 'deftitle',
#     'content': 'defcontent',
#     'date_posted': 'September 04, 2018'
# }
# ]



@app.route("/")
@app.route("/home.html")
def home():
    return render_template('home.html', posts=data)

@app.route("/about.html")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

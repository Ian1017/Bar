from juice import app
from flask import render_template
from juice.models import Item

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/juice')
def juice_page():
    items = Item.query.all()
    return render_template('juice.html', items=items )


if __name__ == '__main__':
   app.run()
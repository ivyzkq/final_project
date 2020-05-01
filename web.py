from flask import Flask, render_template, request, redirect, url_for, session
from main import lookup_item

web = Flask(__name__)
web.secret_key = 'jadnmwjygvnosgaudsvnmfgiuvalfjg'
# web.secret_key = 'sddfklsdhdjkASKLFDHJrfDSFRPdf'

# @web.route('/',methods=['POST','GET'])
# def main():
#     '''
#     main page that greets the users and takes a text input of location
#     '''

#     if request.method =='POST':
#         place = request.form["nm"]
#         session['place'] = place
#         return redirect(url_for("place"))
#     else:
#         return render_template('index.html')

@web.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        item = request.form['nm']
        session['item']=item
        return redirect(url_for('search'))
    else: 
        return render_template('index.html')


@web.route('/item')
def search():
    if "item" in session:
        product = session['item']
        # f'Now displaying search result for {item}.'
        # return (f'<h1>{lookup_item(product)}</h1>')
        list_of_item = lookup_item(product)
        return render_template('result.html',list_of_item = list_of_item,input = product)
        
    else:
        return redirect(url_for('home'))

# @web.route('/exit')
# def exit():
#     print ('<h1>Thank you for using our site<h1> \n<h1>you will be redirect to a home page <h1>')
#     return redirect(url_for('home'))

@web.route('/exit')
def exit():
    session.pop('item',None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    web.run(debug=True)
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name


# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))



# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#    return render_template('test.html')

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('test.html', name = user)

# @app.route('/hello/<int:score>')
# def hello_name(score):
#    return render_template('test.html', marks = score)

@app.route('/')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('test.html', result = dict)







if __name__ == '__main__':
   app.run(debug = True)
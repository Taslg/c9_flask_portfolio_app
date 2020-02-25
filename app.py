from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
  if request.method == 'GET':
	return render_template('add_numbers.html')

  total = "no_one"

  Player_1_choices = []

  Player_2_choices = []

  while request.method == 'POST':
    total = "no_one"

    if Player_1_choices == ['(1,1)', '(1,2)','(1,3)'] or Player_1_choices == ['(1,1)', '(1,3)','(1,2)'] or Player_1_choices == ['(1,1)', '(2,2)','(3,3)'] or Player_1_choices == ['(1,1)', '(3,3)','(2,2)'] or Player_1_choices == ['(1,1)', '(2,1)','(3,1)'] or Player_1_choices == ['(1,1)', '(3,1)','(2,1)'] or Player_1_choices == ['(1,2)', '(1,1)','(1,3)'] or Player_1_choices == ['(1,2)', '(1,3)','(1,1)'] or Player_1_choices == ['(1,2)', '(2,2)','(3,2)'] or Player_1_choices == ['(1,2)', '(3,2)','(2,2)'] or Player_1_choices == ['(1,3)', '(1,2)','(1,1)'] or Player_1_choices == ['(1,3)', '(1,1)','(1,2)'] or Player_1_choices == ['(1,3)', '(2,3)','(3,3)'] or Player_1_choices == ['(1,3)', '(3,3)','(2,3)'] or Player_1_choices == ['(1,3)', '(2,2)','(3,1)'] or Player_1_choices == ['(1,3)', '(3,1)','(2,2)'] or Player_1_choices == ['(2,1)', '(2,2)','(2,3)'] or Player_1_choices == ['(2,1)', '(2,3)','(2,2)'] or Player_1_choices == ['(2,1)', '(1,1)','(3,1)'] or Player_1_choices == ['(2,1)', '(3,1)','(1,1)'] or Player_1_choices == ['(2,2)', '(1,2)','(3,2)'] or Player_1_choices == ['(2,2)', '(3,2)','(1,2)'] or Player_1_choices == ['(2,2)', '(2,1)','(2,3)'] or Player_1_choices == ['(2,2)', '(2,3)','(2,1)'] or Player_1_choices == ['(2,2)', '(1,2)','(3,2)'] or Player_1_choices == ['(2,2)', '(3,2)','(1,2)'] or Player_1_choices == ['(2,2)', '(1,1)','(3,3)'] or Player_1_choices == ['(2,2)', '(3,3)','(1,1)'] or Player_1_choices == ['(2,2)', '(1,3)','(3,1)'] or Player_1_choices == ['(2,2)', '(3,1)','(1,3)'] or Player_1_choices == ['(2,3)', '(2,2)','(2,1)'] or Player_1_choices == ['(2,3)', '(2,1)','(2,2)'] or Player_1_choices == ['(2,3)', '(1,3)','(3,1)'] or Player_1_choices == ['(2,3)', '(3,1)','(1,3)'] or Player_1_choices == ['(3,1)', '(2,2)','(1,3)'] or Player_1_choices == ['(3,1)', '(1,3)','(2,2)'] or Player_1_choices == ['(3,1)', '(3,2)','(3,3)'] or Player_1_choices == ['(3,1)', '(3,3)','(3,2)'] or Player_1_choices == ['(3,1)', '(2,1)','(1,1)'] or Player_1_choices == ['(3,1)', '(1,1)','(2,1)'] or Player_1_choices == ['(3,2)', '(2,2)','(1,2)'] or Player_1_choices == ['(3,2)', '(1,2)','(2,2)'] or Player_1_choices == ['(3,2)', '(3,1)','(3,3)'] or Player_1_choices == ['(3,2)', '(3,3)','(3,1)'] or Player_1_choices == ['(3,3)', '(2,3)','(1,3)'] or Player_1_choices == ['(3,3)', '(1,3)','(2,3)'] or Player_1_choices == ['(3,3)', '(1,1)','(2,2)'] or Player_1_choices == ['(3,3)', '(2,2)','(1,1)'] or Player_1_choices == ['(3,3)', '(3,2)','(3,1)'] or Player_1_choices == ['(3,3)', '(3,1)','(3,2)']:
      total = "Player 1"
      return render_template('add_numbers.html', result=str(total))
      break
    if total == "no_one":
      Player_2_choices.append(request.form['text'])
    
    if len(Player_1_choices) + len(Player_2_choices) == 9:
      total = "Draw"
      return render_template('add_numbers.html', result=str(total))
      break


      
    if Player_2_choices == ['(1,1)', '(1,2)','(1,3)'] or Player_2_choices == ['(1,1)', '(1,3)','(1,2)'] or Player_2_choices == ['(1,1)', '(2,2)','(3,3)'] or Player_2_choices == ['(1,1)', '(3,3)','(2,2)'] or Player_2_choices == ['(1,1)', '(2,1)','(3,1)'] or Player_2_choices == ['(1,1)', '(3,1)','(2,1)'] or Player_2_choices == ['(1,2)', '(1,1)','(1,3)'] or Player_2_choices == ['(1,2)', '(1,3)','(1,1)'] or Player_2_choices == ['(1,2)', '(2,2)','(3,2)'] or Player_2_choices == ['(1,2)', '(3,2)','(2,2)'] or Player_2_choices == ['(1,3)', '(1,2)','(1,1)'] or Player_2_choices == ['(1,3)', '(1,1)','(1,2)'] or Player_2_choices == ['(1,3)', '(2,3)','(3,3)'] or Player_2_choices == ['(1,3)', '(3,3)','(2,3)'] or Player_2_choices == ['(1,3)', '(2,2)','(3,1)'] or Player_2_choices == ['(1,3)', '(3,1)','(2,2)'] or Player_2_choices == ['(2,1)', '(2,2)','(2,3)'] or Player_2_choices == ['(2,1)', '(2,3)','(2,2)'] or Player_2_choices == ['(2,1)', '(1,1)','(3,1)'] or Player_2_choices == ['(2,1)', '(3,1)','(1,1)'] or Player_2_choices == ['(2,2)', '(1,2)','(3,2)'] or Player_2_choices == ['(2,2)', '(3,2)','(1,2)'] or Player_2_choices == ['(2,2)', '(2,1)','(2,3)'] or Player_2_choices == ['(2,2)', '(2,3)','(2,1)'] or Player_2_choices == ['(2,2)', '(1,2)','(3,2)'] or Player_2_choices == ['(2,2)', '(3,2)','(1,2)'] or Player_2_choices == ['(2,2)', '(1,1)','(3,3)'] or Player_2_choices == ['(2,2)', '(3,3)','(1,1)'] or Player_2_choices == ['(2,2)', '(1,3)','(3,1)'] or Player_2_choices == ['(2,2)', '(3,1)','(1,3)'] or Player_2_choices == ['(2,3)', '(2,2)','(2,1)'] or Player_2_choices == ['(2,3)', '(2,1)','(2,2)'] or Player_2_choices == ['(2,3)', '(1,3)','(3,1)'] or Player_2_choices == ['(2,3)', '(3,1)','(1,3)'] or Player_2_choices == ['(3,1)', '(2,2)','(1,3)'] or Player_2_choices == ['(3,1)', '(1,3)','(2,2)'] or Player_2_choices == ['(3,1)', '(3,2)','(3,3)'] or Player_2_choices == ['(3,1)', '(3,3)','(3,2)'] or Player_2_choices == ['(3,1)', '(2,1)','(1,1)'] or Player_2_choices == ['(3,1)', '(1,1)','(2,1)'] or Player_2_choices == ['(3,2)', '(2,2)','(1,2)'] or Player_2_choices == ['(3,2)', '(1,2)','(2,2)'] or Player_2_choices == ['(3,2)', '(3,1)','(3,3)'] or Player_2_choices == ['(3,2)', '(3,3)','(3,1)'] or Player_2_choices == ['(3,3)', '(2,3)','(1,3)'] or Player_2_choices == ['(3,3)', '(1,3)','(2,3)'] or Player_2_choices == ['(3,3)', '(1,1)','(2,2)'] or Player_2_choices == ['(3,3)', '(2,2)','(1,1)'] or Player_2_choices == ['(3,3)', '(3,2)','(3,1)'] or Player_2_choices == ['(3,3)', '(3,1)','(3,2)']:
      total = "Player 2"
      return render_template('add_numbers.html', result=str(total))
      break


    if total == "no_one":
      Player_1_choices.append(request.form['text'])

    if len(Player_1_choices) + len(Player_2_choices) == 9:
      total = "Draw"
      return render_template('add_numbers.html', result=str(total))
      break

@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)

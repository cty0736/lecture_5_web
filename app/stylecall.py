from flask import Flask, render_template ,flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from data import Articles
app = Flask(__name__)

#config mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'myflaskweb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initate mysql
mysql = MySQL(app)

@app.route('/mysql')
def users():
    cur = mysql.connection.cursor()
    sql = '''insert into users (name, email, username, password) values ('Hong','5@naver.com','gangnam5','1234');'''
    cur.execute(sql)
    mysql.connection.commit() #commit
    
    sql = '''desc users'''
    cur.execute(sql)
    
    rv = cur.fetchall()
    cur.close() #connection close
    
    return str(rv)

@app.route("/", methods=['GET','POST'])
def home():
	#return "Hello World!"
	#return "<html><body><h1>Hello World</h1></body></html>"
	return render_template('home.html')
@app.route("/about", methods=['GET','POST']) #맨 뒤에 아무것도 없다면 GET방식
def about():
	return render_template('about.html')
@app.route("/articles", methods=['GET','POST']) #맨 뒤에 아무것도 없다면 GET방식
def articles():
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', arti=articles)

@app.route("/articles/<int:id>", methods=['GET','POST']) #맨 뒤에 아무것도 없다면 GET방식
def articlesinfo(id):
    print(id)
    articles = Articles()
    data = articles[id-1]
    return render_template('articlesinfo.html', id=data)


@app.route("/gallery", methods=['GET','POST'])	
def gallery():
	return render_template('png.html')
	
if __name__ == "__main__":
	app.run(debug= True) #개발 끝나고 서비스 할 때는 디버그 오프 내 prompt에서 보는 함수 따로 작성해라
    # app.run(host='0.0.0.0',port='8000',debug=True) #flask 5000대 nodejs 8000대
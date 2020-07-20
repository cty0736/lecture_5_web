from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:name>/")
def hello():
	#return "Hello World!"
	#return "<html><body><h1>Hello World</h1></body></html>"
	return render_template('stylecall.html')

if __name__ == "__main__":
	app.run(debug= True) #개발 끝나고 서비스 할 때는 디버그 오프 내 prompt에서 보는 함수 따로 작성해라
    # app.run(host='0.0.0.0',port='8000',debug=True) #flask 5000대 nodejs 8000대
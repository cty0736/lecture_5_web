from flask import Flask

app = Flask(__name__) #flask 실행

@app.route("/") # @는 데코레이트, 그다음 함수 그대로 실행
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run() #서버 실행

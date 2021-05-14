from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/hello/<string:name>')  # url pattern으로 name 설정
class Hello(Resource):
    def get(self, name):  # 멤버 함수의 파라미터로 name 설정
        # name으로 받은 것을 이 안에서 처리해준다음에 
        return {"message" : "Welcome, %s!" % name} # 리턴 값으로 결과를 보내줌

@api.route('/hello')
class Bye(Resource):
    def post(self):

        global words

        words = request.json.get('words')

        return {
            "words": words
        }



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
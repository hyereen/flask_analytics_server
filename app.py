from flask import Flask, request, json, request, jsonify  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import


app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/motion/<string:name>', methods=['POST'])
class motion(Resource):
    def post(self, name):
        content = request.json
        print(content)

        combined = "안녕"
        # 안에 로직 채우기 

        return {'result' : "%s!" % combined} 


@api.route('/photo', methods = ['POST'])
class photo(Resource):
    def post(self):

        # words = request.json.get('words')

        words = ['안녕', '감사', '인사']

        return {
            "words": words
        }



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True) # 배포는 5000
    # 테스트할때는 127.0.0.1, debug = True
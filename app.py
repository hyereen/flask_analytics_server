from flask import Flask, request, json, request, jsonify  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import


app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/motion/<string:name>', methods=['GET'])
class motion(Resource):
    def get(self, name):
        content = request.json
        print(content)

        combined = "안녕"
        # 안에 로직 채우기 

        return {'result' : "%s!" % combined} 


@api.route('/photo', methods = ['GET'])
class photo(Resource):
    def get(self):

        global words

        words = request.json.get('words')

        return {
            "words": words
        }



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # 테스트할때는 127.0.0.1, app.debug = True
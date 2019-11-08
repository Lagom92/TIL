# Flask Restful에 대해 공부하자



### Flask

Python의 경량 웹 프레임워크



### Flask-RESTful

Restful API를 만들 수 있는 Flask의 확장판



- flask 설치

```
pip install flask
```



- 기본 플라스크 코드

```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```



- 출력 결과 이미지

![](../web/img/flask-hello.png)





- flask-restful library 설치

- REST API 생성을 도와주는 모듈
- Endpoint URL을 클래스와 매핑시키는 것을 도와줌

```
pip install flask-restful
```



- '/user' post 요청으로 사용자를 생성하고 응답하는 api

```python
# api.py

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}

# add this class as a resource to API library wrapper
api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)
```



- email, password 파라미터를 추가하고 파서를 사용해 파리미터를 추출

```python
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class CreateUser(Resource):
    def post(self):
        try:
            parser.add_argument('email', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']
            return {'Email': args['email'], 'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)
```





- 더하기 기능

```python
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Plus(Resource):
    def get(self):
        try:
            parser.add_argument('x', required=True, type=int, help='x cannot be blank')
            parser.add_argument('y', required=True, type=int, help='y cannot be blank')
            args = parser.parse_args()
            result = args['x'] + args['y']
            return {'result': result}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Plus, '/plus')

if __name__ == '__main__':
        app.run(debug=True)

```



















참고

[https://medium.com/@feedbotstar/python-flask-%EB%A1%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-rest-api-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0-60a29a9ebd8c](https://medium.com/@feedbotstar/python-flask-로-간단한-rest-api-작성하기-60a29a9ebd8c)



https://dev.to/aligoren/building-basic-restful-api-with-flask-restful-57oh



http://codehandbook.org/flask-restful-api-using-python-mysql/






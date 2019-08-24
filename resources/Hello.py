from flask_restful import Resource
import json
from flask import Response

class Hello(Resource):
    def get(self):
        str = 'الدول الأفريقية غير العربية'
        json_obj = {'data': str}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")
        # return {'data': str.encode('utf-16')}
        # return {"message": "Congratulations, You are successfully configured naqaba API"

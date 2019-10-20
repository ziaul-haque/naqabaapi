from flask_restful import Resource, request
from flask import Response
from Model import cache_db
from utils import get_current_date_str, get_diff_day, get_datetime_obj_from_str
import json
from datetime import datetime, timedelta
from casdb.data import get_bus_locations
from reports.common import made_database_stored_procedure_query, made_raw_sql_query, convert_immutable_dict_to_dict
from logger import logger


class Test(Resource):
    def get(self):
        result = made_raw_sql_query('select id, name,name1 from test;')
        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Companies(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_transport_companies', [])
        json_obj = {'companies': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Vehicles(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_transport_vehicles', args)
        json_obj = {'vehicles': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Mosasas(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_active_mosasas', [])
        json_obj = {'mosasas': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Maktabs(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_active_maktabs', [])
        json_obj = {'maktabs': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Locations(Resource):
    def get(self):
        kwargs = convert_immutable_dict_to_dict(request.args)
        uc_response = get_bus_locations(**kwargs)
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")

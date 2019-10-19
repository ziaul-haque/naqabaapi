from flask_restful import Resource, request
from flask import Response
from Model import cache_db
from utils import get_current_date_str, get_diff_day, get_datetime_obj_from_str
import json
from datetime import datetime, timedelta
from casdb.data import get_bus_locations
from reports.common import made_database_stored_procedure_query, made_raw_sql_query, convert_immutable_dict_to_dict


class Test(Resource):
    def get(self):
        result = made_raw_sql_query('select id, name,name1 from test;')
        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Companies(Resource):
    def get(self):
        uc_response = cache_db.get("companies")
        uc_cache_time = cache_db.get("companies_cache_time")
        if uc_cache_time:
            date_diff = get_diff_day(datetime.now(), get_datetime_obj_from_str(uc_cache_time.decode("utf-8")))

        if not uc_cache_time or date_diff > 0:
            result = made_database_stored_procedure_query('sp_get_transport_companies', [])
            json_obj = {'companies': result}
            json_response = json.dumps(json_obj, ensure_ascii=False)
            uc_response = json_response.encode('UTF-8')
            cache_db.set("companies", uc_response)
            cache_db.set("companies_cache_time", get_current_date_str())
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Vehicles(Resource):
    def get(self):
        args = request.args
        uc_response = cache_db.get("vehicles")
        uc_cache_time = cache_db.get("vehicles_cache_time")
        if uc_cache_time:
            date_diff = get_diff_day(datetime.now(), get_datetime_obj_from_str(uc_cache_time.decode("utf-8")))

        if not uc_cache_time or date_diff > 0:
            result = made_database_stored_procedure_query('sp_get_transport_vehicles', args)
            json_obj = {'vehicles': result}
            json_response = json.dumps(json_obj, ensure_ascii=False)
            uc_response = json_response.encode('UTF-8')
            cache_db.set("vehicles", uc_response)
            cache_db.set("vehicles_cache_time", get_current_date_str())
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Mosasas(Resource):
    def get(self):
        uc_response = cache_db.get("mosasas")
        uc_cache_time = cache_db.get("mosasa_cache_time")
        if uc_cache_time:
            date_diff = get_diff_day(datetime.now(), get_datetime_obj_from_str(uc_cache_time.decode("utf-8")))

        if not uc_cache_time or date_diff > 0:
            result = made_database_stored_procedure_query('sp_get_active_mosasas', [])
            json_obj = {'mosasas': result}
            json_response = json.dumps(json_obj, ensure_ascii=False)
            uc_response = json_response.encode('UTF-8')
            cache_db.set("mosasas", uc_response)
            cache_db.set("mosasa_cache_time", get_current_date_str())
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Maktabs(Resource):
    def get(self):
        uc_response = cache_db.get("maktabs")
        uc_cache_time = cache_db.get("maktabs_cache_time")
        if uc_cache_time:
            date_diff = get_diff_day(datetime.now(), get_datetime_obj_from_str(uc_cache_time.decode("utf-8")))

        if not uc_cache_time or date_diff > 0:
            result = made_database_stored_procedure_query('sp_get_active_maktabs', [])
            json_obj = {'maktabs': result}
            json_response = json.dumps(json_obj, ensure_ascii=False)
            uc_response = json_response.encode('UTF-8')
            cache_db.set("maktabs", uc_response)
            cache_db.set("maktabs_cache_time", get_current_date_str())
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Locations(Resource):
    def get(self):
        kwargs = convert_immutable_dict_to_dict(request.args)
        # uc_response = get_bus_locations(kwargs['start_datetime'])
        # start_date = kwargs['start_datetime']
        # end_time = kwargs['end_datetime']

        uc_response = get_bus_locations(**kwargs)
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")

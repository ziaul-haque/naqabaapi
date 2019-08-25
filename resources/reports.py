from flask_restful import Resource, request
from flask import Response
from flask_api import status
from logger import logger

import json

from reports.common import made_database_stored_procedure_query, made_raw_sql_query


class Test(Resource):
    def get(self):
        result = made_raw_sql_query('select id, name,name1 from test;')
        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        uc_response = json_response.encode('UTF-8')
        return Response(uc_response, content_type="application/json; charset=utf-8", mimetype="application/json;")


class Companies(Resource):
    def get(self):
        try:
            result = made_database_stored_procedure_query('sp_get_transport_companies', [])
            return result
        except Exception as e:
            logger.info('execution failed, ' + str(e))


class Vehicles(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_transport_vehicles', args)
        return result


class Mosasas(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_active_mosasa', [])
        return result


class Locations(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_vehicle_location', args)
        return result

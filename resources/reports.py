from flask_restful import Resource, request
from flask import Response
import json

from reports.common import made_database_stored_procedure_query


class Companies(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_transport_companies', [])

        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        response = Response(json_response, content_type="application/json; charset=utf-8")

        if not result:
            return
        else:
            return response


class Vehicles(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_transport_vehicles', args)

        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        response = Response(json_response, content_type="application/json; charset=utf-8")

        if not result:
            return
        else:
            return response


class Mosasas(Resource):
    def get(self):
        result = made_database_stored_procedure_query('sp_get_active_mosasa', [])

        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        response = Response(json_response, content_type="application/json; charset=utf-8")

        if not result:
            return
        else:
            return response


class Locations(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_vehicle_location', args)

        json_obj = {'data': result}
        json_response = json.dumps(json_obj, ensure_ascii=False)
        response = Response(json_response, content_type="application/json; charset=utf-8")

        if not result:
            return
        else:
            return response

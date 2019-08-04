from flask_restful import Resource, request

from reports.common import made_raw_sql_query, made_database_stored_procedure_query


class Companies(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_transport_companies', '')

        if not result:
            return
        else:
            return result


class Vehicles(Resource):
    def get(self):
        args = request.args
        result = made_database_stored_procedure_query('sp_get_transport_vehicles', args)
        if not result:
            return
        else:
            return result

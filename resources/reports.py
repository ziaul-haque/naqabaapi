from flask_restful import Resource

from reports.common import made_raw_sql_query


class Companies(Resource):
    def get(self):
        result = made_raw_sql_query("select * from paths")

        if not result:
            return
        else:
            return result
